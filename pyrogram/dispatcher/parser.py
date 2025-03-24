from collections.abc import (
    Awaitable,
    Callable,
)

import pyrogram
from pyrogram.dispatcher.schemas import (
    TelegramRawUpdate,
    TelegramUpdate,
)

UpdateParserT = Callable[
    [
        "pyrogram.Client",
        "TelegramRawUpdate",
    ],
    Awaitable[TelegramUpdate],
]


class TelegramRawUpdateParser:
    def __init__(self) -> None:
        self._parser_by_constructor_id: dict[int, UpdateParserT | None] = {}

    def add_update_parser(
        self,
        constructor: type["pyrogram.raw.base.Update"],
        parser: UpdateParserT | None,
    ) -> None:
        self._parser_by_constructor_id[constructor.ID] = parser

    async def parse(
        self,
        client: pyrogram.Client,
        raw: TelegramRawUpdate[pyrogram.raw.base.Update],
    ) -> TelegramUpdate:
        parser = self._parser_by_constructor_id.get(raw.update.ID)
        if parser is None:
            return TelegramUpdate(
                raw=raw,
            )

        return await parser(client, raw)
