from __future__ import annotations

__all__ = [
    "BaseBlock",
]

import abc
from typing import IO, TYPE_CHECKING, Generic, Optional

from pretty_text_renderer.common import WithContentTypeMixin
from pretty_text_renderer.content.base import TContent
from pretty_text_renderer.exceptions import PteIncorrectContentType
from pretty_text_renderer.formatters.identity import IdentityFormatter
from pretty_text_renderer.renderers.base import TRenderer

if TYPE_CHECKING:
    from pretty_text_renderer.formatters.base import BaseFormatter


class BaseBlock(WithContentTypeMixin, Generic[TContent, TRenderer], abc.ABC):
    """
    Abstract block class all other blocks should inherit from.
    """

    def __init__(
        self,
        content: TContent,
        renderer: TRenderer,
        formatter: Optional[BaseFormatter] = None,
    ) -> None:
        if not self.is_expected_content_type(content):
            raise PteIncorrectContentType(self, content, self._get_content_type())
        self._content: TContent = content
        self._formatter: BaseFormatter[TContent] = formatter or IdentityFormatter[TContent]()
        self._renderer: TRenderer = renderer

    def get_content(self) -> TContent:
        """
        Return a copy of the block content.

        Working with the returned content will not affect the original data.
        """
        return self._content.copy()

    def format_content(self) -> TContent:
        """
        Apply the formatter to the block content and return an updated copy of the content.
        """
        return self._formatter.format(self)

    def render_as_str(self) -> str:
        """
        Render the block content as a str block.

        This string block is expected to be a valid fragment of the final document.
        """
        content = self.format_content()
        return self._renderer.to_str(content)

    def render_as_bytes(self) -> IO[bytes]:
        """
        Render the block content as an IO[bytes] stream.
        """
        content = self.format_content()
        return self._renderer.to_bytes(content)
