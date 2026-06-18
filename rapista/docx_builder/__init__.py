from .builder import DocumentBuilder


def build(config: dict) -> str:
    builder = DocumentBuilder(config)
    return builder.build()
