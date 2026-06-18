import argparse
import json
import sys

try:
    import yaml
except ImportError:
    yaml = None

from docx_builder import build


def load_config(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        if path.endswith((".yaml", ".yml")):
            if yaml is None:
                print("PyYAML is required for YAML configs. Install with: pip install pyyaml")
                sys.exit(1)
            return yaml.safe_load(f)
        else:
            return json.load(f)


def main():
    parser = argparse.ArgumentParser(description="Build a .docx document from a config file.")
    parser.add_argument("--config", required=True, help="Path to the config file (JSON or YAML)")
    args = parser.parse_args()

    config = load_config(args.config)
    output_path = build(config)
    print(f"Document generated: {output_path}")


if __name__ == "__main__":
    main()
