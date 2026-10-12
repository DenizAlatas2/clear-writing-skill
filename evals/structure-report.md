# Targeted structure and terminology checks

## Change and scope

A final small revision on 12 October 2026 made two existing editorial goals more explicit:

- Untangle a difficult sentence or separate competing points while keeping conditions, reasons, and exceptions attached to the claims they qualify.
- Check repeated wording and sentence patterns for clarity and flow without forcing variety. Use the same term for the same thing.

The revision adds no sentence word limit, compulsory synonym changes, or prescribed rhythm. The existing permission to keep a real three-item list remains.

The [two synthetic cases](structure-cases.json) test an overloaded conditional instruction and repeated document-state terms. They contain no private source material.

## Method and observations

One native platform subagent explicitly read the revised `SKILL.md` and answered both prompts in one session. It did not read the examples or case invariants. A different native platform subagent checked the outputs against the original prompts, invariants, and skill. No model override was set. The exact inherited model identifier was not exposed in the task result.

The reviewer found no material failure in either output. The first answer split the long sentence while retaining the approval deadline, backup timing, additional archive-system read test, and independent status-report commitment. The second kept the already clear wording and the same names for the two document states. A literal check found no matches for the listed excluded wording or punctuation.

- [Raw answers](runs/2026-10-12-structure/answers.json)
- [Independent review](runs/2026-10-12-structure/review.json)
- [Tested file hashes, execution details, and lexical results](runs/2026-10-12-structure/snapshot.json)

## Limits

This is a two-case targeted check with no baseline comparison, no human panel, and no native agent installation or trigger test. It does not measure improvement, general writing quality, or future reliability.

The [earlier five-case adaptation check](adaptation-report.md) and the [historical 22-pair comparison](report.md) concern different snapshots. Neither was rerun for this final revision. Their original records remain unchanged. These checks are not combined into a seven-case or 29-case performance score.
