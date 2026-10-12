# Targeted context and adaptation checks

## Scope

On 12 October 2026, the writing core received three small additions:

- Make action requests answerable from their supplied context, reference, requested contribution, and real deadline.
- Preserve courtesy, thanks, congratulations, and sympathy when they serve the purpose or relationship.
- Recheck facts, speaker, and destination when adapting text across audiences, channels, or event stages.

The [five new cases](adaptation-cases.json) and examples are synthetic. They contain no private source material.

## Execution and result

One native platform subagent explicitly read the revised `SKILL.md` and answered all five prompts in a single session. It did not read the example reference or the test invariants. A separate native platform subagent checked the resulting answers against the original prompts, invariants, and skill. No model override was set. The exact inherited model identifier was not exposed in the task result.

The reviewer found no material failure in these five outputs. A separate literal check found no matches for the listed excluded wording or punctuation. The action request kept its link, review scope, deadline, and reason. The congratulation retained its relationship content. The recap distinguished a planned agenda from unknown outcomes. The personal post omitted the internal note and kept the opinion personal. The invitation did not turn sample-template claims into event facts.

- [Raw answers](runs/2026-10-12-adaptation/answers.json)
- [Independent review](runs/2026-10-12-adaptation/review.json)
- [Tested file hashes, execution details, and lexical results](runs/2026-10-12-adaptation/snapshot.json)

## Limits

This was a targeted check with five synthetic prompts, one writer session, one model reviewer, and no baseline comparison. It does not measure an improvement over the previous skill, other skills, or unaided writing. It does not measure trigger reliability, native host discovery, human preferences, or performance on real correspondence.

The [historical 22-pair comparison](report.md) remains a record of its earlier tested snapshots. Its raw outputs, ratings, and confirmed meaning-loss finding are unchanged. It was not rerun against this revised writing core. The five new checks are not added to its tie count or presented as a new combined score.

Packaging, local links, basic frontmatter, metadata, copy/refusal behavior, and fixture parsing are mechanical checks. They do not grade writing quality or predict error-free future behavior.
