# Source of Truth Priority

Authority is scope-bound. File existence, recency, task inclusion, or conversation does not create approval.

| Priority / source | Authority and permitted use | Prohibited use | Conflict handling / evidence |
| --- | --- | --- | --- |
| 1. Accepted Project Bible, Constitution, and governing documents, including [DS-PC — HOW](DS_PC_001_PROGRAM_CHARTER.md) and [DS-SPD — WHAT](DS_SPD_001_STRATEGIC_PROGRAM_DIRECTIVE.md) under `FD-DS-PROGRAM-001` | Govern only within declared approved scope; DS-PC and DS-SPD operate as companion program sources | Cannot be weakened by supporting records; cannot approve surrounding Draft content or bypass a more specific accepted decision or gate | Preserve accepted text, the `HOW`/`WHAT` relationship, and traceability |
| 2. Explicit Founder-approved decisions and accepted ADRs | Decide only their recorded scope | Cannot approve surrounding Draft content | Require recorded decision ID/scope |
| 3. Current Founder task instruction | Defines immediate scope and permission | Cannot silently amend durable authority | Preserve task evidence; promote durable decisions through governance |
| 4. Approved Product Foundation | Canonical taxonomy/attribute foundations | No invented terms or commercial validity | Require approval/provenance |
| 5. Approved Product DNA | Reusable product structure and ownership | Does not prove product facts or runtime state | Resolve against governing Product sources |
| 6. Approved Master Data | Approved product values and relations | Candidate/missing data cannot be promoted | Require row status, provenance, and review |
| 7. Approved Knowledge Repository | Canonical explanations and evidence-backed knowledge | Must not create product identity/facts | Reference canonical IDs and sources |
| 8. Approved Market Intelligence | Approved market context | Must not override product/business truth | Date, source, owner, and scope required |
| 9. Competitor Research | Supplementary terminology/presentation evidence | Cannot override Founder or canonical data | Record source/date; classify as supplementary |
| 10. External Research | Only when explicitly requested | Cannot become authority by citation alone | Prefer primary sources and record review |
| 11. Audit Reports | Current-state evidence and findings | Not governing approval | Reconcile with higher authority |
| 12. Conversation, AI Memory, Slack Summaries, and Handoffs | Convenience context and evidence locators only | Cannot establish authority, approval, current state, scope, or durable canonical data; `Handoff != Authority` | Re-resolve Repository state independently and promote durable facts only through the approved Repository owner and process |

`FD-DS-PROGRAM-001` accepts DS-PC and DS-SPD as companion program-level governing sources. It does not silently approve the full Draft Project Bible or Constitution, supersede CP-001 through CP-010, accepted Founder decisions or ADRs, accepted architecture, source-priority controls, production controls, `GOV-XD-00` history, or domain roadmaps. More specific accepted authority continues to control its recorded scope.

Competitor research may inform alternative names, search aliases, FAQ ideas, market language, customer questions, UX inspiration, content gaps, and presentation patterns.

Competitor research may not override Founder product specifications, taxonomy ownership, material/alloy availability, compatibility, installation requirements, business/pricing models, SKU rules, product-family boundaries, or approved WordPress architecture.

When sources conflict: confirm scope/status, apply higher accepted authority, preserve the explicit in-scope Founder decision, and use more specific approved peer authority only when it does not violate a parent rule. If unresolved, stop and request a recorded Founder decision; never invent a replacement rule.

Repository state wins within the applicable scope when it conflicts with ChatGPT memory, Claude memory/context, Codex prior-session state, Slack summaries, prior handoffs, or conversation history. If accepted Repository authority itself conflicts materially and scope/status checks cannot resolve it, return `STOP — CONTEXT_NOT_ESTABLISHED` before mutation.
