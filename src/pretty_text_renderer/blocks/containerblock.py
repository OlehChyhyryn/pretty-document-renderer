from __future__ import annotations

from typing import Optional, cast
import uuid

from pretty_text_renderer.blocks.base import BaseBlock
from pretty_text_renderer.content.container import Container
from pretty_text_renderer.exceptions import PteChildNameAlreadyExists
from pretty_text_renderer.renderers.container import BaseContainerRenderer, ContainerRenderer


class ContainerBlock(BaseBlock[Container, BaseContainerRenderer]):
    """
    Special content type that can contain any other content types as its children.

    Specified to be used to connect data into a tree structure, when it is needed.

    By default, the container is empty and has no children. During the rendering process, the children
    are rendered in the order in which they were added to the container (this behavior is guaranteed
    by the python dictionary implementation).
    """

    _content_type = Container

    def __init__(self, content: Optional[Container] = None, renderer: Optional[BaseContainerRenderer] = None) -> None:
        super().__init__(content or Container(), cast("BaseContainerRenderer", renderer or ContainerRenderer()))

    def get_children_map(self) -> dict[str, BaseBlock]:
        """
        Return a copy of the children dictionary from the content object.

        Working with the returned dictionary will not affect the original
        block structure. If you want to update the structure, use methods of the Container class.
        """
        return self._content.children.copy()

    def get_block_names(self) -> list[str]:
        """
        Return a list of children's names from the content object.
        """
        return list(self._content.children.keys())

    def get_blocks(self) -> list[BaseBlock]:
        """
        Return a list of children from the content object.
        """
        return list(self._content.children.values())

    def flush(self) -> None:
        """
        Reset the content object and replace it with a new empty one.
        """
        self._content = Container()

    def pop(self) -> Container:
        """
        Reset the content object and return a copy of an original object
        """
        original = self._content.copy()
        self.flush()
        return original

    def add_block(self, block: BaseBlock, block_name: str | None = None) -> str:
        """
        Add a child block to the container.

        :param block: Child block to add.
        :param block_name: Name of the child block. If not specified, a random UUID will be used.
        :return: Name of the child block.

        :raises PteChildNameAlreadyExists: If a child with the same name already exists.
        """
        block_name = block_name or f"{block.__class__.__name__}_{str(uuid.uuid4())}"
        if block_name in self._content.children:
            raise PteChildNameAlreadyExists(block_name, self)
        self._content.children[block_name] = block
        return block_name

    def remove_block(self, block_name: str) -> None:
        """
        Remove a child from the container.

        :param block_name: Name of the child block.
        """
        self._content.children.pop(block_name)

    def pop_block(self, block_name: str) -> BaseBlock:
        """
        Remove a child from the container and return it.

        :param block_name: Name of the child block.
        :return: Child block.
        """
        return self._content.children.pop(block_name)

    def sort_blocks(self, new_order: list[str]) -> None:
        """
        Reorder children according to the specified list.

        :param new_order: List of children's names in the new order.
        """
        self._content = Container(children={name: self._content.children[name] for name in new_order})
