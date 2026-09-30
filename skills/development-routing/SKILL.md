---
name: development-routing
description: Inspect evidence and select engineering tools for code changes, debugging, deployment failures, database/runtime issues and version-specific API questions. Triggers include fix bug, build failed, 部署失敗 and 除錯; skip pure conceptual explanations without a project or versioned usage question.
---

# Development routing — v0.2.1

Use `intelligent-tool-routing` for capability/authorization decisions and `verification-and-stop` for completion claims.

## 1. Diagnose with applicable evidence

Before changing state, establish these items from available evidence; use N/A with a reason where an item genuinely does not apply:

- [ ] Target repository/service and local/cloud environment.
- [ ] Installed version, commit or equivalent configuration revision, if available; never invent one.
- [ ] Original symptom reproduced or located in direct logs/requests/stack traces.
- [ ] Relevant existing source/configuration/migrations and user edits inspected.
- [ ] A falsifiable hypothesis and the smallest justified change identified.

Read applicable project instructions. Preserve the current stack and unrelated edits. Do not create infrastructure, install packages or redeploy merely because a capability exists.

| Need | First evidence | Escalate when and where |
| --- | --- | --- |
| API/library behavior | Installed version and matching official docs | Exact version absent: official release/source; exact error issues for leads, verify against primary evidence. |
| Failed deployment | Correct provider's deployment record and build/runtime logs | Logs point to dependency/configuration: inspect that version/configuration and official guidance. |
| Database/query error | Current schema, migration history and relevant read-only queries | Error persists: scoped logs or a safe query plan; avoid executing unsafe writes during diagnosis. |
| UI/runtime regression | Relevant source plus permitted API/browser observation | Missing link in the failure: trace the actual data flow. |

Treat local sandbox, user machine and remote provider as distinct surfaces. Use available local source first; use a remote connector only for an authorized target it can actually access.

## 2. Checkpoint, change, validate

Before an isolated change, record the relevant pre-change content/configuration and your intended delta, including existing user changes. Keep checkpoints scoped and private. Define meaningful validation and a feasible, authorized restoration path. Production/data changes require their specific authorization; do not assume every mutation can be undone.

Follow: inspect → diagnose → checkpoint → change → validate. Test the original symptom and affected interfaces; run project-required checks. Do not invent tests for trivial reversible edits or mirror implementation assertions. A build result, deployment record and observed runtime behavior establish different claims.

## 3. Failure and scoped rollback

On failed validation:

1. Capture the failure evidence before restoration where feasible; prioritize an already-authorized urgent restoration when required for service health.
2. Determine whether the failure is caused by this attempt or is a pre-existing/unrelated check failure. Do not erase a valid change merely because an unrelated check failed.
3. Revert only the failed attempt's owned delta to the recorded pre-change state. Preserve user/concurrent edits and independent successful work. Avoid blanket reset/checkout commands. Never auto-reverse migrations, delete data or perform another destructive operation without its required authorization.
4. Verify restoration, record what the attempt ruled out, and return to diagnosis before another isolated attempt.

If restoration is uncertain or unsafe, stop further mutations on that target, report the exact limitation and continue unaffected work. A checkpoint may preserve the original bug; do not call it a proven stable state.

## 4. Finish

Use `verification-and-stop` §2–4. Report what changed, why, the checks actually run, original-symptom outcome and material unverified behavior. A request to fix a bug authorizes ordinary reversible implementation within scope; new production/deploy/destructive actions follow the existing applicable authorization boundary.
