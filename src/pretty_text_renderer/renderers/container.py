from __future__ import annotations

import abc

from pretty_text_renderer.content.container import Container
from pretty_text_renderer.renderers.base import BaseRenderer


class BaseContainerRenderer(BaseRenderer[Container], abc.ABC):
    """
    Base container renderer class.
    """

    _content_type = Container


class ContainerRenderer(BaseRenderer):
    """
    Simplest container renderer that just renders all children in order.

    If you want to specify renderer for format with specific document indentation and general formatting, for example,
    for HTML, you should create your own renderer as child of `BaseContainerRenderer` and override `_render` method.
    """

    def _render(self, content: Container) -> str:
        result = []
        for block in content.children.values():
            result.append(block.render_as_str())
        return "\n".join(result)
