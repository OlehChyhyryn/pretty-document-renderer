from __future__ import annotations

import abc
from typing import TYPE_CHECKING, Generic

from typing_extensions import TypeVar

from pretty_text_renderer.common import WithContentTypeMixin
from pretty_text_renderer.content.base import TContent

if TYPE_CHECKING:
    from pretty_text_renderer.blocks.base import BaseBlock


class BaseFormatter(WithContentTypeMixin, Generic[TContent], abc.ABC):
    def format(self, block: BaseBlock) -> TContent:
        """Format block content according to formatter rules and return it in updated state."""
        content = block.get_content()
        self.validate_content_type(content)
        self._validate_content(content)
        return self._format(content)

    @abc.abstractmethod
    def _format(self, content: TContent) -> TContent:
        """
        Real implementation of the formatting logic.

        This method must be implemented in subclasses

        :param content: content to format
        :return: string with formatted content
        """

    def _validate_content(self, content: TContent) -> None:
        """
        Validated content data type to ensure it can be formatted.

        Default implementation is `do nothing` and should be overridden in subclasses if needed.

        :param content: content to validate
        """
        pass


TFormatter = TypeVar("TFormatter", bound=BaseFormatter)
