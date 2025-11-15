# Project Documentation – One AI Agent, One Command

This repo contains the core assets for turning an AI model into an **autonomous documentation agent**: something that scans your entire codebase, understands its structure, and generates a complete `specs/` folder with architecture docs, per-file explanations, data models, diagrams, and more – all from **one master prompt**.

It’s the companion repo for the article:

> **“Stop Writing Docs by Hand: One Agent AI Command to Document Your Entire Codebase”**  
> https://medium.com/@ronivaldo/stop-writing-docs-by-hand-one-agent-ai-command-to-document-your-entire-codebase-c28c9cc720cd

If you haven’t read it yet, start there for the full story, motivation, and concepts behind this setup.

---

## What This Repo Contains

- **`prompt.md`**  
  The heart of this repo. This is the **master prompt** that turns an LLM into an autonomous documentation agent.  
  It instructs the agent to:
  - scan your whole project  
  - understand the architecture  
  - document each file  
  - map relationships and data models  
  - generate Mermaid diagrams  
  - assemble a complete documentation package in a `specs/` folder  
  - track its own progress in a `runtime.md` file  

- (Optionally) Example structure / notes that show how the `specs/` folder is expected to look after the agent runs.

The repo is **agent-agnostic**: you can use it with any AI environment that lets an agent read your filesystem and run long, multi-step tasks (e.g., “AI dev tools”, IDE agents, or your own orchestration).

---

## How It Works (High Level)

1. You point your AI agent at your project.
2. You give it the contents of **`prompt.md`** as its system / master instruction.
3. The agent:
   - walks the project tree  
   - builds a to-do list of files to process  
   - creates and maintains `specs/runtime.md` as a progress log  
   - writes architectural docs to `specs/architecture_overview.md`  
   - writes file-by-file documentation to `specs/full_documentation.md`  
   - generates indexes (`catalog.txt`, `relationships.txt`, `data_models.txt`)  
   - generates Mermaid diagrams under `specs/diagrams/`  
   - assembles a `developer_guide.md` and `api_reference.md`  
4. It keeps going until the checklist is complete and marks the run as 100% done inside `runtime.md`.

All explanatory text is generated in **English**, even if your source files or identifiers are in another language. Filenames, function names, classes, etc. are preserved as in your original code.

---

## Using `prompt.md` in Your Own Project

> This repo doesn’t ship a specific runtime or CLI – it gives you the **spec** and the **prompt** so you can plug it into the AI tooling of your choice.

A typical flow looks like this:

1. **Clone or copy this repo (or just `prompt.md`):**
   ```bash
   git clone https://github.com/ronivaldo/medium.git
   cd medium/project_documentation
   ```

2. **Open `prompt.md`.**
   This is the full master specification for the agent. Read through it so you understand:

   * what the agent will do
   * which files it will create under `specs/`
   * how it tracks state and avoids duplicate work

3. **Create or select an AI agent environment** that:

   * can read your project’s files
   * can write new files (or patches) into the repo
   * can run long enough to process the whole codebase

4. **Paste the contents of `prompt.md`** as the agent’s main instruction / system prompt.

5. **Run the agent from the root of your target project.**
   The agent will:

   * discover all files
   * start generating the `specs/` folder
   * log progress in `specs/runtime.md`

6. **Let it run.**
   Some tools may occasionally ask you to confirm steps (e.g., “Should I continue with the DAOs?”). Just say “yes, please do it” if you want it to keep going.

7. **Inspect the generated `specs/` folder.**
   You should see:

   * `runtime.md` – progress log and checklist
   * `architecture_overview.md` – high-level architecture
   * `full_documentation.md` – file-by-file documentation
   * `developer_guide.md` – how to run, debug, and extend
   * `api_reference.md` – API docs (if you have endpoints)
   * `catalog.txt`, `relationships.txt`, `data_models.txt`
   * `diagrams/` with Mermaid diagrams (`architecture.mmd`, `dataflow.mmd`, etc.)

---

## When to Use This

This setup is especially useful when:

* you’re onboarding people to a medium or large codebase
* you’ve inherited a project with little to no documentation
* you want a consistent `specs/` folder that can act as a single source of truth
* you hate writing documentation by hand but still want solid docs

It won’t magically fix bad architecture, but it will make your project **far easier to understand**, for you and everyone who touches it later.

---

## Learn More

For the full narrative, examples, and rationale behind this approach, check out the article:

👉 **Stop Writing Docs by Hand: One Agent AI Command to Document Your Entire Codebase**
[https://medium.com/@ronivaldo/stop-writing-docs-by-hand-one-agent-ai-command-to-document-your-entire-codebase-c28c9cc720cd](https://medium.com/@ronivaldo/stop-writing-docs-by-hand-one-agent-ai-command-to-document-your-entire-codebase-c28c9cc720cd)

If you experiment with this setup in your own projects, feel free to adapt `prompt.md` to your stack, your conventions, and your favorite AI tooling.


