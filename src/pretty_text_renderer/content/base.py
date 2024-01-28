from __future__ import annotations

import abc
import dataclasses
from typing import TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from typing_extensions import Self


@dataclasses.dataclass
class BaseContent(abc.ABC):  # noqa: B024
    def copy(self) -> Self:
        return dataclasses.replace(self)


TContent = TypeVar("TContent", bound=BaseContent)
