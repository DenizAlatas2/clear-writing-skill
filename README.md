# Clear writing

A compact experimental Agent Skill for clear, natural German and English writing across AI agents. It helps with new answers and drafts as well as revisions, including customer communication and technical explanations.

The skill asks the writer to answer the actual question, choose a suitable register, and keep facts, uncertainty, responsibilities, conditions, and commitments intact. It removes empty framing and unnecessary jargon without lowering the technical level or manufacturing a personality.

It also applies an opinionated editorial policy: no abstract proof talk, em or en dashes, thought dashes, semicolons, or U+2022 bullets in editable prose. Normal word hyphens remain valid. Exact quotations, URLs, identifiers, and executable syntax stay intact, with any conflict explained. This policy is a style choice, not a claim about who wrote a text.

## Automatic use

The skill is agent-neutral. It uses the open [Agent Skills format](https://agentskills.io/specification) and has no runtime dependencies. Codex, Copilot, and Claude Code are documented integration examples, not the limit of its scope.

Its description covers ordinary German and English answers, messages, documents, explanations, and revisions. You do not need to ask for a rewrite or name the skill every time. A skill-capable host can select it from the task. The optional [Codex metadata](skills/clear-writing/agents/openai.yaml) explicitly allows implicit invocation.

For a writing default across relevant tasks, install the skill **and add the small persistent prose instruction** in the [installation guide](docs/installation.md#make-clear-writing-a-default). This places the default in the host's normal instructions instead of relying only on skill selection. It respects explicit style requests, exact quotations, code, and structured output requirements. It does not grant tool permissions.

Neither a skill description nor a persistent instruction guarantees perfect selection or compliance in every host. Verify discovery and an unnamed writing request in your actual agent. Supported paths and integration behavior are listed in the guide.

## Install with your agent

Copy this request into the agent where you want to use the skill:

```text
Install clear-writing from https://github.com/DenizAlatas2/clear-writing-skill
for this agent, preferably at user scope. Read README.md, docs/installation.md,
and the skill files first. Identify this host and its supported installation
and persistent-instruction locations. Install the complete skill folder and
merge the guide's default prose instruction into the appropriate existing
instructions without overwriting unrelated content. Keep automatic selection
enabled. Preserve explicit style requests, code, quotes, and required formats.
Do not run remote installers, change permissions, or overwrite a conflicting
installation. Ask if the scope or a conflict needs my decision. Verify discovery
and a writing request that does not name the skill. Report the installed paths,
source commit, checks performed, and any host limitations.
```

The guide also has a [German installation request](docs/installation.md#deutscher-installationsauftrag), documented host paths, safe manual copying, and update/removal instructions. The repository does not install itself. A folder in a repository is not automatically available in every chat app, account, or device.

## Use

After setup, just ask for the writing you need:

```text
Schreibe eine kurze Antwort in der Sie-Form aus diesen Fakten:
Der Versand ist verspätet. Wir melden uns bis Mittwoch um 16 Uhr.
Ein Liefertermin steht noch nicht fest.
```

```text
Explain this technical update to a colleague.
Keep its quantities, conditions, responsibilities, and level of certainty.
```

Explicit invocation remains useful for troubleshooting or a one-off task. Codex supports `$clear-writing`; Claude Code supports `/clear-writing`. Other hosts differ, so check the discovered skill list or supported commands.

The [skill entrypoint](skills/clear-writing/SKILL.md) contains the instructions. Its optional [DE/EN examples](skills/clear-writing/references/examples.md) show how to preserve meaning while changing the language. Every example is synthetic.

## Why another writing skill?

[blader/humanizer](https://github.com/blader/humanizer) is a useful starting point for removing recurring writing patterns. [andreaskonopka/humanizer](https://github.com/andreaskonopka/humanizer) already supports German and English, structure-aware editing, and factual preservation. [marmbiz/humanizer-de](https://github.com/marmbiz/humanizer-de) adds detailed German guidance and source and voice safeguards. There is substantial overlap.

This project offers a small, original bundle with explicit support for writing from a facts brief, preserving the degree of commitment, matching the reader relationship, and checking a stricter editorial policy. It uses a focused set of decisions and examples instead of a large pattern catalog. These are packaging and policy choices. No comparison has established that it outperforms those projects.

## Evaluation

The [evaluation protocol](evals/protocol.md) separates file validation from writing quality. The [synthetic cases](evals/cases.json) cover both languages, drafting and revision, customer complaints, refusals, technical detail, real three-item lists, quantified comparisons, uncertain deadlines, already good text, and protected original material.

The following comparisons describe recorded 11 October snapshots, before the 12 October request-context and adaptation additions.

The [evaluation report](evals/report.md) links complete raw outputs, blinded judgments, condition mappings, and tested snapshots. The first 20-case comparison found no general advantage over the strong baseline and exposed a preservation failure. A complete rerun of the final instructions produced ties in all 20 original cases and two separate boundary cases. The model assessors recorded no hard failures. A subsequent independent content review confirmed that both final answers in one case lost a meaningful relation from the source. The other 21 pairs contained no further clear material error in that review. The original answers and scores remain unchanged. The 22 model ties are a small, weakly discriminating assessment, not an error-free result or a general performance advantage. Targeted follow-ups and corrections are recorded separately. Changed facts or commitments and violations of the editorial exclusions are hard failures. They cannot be offset by style ratings. Results are a small model-assessed sample, not a human panel, a detector score, or a promise of performance on your work.

On 12 October, a separate integration update broadened discovery and installation guidance. The report's three-file packaging checks describe the earlier snapshot. The current installable folder has four files, including optional Codex metadata. Later, three small writing additions covered self-contained action requests, purposeful courtesy, and factual boundaries when adapting text for another audience or channel. A [separate targeted check](evals/adaptation-report.md) found no material failures in five new synthetic outputs. It used one model writer and a separate model reviewer, with no baseline. The historical 22-pair comparison was not rerun and must not be treated as an evaluation of the revised writing core.

Packaging, local links, basic skill frontmatter, optional metadata, and isolated copy/refusal checks passed for the integration update. A native Codex CLI smoke test could not initialize its app-server client because its filesystem was read-only, so no writing request ran. Native Codex, Copilot, and Claude invocation remains unverified. The GitHub CLI specification dry-run was not repeated because the available CLI lacks the skill command.

For local packaging, link, fixture, and obvious disclosure checks, run `python3 scripts/check.py`. For specification validation with GitHub CLI 2.90 or later, run `gh skill publish --dry-run .`. These commands do not grade writing. No publication command is required to use the folder.

## Sources and license

[Source notes](docs/sources.md) explain the public writing guidance, existing skills, research scope, and licensing decisions. The instructions and synthetic examples were written for this project. No third-party catalog, prompt, or example was copied into the skill.

Own project content is licensed under [MIT](LICENSE). The installable folder includes the same license. Referenced projects and publications retain their own terms. In particular, the German catalog in `marmbiz/humanizer-de` is subject to the separate terms in its NOTICE, so its repository must not be treated as wholly MIT.

## Grenzen

Der Skill verbessert die Formulierung aus dem vorhandenen Kontext. Fehlende Sachkenntnis, falsche Ausgangsdaten oder unklare Vereinbarungen löst er nicht von selbst. Klare Sprache darf fachliche Unterschiede und berechtigte Unsicherheit nicht beseitigen. Die Wort- und Satzzeichenregeln sind bewusst streng und passen nicht zu jedem Stilauftrag. Bei wörtlichen Zitaten oder ausführbarer Syntax kann ein sichtbarer Konflikt bleiben.

## Contribute

Suggest a narrow improvement with a synthetic example, the reader and task, the observed problem, and the meaning that must stay intact. Include counterexamples where an edit would make good writing worse. Do not submit private messages, customer records, employer material, or credentials.
