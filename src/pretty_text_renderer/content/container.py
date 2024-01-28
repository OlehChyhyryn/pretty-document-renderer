import dataclasses
from typing import TYPE_CHECKING, Dict

from pretty_text_renderer.content.base import BaseContent

if TYPE_CHECKING:
    from pretty_text_renderer.blocks.base import BaseBlock


@dataclasses.dataclass
class Container(BaseContent):
    """
    Basic content class that can contain any other content objects.

    Supposed to be used with `ContainerBlock`, `ContainerFormatter` objects.

    Implement per-file-type Renderer class for this content type to be rendered.
    """

    children: Dict[str, BaseBlock] = dataclasses.field(default_factory=dict)
