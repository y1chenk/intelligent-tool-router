---
name: deep-research-routing
description: Route multi-source public research and recursive pivots for dig, deep dig, search everything, 深挖 and 全網搜. Track provenance, branch closure, conflicts and evidence quality; use for archival/file/dataset investigations and substantial fact-checking, not a routine single-source fact or live project diagnosis.
---

# Deep research routing — v0.2.1

Use `intelligent-tool-routing` for capabilities and `verification-and-stop` for general inspection/continuation. Research depth does not cap required verification.

## 1. Scope and depth

Resolve entity/version/period ambiguity. Start from authoritative relevant evidence; widen categories only when they answer a concrete question. Prefer supported APIs/bulk exports when useful and respect robots and rate limits.

| Mode | Coverage | Default presentation, subject to user/host requirements |
| --- | --- | --- |
| find | Retrieve the specified item and verify identity. | Brief answer with complete source URL and dates. |
| dig | Main relevant categories and material gaps. | Summary, findings and coverage limits. |
| deep dig | Recursive promising identifiers and consequential verification. | Fuller evidence-linked findings and branch limits. |
| search everything | Maximum relevant lawful coverage. | State covered and uncovered categories; never claim exhaustive internet coverage. |

Use verified public or authorized sources. Check uncertain access/publication intent instead of exploiting misconfiguration. Exclude breached/leaked material, access-control bypass, unauthorized probing and privacy-invasive dossiers. Relevant openly licensed/scientific/public-domain metadata is eligible. Bound downloads to justified size/scope; inspect metadata/content without executing downloaded programs.

## 2. Record observable state

For a multi-branch investigation or complex provenance, maintain a task-local ledger using [ledger.schema.json](references/ledger.schema.json); [ledger-example.json](references/ledger-example.json) demonstrates the shape. Follow [ledger-versioning.md](references/ledger-versioning.md) when extending or migrating persisted records. For a small single-branch question, use a compact record instead of adding schema overhead solely because a call counter crossed two.

Store identifiers, canonical query signatures, observed evidence, URLs, dates, next pivots and closure reasons; exclude private details, credentials and hidden reasoning. Validate with an available JSON Schema validator before relying on a persisted ledger. If none is available, label structural validation pending. Schema conformance does not prove factual correctness or temporal state transitions.

## 3. Pivot, close, backtrack

Follow identifier → search → new identifier → verify → pivot. Use platform-supported exact strings/site/filetype/date operators. Pivot filenames through project/release/directory records and lawful mirrors; use authoritative DOI/repo/dataset records. Use archives early for removed files or chronology; archived statements remain historical until re-verified.

Emit one short `[PIVOT] <observable source> → <next source>` progress note per material direction change in dig and deeper; this is a user-visible activity summary, not hidden reasoning.

After three consecutive materially distinct searches produce no meaningful evidence/identifier, close only that branch as `no-new-evidence`. Reset its counter on a meaningful find. Also close on sufficient evidence, exhausted leads, out-of-scope, access boundaries or irrecoverable tool failure; record the actual reason. A failed connector means `tool-failure`, not that data is absent.

Backtrack to the last successful identifier only if it has an untried relevant alternative. Deduplicate prior query signatures and avoid reopening the same exhausted path. If no promising alternative remains, finish with coverage limits; do not create endless new searches. Polling, authorized actions and required checks do not count as unsuccessful searches.

## 4. Verify, grade, deliver

Normalize while preserving original values and row-level provenance. Deduplicate copied/syndicated sources. Resolve conflicts by entity, definition, units, version, sample and event/source date; explain evidence weight and unresolved gaps rather than averaging incompatible numbers.

Grade source provenance separately from claim type/confidence: A official primary; B official mirror/repository or government/academic; C identified secondary reporting or technical community; D aggregator/unsourced. Original measurements can be primary within the originator's scope. Preserve more specific user definitions. Label values `measured`, `estimated`, `reported` or `inferred`; an official provider's estimate remains an estimate, not automatically D-grade. Attribute single-source statements; do not assert unsupported or D-grade claims as established fact. Never imply an independent confirmation merely because URLs differ.

Use actual observation date in the user's timezone; record known source dates separately and unknown dates as unknown. Crawl time alone does not prove freshness. Findings need complete directly accessible URLs; put unverified/no-URL leads in an appendix.

For dig and deeper use:

| Finding | Identifiers | Source URL | Evidence Grade | Confidence | Date Observed |
| --- | --- | --- | --- | --- | --- |

Keep grade and confidence separate, and retain required user date tags/citations. If the user requires this table for every engagement, honor that requirement even in find mode. End with: `Covered: <categories>. Not covered: <categories and actual reasons>.` Include closed-branch/access limits and optional requested CSV/JSON. Localize prose. Use the core routing status template only for an actual action/completion report.
