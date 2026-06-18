# Agent

## Project
Document generator that builds `.docx` files using composable skill modules. Users provide a YAML/JSON config describing the document structure; the system assembles a Word document from reusable building blocks (cover page, TOC, body sections, headers/footers).

## Architecture

```
rapista/
├── build_doc.py              # CLI entry point
├── docx_builder/
│   ├── __init__.py            # Exports build(config) -> str
│   ├── builder.py             # DocumentBuilder: iterates sections, dispatches to modules
│   └── modules.py             # Individual module functions (cover, toc, body, headers_footers)
├── skills/
│   └── docx/
│       └── SKILL.md           # Skill documentation
├── output/                    # Generated .docx files land here
├── sample_config.yml          # Example config
└── AGENTS.md                  # This file
```

**Flow**: `build_doc.py --config <file>` → loads YAML/JSON → calls `docx_builder.build(config)` → `DocumentBuilder` loops over `sections` → dispatches each to its module function → saves `.docx` to `output/`.

## Available Skills

### docx
Build a complete `.docx` document. Uses `python-docx` to assemble a Word document from composable modules. Accepts a JSON/YAML config describing the document structure, styling, and content sources.

**Modules** (defined in `docx_builder/modules.py`):

| Module            | Function               | Config Keys                            |
|-------------------|------------------------|----------------------------------------|
| `cover`           | `cover()`              | `title`, `subtitle`                    |
| `toc`             | `toc()`                | `title` (default: "Table of Contents") |
| `body`            | `body()`               | `title`, `content`                     |
| `headers_footers` | `headers_footers()`    | `header_text`, `footer_text`           |

## Commands

### Setup
```powershell
pip install python-docx pyyaml
```

### Build a document
```powershell
python build_doc.py --config sample_config.yml
```

### Add a new module
1. Define a function in `docx_builder/modules.py` that accepts `(document: Document, section: dict)`.
2. Import and register it in `docx_builder/builder.py` by adding to the `MODULES` dict.

## Agent Instructions
- When working on document generation, load the `docx` skill from `skills/docx/SKILL.md`.
- Follow the skill's instructions for creating and combining document components.
- When adding new module types, define the function in `modules.py` and register it in `builder.py`.
- All generated files go under `output/`.
- For configs, use `sample_config.yml` as the template.
- Use `build_doc.py` with `--config` to build; the helper `docx_builder.build(config)` is also importable for programmatic use.
