import filecmp
from tempfile import NamedTemporaryFile
import unittest

from pretty_text_renderer.config import BASE_DIR


class TxtRendererTestCase(unittest.TestCase):
    def test_paragraph_content_rendered_correctly(self) -> None:
        from pretty_text_renderer.blocks.paragraph import ParagraphBlock
        from pretty_text_renderer.content.paragraph import Paragraph
        from pretty_text_renderer.renderers.paragraph import TxtPlainTextRenderer

        content = Paragraph("Hello World!")
        block = ParagraphBlock(content, TxtPlainTextRenderer())
        rendered = block.render_as_str()
        self.assertEqual(rendered, "Hello World!")
        temp_file = NamedTemporaryFile(suffix=".txt")
        stream = block.render_as_bytes()
        with open(temp_file.name, "wb") as f:
            f.write(stream.read())
        filecmp.cmp(temp_file.name, str(BASE_DIR / "pretty_text_renderer/tests/resources/expected/paragraph.txt"))
