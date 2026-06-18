# Document Generation with AI + Skills

Build `.docx` documents using composable skill modules. Each module (cover, TOC, body, headers/footers) can be mixed and matched via a simple YAML/JSON config.

## Quick Start

```
pip install python-docx
python build_doc.py --config sample_config.yml
```

## Structure

- `build_doc.py` — CLI entry point
- `docx_builder/` — builder package with composable modules
- `skills/docx/SKILL.md` — skill instructions for AI agents
- `output/` — generated documents
