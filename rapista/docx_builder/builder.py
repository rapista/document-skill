from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

from .modules import cover, toc, body, headers_footers


MODULES = {
    "cover": cover,
    "toc": toc,
    "body": body,
    "headers_footers": headers_footers,
}


class DocumentBuilder:
    def __init__(self, config: dict):
        self.config = config
        self.document = Document()
        self.sections = config.get("sections", [])

    def build(self) -> str:
        for section in self.sections:
            module_name = section.get("module")
            mod = MODULES.get(module_name)
            if mod:
                mod(self.document, section)
        output_path = self.config.get("output", "output/document.docx")
        self.document.save(output_path)
        return output_path
