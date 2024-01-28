from typing import Type, cast

from pretty_text_renderer.content.base import BaseContent, TContent
from pretty_text_renderer.formatters.base import BaseFormatter


class IdentityFormatter(BaseFormatter[TContent]):
    def _format(self, content: TContent) -> TContent:
        return content.copy()

    def _get_content_type(self) -> Type[TContent]:
        return cast("Type[TContent]", BaseContent)
