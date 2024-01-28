import abc

from pretty_text_renderer.content.paragraph import Paragraph
from pretty_text_renderer.renderers.base import BaseRenderer


class ParagraphRenderer(BaseRenderer[Paragraph], abc.ABC):
    pass


class TxtPlainTextRenderer(ParagraphRenderer):
    _content_type = Paragraph

    def _render(self, content: Paragraph) -> str:
        return content.text
