---
name: verification-and-stop
description: Check action-completion claims, partial or mismatched tool results and repetitive calls. Use before saying saved, installed, deployed, fixed or operationally verified, and when deciding whether to continue a failing loop; skip routine tool-free replies and complete simple factual reads.
---

# Verification and stop — v0.2.1

Use `intelligent-tool-routing` §4 for the localized final status template. Research branch counters are owned by `deep-research-routing` §3, not by a global tool-call limit.

## 1. Inspect relevant results

- [ ] Inspect success/error/pending state and every relevant batch item; do not invent a status code the tool does not expose.
- [ ] Check that the requested scope is complete: required fields, relevant truncation and needed pages. Do not exhaust irrelevant pagination solely to complete a checklist.
- [ ] Match entity, installed/requested version, jurisdiction and time period. Historical questions may intentionally use older sources; schedules may intentionally have future dates.
- [ ] Treat null/missing fields as unknown, not zero or proof of absence.
- [ ] Inspect the underlying source when a precise claim exceeds snippet evidence.

Mark a genuinely inapplicable check N/A with a brief reason. Schema-valid output can still be incomplete or wrong.

## 2. Match the claim to evidence

| Claim | Minimum evidence |
| --- | --- |
| Drafted | Content exists in the reply or local working file; specify location when useful. |
| Locally validated | Relevant checks executed and inspected, with their actual outcome. |
| Saved/committed | The applicable local/file/provider/repository operation succeeded; distinguish local from durable/account storage. |
| Created/published remotely | Provider response proves that specific state and audience. |
| Deployed | Target deployment reached its provider's deployment-success state; a push alone is insufficient. |
| Installed/enabled/connected | Host listing/status or actual supported capability proves that particular state. |
| Operationally verified | Intended behavior observed in the target environment; a ping proves reachability only. |

These are separate claims, not a mandatory linear ladder. A generated archive does not prove installation; a build does not prove runtime correctness; plan-only examples do not measure real-world reliability. Reuse still-valid evidence when nothing relevant changed.

## 3. Decide whether another call is justified

Continue only for at least one concrete task gain: new required evidence/identifier/source category; meaningful independent verification; deeper necessary extraction; schema/capability discovery; reduced material uncertainty; an authorized action; required validation; or contract-compliant polling/recovery.

Stop redundant work when the requested outcome is supported and necessary actions/checks are complete. Do not stop useful work solely because a soft budget is exceeded, an A/B source already exists, a branch closed or a job returned pending. For a blocked target, continue unaffected work and report the actual boundary. Inspect state before retrying an uncertain mutation; follow tool-specific retry/polling contracts.

## 4. Report accurately

Use only applicable core status lines in the user's language. State the exact completed state and evidence; include outstanding work/blockers only when material. Distinguish facts, attributed claims, estimates, inferences and unverified behavior. Never claim calls/tests/saves/installation/performance without records. Complete a reviewable result before requesting a new external action; existing applicable authorization remains valid.
