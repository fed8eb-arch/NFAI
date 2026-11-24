# W2 HubSpot custom property mapping (plan only)

Follows the Marketing owner spec v1.2 (`w2-ga4-source-field.md`, commit `62e20fd`) §5. Nothing was created in HubSpot (W1 has not run). No secrets, no portal ID.

**Limit (official):** HubSpot Free allows **10 custom properties in total** across contacts, companies, and deals, not 10 per object. Source, checked 2026-11-23: [Free Tools catalog](https://legal.hubspot.com/hubspot-product-and-services-catalog/free-tools).

Marketing’s plan uses **2 of 10** contact properties. UTM fields should use HubSpot standard properties if they exist on the Free account after W1; do not spend extra custom-property slots on UTMs until that is verified.

## Recommended contact properties (2 of 10)

Create after W1, on Contacts, group `contactinformation`. Internal names and option keys must match the form (`how_did_you_hear_about_us`). Do not add an `unknown` option; that is a reporting bucket only.

### 1. `how_did_you_hear_about_us`

| | |
|---|---|
| Label | How did you hear about us? |
| Type / field type | `enumeration` / `select` |
| Required in HubSpot? | No (the website select is required; older leads may be blank) |

| Label | Value |
|---|---|
| GC / general contractor referral | `gc_referral` |
| Tender or bid platform | `tenders` |
| LinkedIn | `linkedin` |
| AI assistant (ChatGPT, Perplexity, etc.) | `ai_assistant` |
| Google or other search | `search` |
| Referral from a colleague/past client | `referral` |
| Other (please specify) | `other` |

```json
{
  "groupName": "contactinformation",
  "name": "how_did_you_hear_about_us",
  "label": "How did you hear about us?",
  "type": "enumeration",
  "fieldType": "select",
  "options": [
    {"label": "GC / general contractor referral", "value": "gc_referral", "displayOrder": 0, "hidden": false},
    {"label": "Tender or bid platform", "value": "tenders", "displayOrder": 1, "hidden": false},
    {"label": "LinkedIn", "value": "linkedin", "displayOrder": 2, "hidden": false},
    {"label": "AI assistant (ChatGPT, Perplexity, etc.)", "value": "ai_assistant", "displayOrder": 3, "hidden": false},
    {"label": "Google or other search", "value": "search", "displayOrder": 4, "hidden": false},
    {"label": "Referral from a colleague/past client", "value": "referral", "displayOrder": 5, "hidden": false},
    {"label": "Other (please specify)", "value": "other", "displayOrder": 6, "hidden": false}
  ]
}
```

### 2. `how_did_you_hear_about_us_other`

| | |
|---|---|
| Label | How did you hear about us (other) |
| Type / field type | `string` / `text` |
| When to set | Only if `how_did_you_hear_about_us` is `other`; otherwise empty |
| Max length on the form | 200 |
| Public repo | Never write this free text into NFAI or into GA4 |

```json
{
  "groupName": "contactinformation",
  "name": "how_did_you_hear_about_us_other",
  "label": "How did you hear about us (other)",
  "type": "string",
  "fieldType": "text"
}
```

Do not write raw UTM values into HubSpot-managed `hs_analytics_*` properties via the API. Do not create these properties until W1 exists.
