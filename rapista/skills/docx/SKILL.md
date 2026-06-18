# docx Skill

Build a `.docx` document from a YAML/JSON config file.

## Usage

```
pip install python-docx
python -m build_doc --config <config.yml>
```

## Config Structure

```yaml
output: "output/document.docx"
sections:
  - module: cover
    title: "My Document"
    subtitle: "Generated with python-docx"
  - module: toc
    title: "Table of Contents"
  - module: body
    title: "Introduction"
    content: "This is the body content."
  - module: headers_footers
    header_text: "Confidential"
    footer_text: "Page "
```

## Modules

| Module          | Purpose                        |
|-----------------|--------------------------------|
| `cover`         | Title page with styling        |
| `toc`           | Table of contents page         |
| `body`          | Main content with headings     |
| `headers_footers` | Header and footer for all pages |

## Module Components

Each module is composable. Add `sections` entries to combine them in order.

## Output

All generated files go under `output/`.
