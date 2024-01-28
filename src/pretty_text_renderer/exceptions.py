from __future__ import annotations

__all__ = [
    "PteException",
    "PteChildNameAlreadyExists",
    "PteContentTypeMustBeProvided",
    "PteIncorrectContentType",
]

import abc
from typing import TYPE_CHECKING, Type

if TYPE_CHECKING:
    from pretty_text_renderer.blocks.containerblock import ContainerBlock
    from pretty_text_renderer.common import WithContentTypeMixin
    from pretty_text_renderer.content.base import BaseContent


class PteException(Exception, abc.ABC):
    """
    This is the base exception class for the PrettyTextEditor. All custom exceptions in the PrettyTextEditor
    should inherit from this class.
    """


class PteChildNameAlreadyExists(PteException, KeyError):
    """
    This exception is raised when an attempt is made to add a child block with a name that already
    exists in the container. The container does not allow duplicate names for child blocks.
    """

    def __init__(self, block_name: str, container_obj: ContainerBlock) -> None:
        msg = (
            f"Child block with name `{block_name}` already exists in the container `{container_obj}`."
            f"Please, provide a unique name."
        )
        super().__init__(msg)


class PteContentTypeMustBeProvided(PteException, NotImplementedError):
    """
    This exception is raised when an attempt is made to get the content type from a class that does not
    specify the content type as a class variable not override getter method.
    """

    def __init__(self, with_content: WithContentTypeMixin) -> None:
        class_name = with_content.__class__.__name__
        msg = (
            f"`{class_name}` does not specify expected content type."
            f"Please, specify `{class_name}._content_type` class variable "
            f"or override `{class_name}._get_content_type` method."
        )
        super().__init__(msg)


class PteIncorrectContentType(PteException, TypeError):
    """
    This exception is raised when an attempt to populate a block with content of an incorrect type.
    """

    def __init__(
        self, block: WithContentTypeMixin, content: BaseContent, expected_content_type: Type[BaseContent]
    ) -> None:
        msg = (
            f"`{block.__class__.__name__}` expected content of type `{expected_content_type}`, "
            f"but got content of type `{content.__class__}`."
        )
        super().__init__(msg)
