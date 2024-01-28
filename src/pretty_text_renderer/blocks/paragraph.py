from pretty_text_renderer.blocks.base import BaseBlock
from pretty_text_renderer.content.paragraph import Paragraph
from pretty_text_renderer.renderers.paragraph import ParagraphRenderer


class ParagraphBlock(BaseBlock[Paragraph, ParagraphRenderer]):
    _content_type = Paragraph
