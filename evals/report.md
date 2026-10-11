# Evaluation report

The initial paired run does not show a general improvement over the baseline. It exposed one meaning loss in the skill condition. A fresh four-case follow-up checked a correction and exposed a remaining abstract proof formulation. The original failures remain visible in the raw records.

The baseline already inherited the platform's writing guidance. Both conditions used ordinary task prompts, while one additionally read the skill. This is a strong baseline, not an unprompted model. No other public writing skill was tested, so these results do not establish superiority over existing projects.

## Initial comparison

Tested candidate: `6f8ca46ed2f27356ee9b3bdc40ce3b74319b89d3`.

Twenty synthetic DE/EN tasks produced 40 unedited answers. Two independent model assessors each rated 10 paired cases with randomized A/B order and no condition labels. They assessed naturalness, precision, preservation, length, and register. Changed facts or commitments and excluded prose forms were separate hard failures.

| Recorded preference | Case count |
| --- | --- |
| Baseline | 4 |
| Skill | 3 |
| Tie | 13 |

There was one hard meaning failure in the skill condition, in `de-protected-original`. The revised introduction retained the originals and disclosed the punctuation conflict, but dropped the source's stated connection between the following material and the findings. The correction adds an explicit instruction to preserve meaningful relations, with disclosure when the available details cannot support a suitable rephrasing.

The skill condition also repeated the optional Friday rollout unnecessarily in `de-technical-revision` and made the testing limit less specific in `en-punctuation-revision`. The baseline gave a more concrete requested example in the longer idempotency explanation. Those observations do not justify banning repetition or hypothetical examples in general.

Both writers retained the quantifier above 30%, conditional deadlines, the genuine three-item lists, the already good texts, and the diagnostic release details in this sample. Both avoided the exact excluded lexical forms and punctuation outside protected originals. That lexical check does not detect every abstract synonym or establish overall writing quality.

Raw records: [baseline](runs/2026-10-11-initial/baseline.json), [skill](runs/2026-10-11-initial/skill.json), [judgments 1](runs/2026-10-11-initial/scores-1.json), [judgments 2](runs/2026-10-11-initial/scores-2.json), [mapping](runs/2026-10-11-initial/mapping.json), [hashes](runs/2026-10-11-initial/snapshot.json), [lexical check](runs/2026-10-11-initial/lexical-check.json), [execution and limits](runs/2026-10-11-initial/metadata.json).

## Stated relations and uncertainty

Tested candidate: `27ed5a3820f9cf486a9133e050e97dd5d77e1a69`.

Two replayed cases and two new DE/EN relation cases produced eight unedited answers in fresh writer sessions. One fresh blinded assessor rated them. The original relation loss was not repeated. The English relation case still used an abstract proof-status synonym in both conditions. The German baseline did likewise.

Recorded preferences were two for the skill, one for the baseline, and one tie. The skill had one hard editorial failure. The baseline had two hard editorial failures and one meaning failure under the assessor's interpretation of a significance claim. The assessor treated decisive importance as a substantive stance, rather than disposable emphasis. This interpretive difference is disclosed in the raw judgment and limits comparisons between runs.

The next correction requires the writer to state the concrete open question or work limit instead of swapping one abstract proof verdict for another. The previously exposed cases are development checks for that correction, not fresh holdouts.

Raw records: [cases](runs/2026-10-11-relations/cases.json), [baseline](runs/2026-10-11-relations/baseline.json), [skill](runs/2026-10-11-relations/skill.json), [judgments](runs/2026-10-11-relations/scores.json), [mapping](runs/2026-10-11-relations/mapping.json), [hashes](runs/2026-10-11-relations/snapshot.json), [execution and limits](runs/2026-10-11-relations/metadata.json).

## Concrete-uncertainty development check

Tested candidate: `9094764e0d03cf32d27aed3ce2f899d089d723a8`.

A fresh skill-writer session answered the two previously exposed DE/EN relation cases. The unchanged baseline answers from the prior follow-up were reused for comparison. A fresh blinded assessor preferred the skill in both pairs. No meaning or editorial hard failure was identified in the new skill answers. The old baseline answers retained their abstract proof verdicts.

This confirms the correction on these two development cases. It is not a fresh holdout result or a whole-suite pass. The runtime skill hash is recorded so readers can distinguish these instructions from the earlier tested versions.

Raw records: [cases](runs/2026-10-11-uncertainty/cases.json), [reused baseline](runs/2026-10-11-uncertainty/baseline.json), [new skill answers](runs/2026-10-11-uncertainty/skill.json), [judgments](runs/2026-10-11-uncertainty/scores.json), [mapping](runs/2026-10-11-uncertainty/mapping.json), [hashes](runs/2026-10-11-uncertainty/snapshot.json), [execution and limits](runs/2026-10-11-uncertainty/metadata.json).

## Limits and host checks

Writers and assessors ran as platform agents in Codex. No model override was set, and the exact inherited model identifier was not exposed by the tool. Each writer session contained its batch of cases, so there was no context reset between individual cases. Each pair had one assessor, with no interjudge reliability measurement. There was no human panel, cross-model study, live customer material, or comparison with existing public skills.

The final skill must be assessed by its recorded snapshot. The complete 20-case run belongs to the earlier candidate. Later targeted checks do not mean that all 20 cases were rerun against the final instructions.

`gh skill publish --dry-run .` passed using GitHub CLI 2.92.0. Full-folder copying into isolated project and simulated personal `.agents/skills` layouts preserved all three runtime files and refused an existing target. The standalone Copilot CLI could not start under the cache write restriction. Native Codex and Copilot discovery and invocation are therefore untested. No login, configuration, reconnection, paid API runner, or hosted CI was added.

The local checker passed its packaging, local-link, fixture, and obvious disclosure checks. It does not provide a complete secret scan or a guarantee that the writing instructions will be followed.
