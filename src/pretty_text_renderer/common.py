from __future__ import annotations

import abc
from typing import TYPE_CHECKING, Any, Generic, Optional, Type, Union

from pretty_text_renderer.content.base import TContent
from pretty_text_renderer.exceptions import PteContentTypeMustBeProvided, PteIncorrectContentType

if TYPE_CHECKING:
    from typing_extensions import TypeGuard


class WithContentTypeMixin(Generic[TContent], abc.ABC):
    _content_type: Optional[Type[TContent]] = None
    """
    Content type this class is expected to receive.
    """

    def is_expected_content_type(self, content: Union[TContent, Any]) -> TypeGuard[TContent]:
        """
        Check and TypeGuard that the content is of the expected type.

        :param content: content to check
        :return: True if content is of the expected type, False otherwise
        """
        return isinstance(content, self._get_content_type())

    def validate_content_type(self, content: TContent) -> None:
        """
        Validate that expected block content type is the same as a content type expected by the formatter.

        :param content: a content object to validate

        :raises PteIncorrectContentType: if a content type is not the same as expected
        """
        if not self.is_expected_content_type(content):
            raise PteIncorrectContentType(self, content, self._get_content_type())

    def _get_content_type(self) -> Type[TContent]:
        """
        Get the content type this class is expected to receive.

        :return: the value of `_content_type` class variable if it is set, otherwise expected to be overridden
        """
        if self._content_type is None:
            raise PteContentTypeMustBeProvided(self)
        return self._content_type
