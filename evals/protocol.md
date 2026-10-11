# Behavioral evaluation

Format checks answer whether the files are shaped correctly. They do not measure writing quality.

## Design

Use the synthetic cases in [cases.json](cases.json). There are German and English cases for drafting and revision, customer messages, technical explanations, refusals, short answers, and an already good text. The invariant lists are for assessors, not writers.

1. Freeze a candidate commit or record file hashes before generating outputs.
2. Start two independent writer sessions with the same model and runtime instructions. Give both the same prompts, with no expected answers or assessor criteria.
3. Give one writer the skill and its optional examples. Give the baseline writer no new skill instructions. Prevent access to the other writer's outputs. Use a fresh context for each case when feasible. If cases share a session, report that limitation.
4. Save the complete raw outputs and execution metadata. Never repair an output before scoring it.
5. Randomize the order of the two candidates for each case. Give an independent assessor the case, invariants, and candidates without the condition labels or the skill.
6. Score each candidate, cite concrete output details, and record any hard failures. Disclose the mapping after the assessment. Review it for errors without rewriting unfavorable results.

## Scores

Rate each dimension from 0 to 4. Use 4 for a strong fit, 3 for a minor issue, 2 for a material weakness, 1 for a serious weakness, and 0 for a failure to address the task. Explain differences rather than calculating a universal writing score.

| Dimension | What to assess |
| --- | --- |
| Naturalness | Idiomatic language without padding, a manufactured persona, or forced casualness |
| Precision | Clear meaning, scope, references, and useful technical detail |
| Preservation | Material facts, uncertainty, relationships, responsibility, conditions, and commitments |
| Length | Enough information for this task without needless expansion or loss |
| Register | Appropriate language, tone, formality, and Du or Sie relationship |

Any changed or invented material fact, condition, or commitment is a hard failure. Any excluded wording or punctuation in editable prose is also a hard failure. Neither can be offset by the scores. Do not mark intact protected quotes, code, or URLs as prohibited prose. Assess whether a conflict was disclosed when needed.

The baseline receives the ordinary task request, not the skill's special exclusions. That comparison tests the whole instruction bundle. Report that a punctuation advantage partly reflects an extra explicit requirement, and do not equate it with a general improvement in writing.

## Reporting and limits

Publish raw outputs, condition mapping, per-case judgments, hard failures, date, model identity if available, session design, and skill hash or commit. State whether generation was performed by platform agents, Codex CLI, or Copilot. A model assessor is not a human panel. A small synthetic suite does not establish performance on real customer work or across models. Do not advertise a detector score, a percentage of “human writing,” or superiority over other projects without a direct comparison.

If the skill changes after testing, identify the tested snapshot and separate untested changes. Follow-up tests should target a demonstrated failure and remain visible alongside the earlier result.
