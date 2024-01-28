from __future__ import annotations

from pretty_text_renderer.content.container import Container
from pretty_text_renderer.renderers.base import BaseRenderer


class ContainerRenderer(BaseRenderer):
    _content_type = Container

    def _render(self, content: Container) -> str:
        result = []
        for block in content.children.values():
            result.append(block.render_as_str())
        return "\n".join(result)
