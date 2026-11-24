/* NFAI Growth OS — offline Creative System QC (Node.js >=18, no dependencies).
 * Founder-authorized implementation, 2026-11-24. No network/API calls.
 * Usage: node creative-qc.cjs --self-test
 *        node creative-qc.cjs /path/to/authorized-aggregate.json
 * JSON schema and synthetic example are in selfTest below. Input/output is private
 * unless explicitly sanitized and approved. IDs are opaque; do not include PII,
 * credentials, customer text or raw ad assets. Output to stdout only.
 * This is QC/glue, not an ad platform, attribution engine, or automatic publisher.
 * Human acceptance and statistical validation remain required.
 */
function creativeQC(input) {
  "use strict";
  const fail = (m) => { throw new Error(m); };
  const object = v => v !== null && typeof v === "object" && !Array.isArray(v);
  const id = v => typeof v === "string" && /^[A-Za-z0-9][A-Za-z0-9_.:-]{0,79}$/.test(v);
  const int = v => Number.isSafeInteger(v) && v >= 0;
  const date = v => typeof v === "string" && /^\d{4}-\d{2}-\d{2}$/.test(v) &&
    !Number.isNaN(Date.parse(v)) && new Date(v).toISOString().slice(0,10) === v;
  const keys = (o, required, optional=[]) => object(o) &&
    required.every(k=>Object.prototype.hasOwnProperty.call(o,k)) &&
    Object.keys(o).every(k=>required.includes(k)||optional.includes(k));
  const ratio = (n,d) => d === 0 ? null : Math.round((n/d)*1e6)/1e6;
  if (!keys(input, ["schema","data_kind","min_clicks","min_qualified","creatives"], ["observations"])) fail("invalid input schema");
  if (input.schema !== "nfai-creative-qc-v1" || !["actual","synthetic"].includes(input.data_kind)) fail("invalid schema or data kind");
  if (!int(input.min_clicks)||input.min_clicks<1||!int(input.min_qualified)||input.min_qualified<1) fail("positive thresholds required");
  if (!Array.isArray(input.creatives)||input.creatives.length>10000) fail("invalid creative array");
  const required=["creative_id","platform","campaign_id","segment_id","funnel_id","window_start","window_end","currency","attribution","evidence_id","persona","hook","body","angle","prompt_version","impressions","clicks","leads","qualified","sales","spend_minor","revenue_minor","gross_profit_minor"];
  const labels=["creative_id","platform","campaign_id","segment_id","funnel_id","evidence_id","persona","hook","body","angle","prompt_version"];
  const nums=["impressions","clicks","leads","qualified","sales","spend_minor","revenue_minor","gross_profit_minor"];
  const seen=new Set(), groups=new Map();
  for (let i=0;i<input.creatives.length;i++) {
    const r=input.creatives[i], p=`creative row ${i+1}: `;
    if (!keys(r,required)||!labels.every(k=>id(r[k]))||!nums.every(k=>int(r[k]))) fail(p+"invalid fields; use opaque IDs and nonnegative integer minor units");
    if (!date(r.window_start)||!date(r.window_end)||r.window_start>r.window_end||!/^([A-Z]{3})$/.test(r.currency)||r.attribution!=="click_cohort") fail(p+"invalid window/currency/attribution");
    if (r.clicks>r.impressions||r.leads>r.clicks||r.qualified>r.leads||r.sales>r.qualified||r.gross_profit_minor>r.revenue_minor||(r.sales===0&&r.revenue_minor!==0)) fail(p+"inconsistent click-cohort totals");
    const key=JSON.stringify([r.platform,r.campaign_id,r.segment_id,r.funnel_id,r.window_start,r.window_end,r.currency,r.attribution]);
    const unique=JSON.stringify([key,r.creative_id]);
    if(seen.has(unique)) fail(p+"duplicate creative within comparison group");
    seen.add(unique);
    const eligible=r.clicks>=input.min_clicks&&r.qualified>=input.min_qualified&&r.spend_minor>0;
    const result={creative_id:r.creative_id,evidence_id:r.evidence_id,persona:r.persona,hook:r.hook,body:r.body,angle:r.angle,prompt_version:r.prompt_version,impressions:r.impressions,clicks:r.clicks,leads:r.leads,qualified:r.qualified,sales:r.sales,spend_minor:r.spend_minor,revenue_minor:r.revenue_minor,gross_profit_minor:r.gross_profit_minor,ctr:ratio(r.clicks,r.impressions),qualification_rate:ratio(r.qualified,r.leads),sale_rate:ratio(r.sales,r.qualified),cpql_minor:ratio(r.spend_minor,r.qualified),cac_minor:ratio(r.spend_minor,r.sales),roas:ratio(r.revenue_minor,r.spend_minor),contribution_after_ads_minor:r.gross_profit_minor-r.spend_minor,comparison_eligible:eligible,reason:eligible?"thresholds_met":"insufficient_clicks_qualified_or_spend"};
    if(!groups.has(key)) groups.set(key,[]);
    groups.get(key).push(result);
  }
  const observations=input.observations===undefined?[]:input.observations;
  if(!Array.isArray(observations)||observations.length>10000) fail("invalid observation array");
  const obsSeen=new Set();
  const signals=observations.map((o,i)=>{
    if(!keys(o,["ad_id","advertiser_id","market","observed_on","evidence_id","source"],["active_days","copies","reach"])||
      !["ad_id","advertiser_id","market","evidence_id"].every(k=>id(o[k]))||!date(o.observed_on)||!["manual_public","authorized_export"].includes(o.source)||
      !["active_days","copies","reach"].every(k=>o[k]===undefined||o[k]===null||int(o[k]))) fail(`observation row ${i+1}: invalid source or fields`);
    const k=JSON.stringify([o.market,o.advertiser_id,o.ad_id,o.observed_on]);
    if(obsSeen.has(k)) fail(`observation row ${i+1}: duplicate`);
    obsSeen.add(k);
    return {...o,active_days:o.active_days??null,copies:o.copies??null,reach:o.reach??null,interpretation:"proxy_only_not_performance"};
  });
  return {schema:"nfai-creative-qc-report-v1",data_kind:input.data_kind,decision:"human_review_required_no_automatic_winner",limitations:["click-cohort counts only; no view-through or repeat-sale attribution","gross profit input is nonnegative before advertising; losses below zero need a separate accounting model","thresholds are eligibility gates, not statistical significance","comparison is descriptive, not causal","competitor observations are not sales or ROI"],groups:[...groups.entries()].map(([k,rows])=>({comparison_key:JSON.parse(k),eligible_count:rows.filter(r=>r.comparison_eligible).length,rows:rows.sort((a,b)=>Number(b.comparison_eligible)-Number(a.comparison_eligible)||(a.cpql_minor??Infinity)-(b.cpql_minor??Infinity)||a.creative_id.localeCompare(b.creative_id))})),competitor_observations:signals};
}

function selfTest() {
  const assert=(condition,msg)=>{if(!condition)throw new Error(msg)};
  const row={creative_id:"a",platform:"meta",campaign_id:"c",segment_id:"s",funnel_id:"f",window_start:"2026-11-01",window_end:"2026-11-07",currency:"USD",attribution:"click_cohort",evidence_id:"synthetic-1",persona:"p",hook:"h",body:"b",angle:"g",prompt_version:"v1",impressions:1000,clicks:100,leads:20,qualified:10,sales:2,spend_minor:10000,revenue_minor:50000,gross_profit_minor:25000};
  const base={schema:"nfai-creative-qc-v1",data_kind:"synthetic",min_clicks:50,min_qualified:5,creatives:[row]};
  const checks=[];
  function check(name,fn){fn();checks.push(name);}
  function rejects(v){let ok=false;try{creativeQC(v)}catch(e){ok=true}assert(ok,"expected rejection");}
  check("exact metrics",()=>{const r=creativeQC(base).groups[0].rows[0];assert(r.cpql_minor===1000&&r.cac_minor===5000&&r.ctr===0.1&&r.roas===5&&r.contribution_after_ads_minor===15000,"metrics");});
  check("no causal winner",()=>assert(creativeQC(base).decision==="human_review_required_no_automatic_winner","decision"));
  check("same cohort ordering",()=>{const x=creativeQC({...base,creatives:[row,{...row,creative_id:"b",spend_minor:5000}]});assert(x.groups.length===1&&x.groups[0].rows[0].creative_id==="b","order");});
  check("segment separation",()=>assert(creativeQC({...base,creatives:[row,{...row,segment_id:"other"}]}).groups.length===2,"segment"));
  check("currency separation",()=>assert(creativeQC({...base,creatives:[row,{...row,currency:"EUR"}]}).groups.length===2,"currency"));
  check("period separation",()=>assert(creativeQC({...base,creatives:[row,{...row,window_end:"2026-11-08"}]}).groups.length===2,"period"));
  check("zero denominators",()=>{const r=creativeQC({...base,creatives:[{...row,clicks:0,leads:0,qualified:0,sales:0,revenue_minor:0,gross_profit_minor:0,spend_minor:0}]}).groups[0].rows[0];assert(r.cpql_minor===null&&r.cac_minor===null&&r.roas===null&&!r.comparison_eligible,"zeros");});
  check("low sample",()=>assert(!creativeQC({...base,min_clicks:101}).groups[0].rows[0].comparison_eligible,"threshold"));
  check("duplicate rejected",()=>rejects({...base,creatives:[row,row]}));
  check("invalid date rejected",()=>rejects({...base,creatives:[{...row,window_start:"2026-02-30"}]}));
  check("negative spend rejected",()=>rejects({...base,creatives:[{...row,spend_minor:-1}]}));
  check("invalid funnel rejected",()=>rejects({...base,creatives:[{...row,qualified:21}]}));
  check("extra fields rejected",()=>rejects({...base,creatives:[{...row,token:"ignored"}]}));
  check("missing metric rejected",()=>{const x={...row};delete x.sales;rejects({...base,creatives:[x]});});
  check("proxy separate",()=>{const r=creativeQC({...base,observations:[{ad_id:"ad",advertiser_id:"adv",market:"US",observed_on:"2026-11-24",evidence_id:"obs1",source:"manual_public",active_days:60}]});assert(r.competitor_observations[0].reach===null&&r.competitor_observations[0].interpretation==="proxy_only_not_performance","proxy");});
  check("unapproved source rejected",()=>rejects({...base,observations:[{ad_id:"ad",advertiser_id:"adv",market:"US",observed_on:"2026-11-24",evidence_id:"obs1",source:"scraped"}]}));
  return {passed:checks.length,checks};
}

module.exports = { creativeQC, selfTest };
if (require.main === module) {
  try {
    const arg=process.argv[2];
    if(process.argv.length!==3) throw new Error("usage: node creative-qc.cjs --self-test | INPUT.json");
    if(arg==="--self-test") process.stdout.write(JSON.stringify(selfTest(),null,2)+"\n");
    else {
      const fs=require("node:fs");
      if(!fs.statSync(arg).isFile()||fs.statSync(arg).size>8*1024*1024) throw new Error("input must be a local file of at most 8 MiB");
      const report=creativeQC(JSON.parse(fs.readFileSync(arg,"utf8").replace(/^\uFEFF/,"")));
      process.stdout.write(JSON.stringify(report,null,2)+"\n");
    }
  } catch(e) {
    // Never echo malformed input, file paths, tokens, or parser snippets.
    process.stderr.write("Creative QC failed. Check schema, file and arguments locally.\n");
    process.exitCode=1;
  }
}
