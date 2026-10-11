# Clear writing

A compact Agent Skill for clear, natural German and English writing in Codex and GitHub Copilot. It helps with new answers and drafts as well as revisions, including customer communication and technical explanations.

The skill asks the writer to answer the actual question, choose a suitable register, and keep facts, uncertainty, responsibilities, conditions, and commitments intact. It removes empty framing and unnecessary jargon without lowering the technical level or manufacturing a personality.

It also applies an opinionated editorial policy: no abstract proof talk, em or en dashes, thought dashes, semicolons, or U+2022 bullets in editable prose. Normal word hyphens remain valid. Exact quotations, URLs, identifiers, and executable syntax stay intact, with any conflict explained. This policy is a style choice, not a claim about who wrote a text.

## Install

This candidate is awaiting review and has not been published. The GitHub clone commands below describe the intended repository after publication. You can use the local skill folder now.

The documented shared location for project skills is `.agents/skills`. The documented shared personal location is `~/.agents/skills`. Copy the whole `clear-writing` folder, including its references and license. These locations are supported by the current [Codex documentation](https://learn.chatgpt.com/docs/customization/overview#skills) and [GitHub Copilot documentation](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills).

### Project installation, Codex and Copilot

From the root of the project where you want to use the skill:

```sh
git clone https://github.com/DenizAlatas2/clear-writing-skill.git /tmp/clear-writing-source
mkdir -p .agents/skills
test ! -e .agents/skills/clear-writing && cp -R /tmp/clear-writing-source/skills/clear-writing .agents/skills/
```

The last command leaves an existing installation alone. Review or back up an existing copy before replacing it. Use a different empty clone destination if `/tmp/clear-writing-source` already exists. Restart your agent session if it does not discover the new skill.

Copilot also documents `.github/skills/clear-writing` for project installation. Use one copy in the location appropriate to your host, to avoid duplicate skill names.

### Personal installation, Codex and Copilot

After obtaining the repository, run this from its root:

```sh
mkdir -p "$HOME/.agents/skills"
test ! -e "$HOME/.agents/skills/clear-writing" && cp -R skills/clear-writing "$HOME/.agents/skills/"
```

These examples use a POSIX shell. On other systems, copy the same folder with your file manager or native shell.

The paths and copy behavior are checked against current documentation and an isolated local copy test. Discovery and invocation in a standalone Codex or Copilot host have not yet been tested. Host features and automatic selection can vary. This repository does not modify your configuration or install itself.

## Use

In Codex, explicitly request `$clear-writing`. Copilot selects relevant skills from their description. Ask it to use the `clear-writing` skill for the task. For hosts that support skill slash commands, select the discovered skill from the menu. Check the host's available commands instead of assuming identical syntax across products.

```text
$clear-writing Schreibe eine kurze Antwort in der Sie-Form aus diesen Fakten:
Der Versand ist verspätet. Wir melden uns bis Mittwoch um 16 Uhr.
Ein Liefertermin steht noch nicht fest.
```

```text
Use the clear-writing skill to revise this technical update.
Keep its quantities, conditions, responsibilities, and level of certainty.
```

The [skill entrypoint](skills/clear-writing/SKILL.md) contains the instructions. Its optional [DE/EN examples](skills/clear-writing/references/examples.md) show how to preserve meaning while changing the language. Every example is synthetic.

## Why another writing skill?

[blader/humanizer](https://github.com/blader/humanizer) is a useful starting point for removing recurring writing patterns. [andreaskonopka/humanizer](https://github.com/andreaskonopka/humanizer) already supports German and English, structure-aware editing, and factual preservation. [marmbiz/humanizer-de](https://github.com/marmbiz/humanizer-de) adds detailed German guidance and source and voice safeguards. There is substantial overlap.

This project offers a small, original bundle with explicit support for writing from a facts brief, preserving the degree of commitment, matching the reader relationship, and checking a stricter editorial policy. It uses a focused set of decisions and examples instead of a large pattern catalog. These are packaging and policy choices. No comparison has established that it outperforms those projects.

## Evaluation

The [evaluation protocol](evals/protocol.md) separates file validation from writing quality. The [synthetic cases](evals/cases.json) cover both languages, drafting and revision, customer complaints, refusals, technical detail, real three-item lists, quantified comparisons, uncertain deadlines, already good text, and protected original material.

An independent paired evaluation and its raw outputs will be recorded in `evals/runs`. Changed facts or commitments and violations of the editorial exclusions are hard failures. They cannot be offset by style ratings. Results are a small model-assessed sample, not a human panel, a detector score, or a promise of performance on your work.

## Sources and license

[Source notes](docs/sources.md) explain the public writing guidance, existing skills, research scope, and licensing decisions. The instructions and synthetic examples were written for this project. No third-party catalog, prompt, or example was copied into the skill.

Own project content is licensed under [MIT](LICENSE). The installable folder includes the same license. Referenced projects and publications retain their own terms. In particular, the German catalog in `marmbiz/humanizer-de` is subject to the separate terms in its NOTICE, so its repository must not be treated as wholly MIT.

## Grenzen

Der Skill verbessert die Formulierung aus dem vorhandenen Kontext. Fehlende Sachkenntnis, falsche Ausgangsdaten oder unklare Vereinbarungen löst er nicht von selbst. Klare Sprache darf fachliche Unterschiede und berechtigte Unsicherheit nicht beseitigen. Die Wort- und Satzzeichenregeln sind bewusst streng und passen nicht zu jedem Stilauftrag. Bei wörtlichen Zitaten oder ausführbarer Syntax kann ein sichtbarer Konflikt bleiben.

## Contribute

Suggest a narrow improvement with a synthetic example, the reader and task, the observed problem, and the meaning that must stay intact. Include counterexamples where an edit would make good writing worse. Do not submit private messages, customer records, employer material, or credentials.
