"use client";

import Link from "next/link";
import { type FormEvent, useEffect, useRef, useState } from "react";
import {
  attributionFields,
  inquiryLimits,
  leadSources,
  projectPhases,
  type AttributionField,
} from "@/lib/project-inquiry";

type Field = keyof typeof inquiryLimits;
type Errors = Partial<Record<Field, string>>;

const fields = [
  { name: "name", label: "Name", type: "text", autoComplete: "name" },
  { name: "company", label: "Company", type: "text", autoComplete: "organization" },
  { name: "email", label: "Work email", type: "email", autoComplete: "email" },
  { name: "location", label: "Project city and state", type: "text", autoComplete: "off" },
] as const;

const FIRST_TOUCH_KEY = "wr_first_touch_v1";

type Attribution = Record<AttributionField, string>;

function emptyAttribution(): Attribution {
  return {
    utm_source: "",
    utm_medium: "",
    utm_campaign: "",
    utm_term: "",
    utm_content: "",
    referrer_host: "",
    landing_path: "",
  };
}

function looksLikeEmail(value: string): boolean {
  return /[^\s@]+@[^\s@]+\.[^\s@]+/.test(value);
}

function hostnameOf(referrer: string): string {
  if (!referrer) return "";
  try {
    return new URL(referrer).hostname;
  } catch {
    return "";
  }
}

function readAttribution(): Attribution {
  const params = new URLSearchParams(window.location.search);
  const current = emptyAttribution();
  for (const key of ["utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content"] as const) {
    const value = (params.get(key) ?? "").trim();
    current[key] = looksLikeEmail(value) ? "" : value;
  }
  current.referrer_host = hostnameOf(document.referrer ?? "");
  current.landing_path = window.location.pathname;
  try {
    const savedRaw = sessionStorage.getItem(FIRST_TOUCH_KEY);
    if (savedRaw) {
      const saved = JSON.parse(savedRaw) as Partial<Attribution>;
      const merged = emptyAttribution();
      for (const key of attributionFields) {
        const first = typeof saved[key] === "string" ? saved[key] : "";
        merged[key] = first || current[key];
      }
      return merged;
    }
    sessionStorage.setItem(FIRST_TOUCH_KEY, JSON.stringify(current));
  } catch {
    // sessionStorage may be blocked; still return the current page values.
  }
  return current;
}

export function ProjectInquiryForm() {
  const [pending, setPending] = useState(false);
  const [status, setStatus] = useState("");
  const [errors, setErrors] = useState<Errors>({});
  const [sent, setSent] = useState(false);
  const [showOther, setShowOther] = useState(false);
  const [attribution, setAttribution] = useState<Attribution>(emptyAttribution);
  const requestId = useRef("");
  const inFlight = useRef(false);

  useEffect(() => {
    setAttribution(readAttribution());
  }, []);

  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (inFlight.current) return;
    inFlight.current = true;
    const form = event.currentTarget;
    setPending(true);
    setSent(false);
    setErrors({});
    setStatus("");
    try {
      requestId.current ||= crypto.randomUUID();
      const payload = Object.fromEntries(new FormData(form));
      if (payload.how_did_you_hear_about_us !== "other") {
        payload.how_did_you_hear_about_us_other = "";
      }
      // Client-side only: the current /api/contact route is unchanged (Director).
      // Extra keys are sent in the JSON body but are not validated or added to the
      // Resend email until a later, approved route.ts change.
      const response = await fetch("/api/contact", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ...payload, requestId: requestId.current }),
      });
      const result = await response.json() as { sent?: boolean; error?: string; fields?: Errors };
      if (response.ok && result.sent) {
        form.reset();
        setShowOther(false);
        requestId.current = "";
        setSent(true);
        setStatus("Your project inquiry was sent.");
      } else {
        setErrors(result.fields ?? {});
        setStatus(result.error ?? "We couldn't send your inquiry. Try again.");
        const first = Object.keys(result.fields ?? {})[0];
        if (first) requestAnimationFrame(() => {
          const input = form.elements.namedItem(first);
          if (input instanceof HTMLElement) input.focus();
        });
      }
    } catch {
      setStatus("We couldn't confirm sending your inquiry. Try again.");
    } finally {
      inFlight.current = false;
      setPending(false);
    }
  }

  function feedback(field: Field) {
    return errors[field] && <span className="wc-form-error" id={`inquiry-${field}-error`}>{errors[field]}</span>;
  }

  function validation(field: Field) {
    return {
      "aria-invalid": errors[field] ? true : undefined,
      "aria-describedby": errors[field] ? `inquiry-${field}-error` : undefined,
    };
  }

  return <form className="wc-form" method="post" onSubmit={submit} onChange={() => { requestId.current = ""; }}>
    <noscript><p className="wc-wide">Enable JavaScript to send a project inquiry.</p></noscript>
    {fields.map(({ name, label, type, autoComplete }) => <label key={name}>
      {label}
      <input name={name} type={type} autoComplete={autoComplete} maxLength={inquiryLimits[name]} required {...validation(name)} />
      {feedback(name)}
    </label>)}
    <label className="wc-wide">Project phase
      <select name="phase" defaultValue="" required {...validation("phase")}>
        <option value="" disabled>Select the phase</option>
        {projectPhases.map(phase => <option key={phase}>{phase}</option>)}
      </select>
      {feedback("phase")}
    </label>
    <label className="wc-wide">How did you hear about us?
      <select
        name="how_did_you_hear_about_us"
        defaultValue=""
        required
        {...validation("how_did_you_hear_about_us")}
        onChange={(event) => setShowOther(event.target.value === "other")}
      >
        <option value="" disabled>Select one option</option>
        {leadSources.map((source) => <option key={source.value} value={source.value}>{source.label}</option>)}
      </select>
      {feedback("how_did_you_hear_about_us")}
    </label>
    <label className="wc-wide wc-other-detail" hidden={!showOther}>Please specify
      <input
        name="how_did_you_hear_about_us_other"
        type="text"
        maxLength={inquiryLimits.how_did_you_hear_about_us_other}
        required={showOther}
        autoComplete="off"
        {...validation("how_did_you_hear_about_us_other")}
      />
      {feedback("how_did_you_hear_about_us_other")}
    </label>
    <label className="wc-wide">Scope and schedule
      <textarea name="message" rows={6} maxLength={inquiryLimits.message} required {...validation("message")} />
      {feedback("message")}
    </label>
    <label className="wc-honeypot" aria-hidden="true">Website<input name="website" tabIndex={-1} autoComplete="off" /></label>
    {attributionFields.map((name) => (
      <input key={name} type="hidden" name={name} value={attribution[name]} readOnly />
    ))}
    {/* Legal notice from w2-consent-text.md §1a, placed above the submit button, no checkbox.
        GA sentences (§1a second sentence and §1b) omitted: no GA4 tag is installed.
        "We do not sell or share…" omitted (unconfirmed). Contact-email clause omitted (preview fallback: end at "for details."). */}
    <p className="wc-wide wc-consent">We use the details you submit (name, company, work email, project location, phase, how you heard about us, and your message) to respond to your inquiry. See our <Link href="/privacy">Privacy Notice</Link> for details.</p>
    <button className="wc-button wc-wide" type="submit" disabled={pending}>{pending ? "Sending…" : "Send project inquiry"} <span aria-hidden="true">↗</span></button>
    <p className={`wc-wide ${sent ? "" : "wc-form-error"}`} role="status" aria-live="polite" aria-atomic="true">{status}</p>
  </form>;
}
