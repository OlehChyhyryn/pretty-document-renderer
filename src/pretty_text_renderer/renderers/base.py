from __future__ import annotations

import abc
from io import BytesIO
from typing import IO, Generic, TypeVar

from pretty_text_renderer.common import WithContentTypeMixin
from pretty_text_renderer.content.base import TContent


class BaseRenderer(WithContentTypeMixin, Generic[TContent], abc.ABC):
    def to_str(self, content: TContent) -> str:
        self.validate_content_type(content)
        self._validate_content(content)
        return self._render(content)

    def to_bytes(self, content: TContent) -> IO[bytes]:
        return BytesIO(self.to_str(content).encode())

    def _validate_content(self, content: TContent) -> None:
        """
        Validated content data type to ensure it can be rendered.

        Default implementation is `do nothing` and should be overridden in subclasses if needed.

        :param content: content to validate
        """
        pass

    @abc.abstractmethod
    def _render(self, content: TContent) -> str:
        """
        Real implementation of the rendering logic.
        Both `to_str` and `to_bytes` methods delegate to this method.

        :param content: Content to be rendered.
        :return: Rendered content as a string.
        """


TRenderer = TypeVar("TRenderer", bound=BaseRenderer)
