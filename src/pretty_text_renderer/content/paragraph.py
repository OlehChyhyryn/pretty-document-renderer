import dataclasses

from pretty_text_renderer.content.base import BaseContent


@dataclasses.dataclass
class Paragraph(BaseContent):
    text: str
