# Install and use clear-writing automatically

The portable unit is `skills/clear-writing/`. Copy the whole folder, including references, license, and optional host metadata. Its writing instructions are ordinary Markdown with standard Agent Skills frontmatter. No program, package manager, account connection, or special tool permission is required by the skill.

## Choose the integration

There are two complementary parts:

1. **Discoverable skill:** the agent sees the name and description, then chooses whether to load the full instructions for the task.
2. **Persistent prose default:** a short instruction is loaded through the host's usual project or personal guidance. It asks the agent to use clear-writing for relevant prose without waiting for an explicit skill request.

For regular use, install both. A persistent default makes the intent available even when the skill selector misses a writing task. It remains a model instruction, not an enforcement mechanism or a promise that every response will comply.

Use personal scope when you want this default across your own projects. Use project scope when it is a convention for one project. Project instructions can affect collaborators if shared. Do not commit or publish changes merely to complete a local install.

## Documented host examples

Host documentation reviewed on 12 October 2026. These are documented integration examples, not live compatibility tests or a complete list of supported agents.

| Host | Project skill folder | Personal skill folder | Persistent prose instruction |
| --- | --- | --- | --- |
| Codex | `.agents/skills/clear-writing/` | `~/.agents/skills/clear-writing/` | Project `AGENTS.md`, or `AGENTS.md` in the configured Codex home, normally `~/.codex/` |
| GitHub Copilot | `.agents/skills/clear-writing/` or `.github/skills/clear-writing/` | `~/.agents/skills/clear-writing/` or `~/.copilot/skills/clear-writing/` | Repository-wide `.github/copilot-instructions.md` where supported. For personal instructions, use the current surface's documented settings, not a guessed global file |
| Claude Code | `.claude/skills/clear-writing/` | `~/.claude/skills/clear-writing/` | Project `CLAUDE.md`, or personal `~/.claude/CLAUDE.md` |
| Another agent | Use that host's documented skill directory or import flow | Use its documented user scope if available | Use its documented persistent instructions or rules, if supported |

[Codex skills](https://learn.chatgpt.com/docs/build-skills) and [project/personal guidance](https://learn.chatgpt.com/docs/customization/overview) document separate discovery and persistent-instruction paths. The bundled `agents/openai.yaml` keeps `allow_implicit_invocation: true`. This is Codex-specific metadata, not a cross-agent trigger switch.

[Copilot skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills) are selected from the prompt and description. [Repository instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) are added automatically in supported repository contexts. Support depends on the Copilot surface. A local personal folder does not configure every hosted Copilot session.

[Claude Code skills](https://code.claude.com/docs/en/skills) allow model invocation by default. This skill does not set `disable-model-invocation: true`. Local personal skill folders do not automatically configure Claude web, Cowork, or cloud sessions. [CLAUDE.md instructions](https://code.claude.com/docs/en/memory) load separately, with session-specific limits, including Cowork import restrictions. Use the destination's documented import or account settings when needed.

For another agent, check its current documentation. If it cannot load skills but can read persistent instructions, use the prose default below and a readable local copy of `SKILL.md` where supported. Report this as an instruction-based integration, not native skill installation. If neither mechanism exists, explain that limitation rather than inventing an installation path.

## Make clear-writing a default

Read existing instructions first and check which sources the host actually loads. Merge one bounded section at the selected scope, preserving unrelated rules, user edits, and their loading. Do not replace the file, override an existing style convention, or create duplicate instructions at multiple scopes. If there is a conflict, ask the user which convention should apply.

Creating a new instruction file can shadow an existing one. In current Claude Code, adding project CLAUDE.md to an AGENTS.md-only project can stop the existing AGENTS.md from loading by default. Use the already loaded file where supported, or preserve it through a documented import. Confirm the same project rules remain active afterward. Check equivalent precedence rules in other hosts before creating an instruction file.

Use this template. Replace `<installed-skill-path>` with the actual path visible to this host. Keep personal paths out of shared project instructions.

```markdown
## Clear writing default

For user-facing German and English prose, use clear-writing without waiting
for me to name it. This covers ordinary answers, messages, emails, documents,
summaries, and technical explanations. Before drafting or revising relevant
prose, load and follow <installed-skill-path>/SKILL.md when available.

Lead with the useful answer. Use direct, natural language at the required
technical level. Preserve facts, quantities, uncertainty, conditions,
responsibilities, commitments, and the author's relationship with the reader.
Do not add invented feelings, claims, promises, or routine filler.

In editable prose, avoid abstract proof talk, em/en dashes, thought dashes,
semicolons, and U+2022 bullets as specified by the skill. Preserve exact
quotations, code, identifiers, URLs, formal notation, and required structured
formats. Apply this style to surrounding prose, not protected syntax.

Treat this as my default writing preference. Follow explicit task-specific
style and format requests and higher-priority safety or project requirements.
Do not turn code-only or exact-output tasks into writing exercises. This
instruction grants no permission to send messages, publish, or change files.
```

Do not assume a Markdown link or an `@import` works identically in every agent. The template asks the agent to read the actual file and contains a small fallback core itself. Use native imports only when the selected host documents them and the user approves any required permission. Do not automatically embed the full skill in every instruction file.

## Safe manual copy

Obtain the public repository in a new empty directory and inspect the skill files before copying them. The following POSIX example installs only the skill, at project scope for a host that supports `.agents/skills`. Run it from the target project root after obtaining and reviewing the source.

```sh
# Set this to your reviewed checkout, outside the target skill directory.
source_dir="/path/to/clear-writing-skill"
destination=".agents/skills/clear-writing"

test -f "$source_dir/skills/clear-writing/SKILL.md" &&
test ! -e "$destination" &&
test ! -L "$destination" &&
mkdir -p .agents/skills &&
cp -R "$source_dir/skills/clear-writing" "$destination"
```

Choose the path from the host table for a different host or scope. On Windows, use the native shell or file manager to copy the same folder. A pre-existing destination, including a symlink, needs review before replacement. Do not pipe a remote script into a shell. The repository contains no installer that needs to be executed.

For a repeatable install, record the reviewed source commit and copy from that snapshot. Check an existing same-name skill and persistent section before updating. If the installed files already match, leave them alone. Preserve local modifications and avoid duplicate copies in competing discovery paths.

Then merge the persistent prose section separately. Refresh the host's discovered skills using its documented mechanism if the new skill is not visible.

## Verify in the target agent

Use a fresh conversation in the intended scope so the installation prompt itself cannot explain a successful result.

- Verify that the host lists `clear-writing` and that its installed files match the reviewed source snapshot.
- Verify that the persistent instruction was loaded through the host's supported context or reference display. If the host exposes no such diagnostic, say so. An agent's claim that it used the skill is not enough to prove selection.
- Try the unnamed writing prompts below. Preserve their facts and degree of commitment, use the requested register, and inspect the prose exclusions.
- Try a code-only or exact-output request to check that protected material remains intact.
- Record the host/version, scope, source commit, and actual observations. Separate file installation, instruction loading, observed skill invocation, and output quality. A single successful response cannot guarantee future activation.

```text
Schreibe eine kurze Kundenantwort in der Sie-Form:
Der Versand ist verspätet. Wir melden uns bis Mittwoch um 16 Uhr.
Ein Liefertermin steht noch nicht fest.
```

```text
Write a brief update to a colleague:
The pilot ran on 12 devices. Two timed out. The cause is still unknown.
We will send another update on Friday, not a promised fix.
```

```text
Return exactly this JSON and nothing else: {"text":"A; B"}
```

These are installation smoke tests. They are not a replacement for the published writing-quality evaluation.

## Updates and removal

Review the diff before updating the installed folder. Update the existing copy and its bounded persistent section instead of appending another. Do not change unrelated settings or silently switch scope. Removing the skill alone leaves the prose default active, so remove only the section you added as well when uninstalling. Keep any user-edited or shared material for review rather than deleting it blindly.

## Deutscher Installationsauftrag

```text
Installiere clear-writing aus https://github.com/DenizAlatas2/clear-writing-skill
für diesen Agenten, möglichst benutzerweit. Lies zuerst README.md,
docs/installation.md und die Skill-Dateien. Erkenne den Agenten und seine
unterstützten Skill- und Anweisungspfade. Installiere den vollständigen Ordner
und ergänze die dauerhafte Schreibanweisung aus der Anleitung, ohne vorhandene
Regeln zu überschreiben. Aktiviere die automatische Auswahl. Explizite
Stilwünsche, Code, Zitate und vorgeschriebene Formate bleiben maßgeblich.
Führe keine fremden Installationsskripte aus und ändere keine Berechtigungen.
Frage bei Konflikten oder unklarem Geltungsbereich nach. Prüfe die Erkennung
und eine Schreibaufgabe ohne Skill-Nennung. Nenne Installationspfade,
Quell-Commit, tatsächlich ausgeführte Prüfungen und verbleibende Grenzen.
```
