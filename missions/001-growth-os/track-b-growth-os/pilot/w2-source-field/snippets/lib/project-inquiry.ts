export const projectPhases = ["Planning", "Bidding", "Construction", "Expansion or retrofit", "Other"];

/** Self-reported inquiry source. Keys and labels: Marketing spec v1.2 (w2-ga4-source-field.md, commit 62e20fd) §4. Implement verbatim. */
export const leadSources = [
  { value: "gc_referral", label: "GC / general contractor referral" },
  { value: "tenders", label: "Tender or bid platform" },
  { value: "linkedin", label: "LinkedIn" },
  { value: "ai_assistant", label: "AI assistant (ChatGPT, Perplexity, etc.)" },
  { value: "search", label: "Google or other search" },
  { value: "referral", label: "Referral from a colleague/past client" },
  { value: "other", label: "Other (please specify)" },
] as const;

export type LeadSourceValue = (typeof leadSources)[number]["value"];

export const leadSourceValues: readonly string[] = leadSources.map((item) => item.value);

export const inquiryLimits = {
  name: 100,
  company: 150,
  email: 254,
  location: 150,
  phase: 40,
  message: 2000,
  how_did_you_hear_about_us: 40,
  how_did_you_hear_about_us_other: 200,
  utm_source: 200,
  utm_medium: 200,
  utm_campaign: 200,
  utm_term: 200,
  utm_content: 200,
  referrer_host: 253,
  landing_path: 200,
};

export const attributionFields = [
  "utm_source",
  "utm_medium",
  "utm_campaign",
  "utm_term",
  "utm_content",
  "referrer_host",
  "landing_path",
] as const;

export type AttributionField = (typeof attributionFields)[number];

export const inquiryEmail = /^[^\s@<>]+@[^\s@<>]+\.[^\s@<>]+$/;

/** Trim, strip control characters, and cap length. Hidden attribution must not block a valid inquiry. */
export function sanitizeAttribution(raw: unknown, max: number): string {
  if (typeof raw !== "string") return "";
  const value = raw.replace(/[\u0000-\u001F\u007F]/g, " ").replace(/\s+/g, " ").trim();
  return value.length > max ? value.slice(0, max) : value;
}
