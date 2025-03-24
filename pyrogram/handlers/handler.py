#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from collections.abc import Awaitable, Callable
from typing import (
    Any,
    ClassVar,
    TypeVar,
)

import pyrogram

UpdateT = TypeVar("UpdateT")


class Handler:
    event_type: ClassVar[str] = "unknown"

    def __init__(
        self,
        callback: Callable[["pyrogram.Client", UpdateT], Awaitable[Any]],
        filters: "pyrogram.filters.Filter | None" = None,
    ) -> None:
        self.callback = callback
        self.filters = filters

    async def check(self, client: "pyrogram.Client", update: UpdateT) -> bool:
        if self.filters is None:
            return True
        return await self.filters(client, update)
