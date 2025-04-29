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

import asyncio
import logging
from typing import Any

from .transport import TCP, TCPAbridged

log = logging.getLogger(__name__)


class Connection:
    MAX_CONNECTION_ATTEMPTS = 3

    def __init__(
        self,
        address: tuple[str, int],
        ipv6: bool,
        proxy: dict[str, Any] | None,
        protocol_factory: type[TCP] = TCPAbridged,
    ) -> None:
        self.hostname, self.port = address
        self.ipv6 = ipv6
        self.proxy = proxy
        self.protocol_factory = protocol_factory
        self.protocol: TCP | None = None

        log.debug(
            "Initialized connection | host=%s port=%d ipv6=%s proxy=%s protocol=%s",
            self.hostname,
            self.port,
            self.ipv6,
            self.proxy,
            self.protocol_factory.__name__,
        )

    async def connect(self) -> None:
        for attempt in range(Connection.MAX_CONNECTION_ATTEMPTS):
            self.protocol = self.protocol_factory(ipv6=self.ipv6, proxy=self.proxy)
            try:
                log.info(
                    "Connecting (%d/%d) | host=%s port=%d ipv6=%s",
                    attempt + 1,
                    Connection.MAX_CONNECTION_ATTEMPTS,
                    self.hostname,
                    self.port,
                    self.ipv6,
                )
                await self.protocol.connect((self.hostname, self.port))
            except OSError as e:
                log.warning(
                    "Connection failed (%d/%d) | host=%s port=%d ipv6=%s error=%s",
                    attempt + 1,
                    Connection.MAX_CONNECTION_ATTEMPTS,
                    self.hostname,
                    self.port,
                    self.ipv6,
                    e,
                )
                await self.protocol.close()
                await asyncio.sleep(1)
            else:
                log.info(
                    "Connection established | host=%s port=%d ipv6=%s protocol=%s",
                    self.hostname,
                    self.port,
                    self.ipv6,
                    self.protocol_factory.__name__,
                )
                break
        else:
            log.error(
                "All connection attempts failed | host=%s port=%d ipv6=%s",
                self.hostname,
                self.port,
                self.ipv6,
            )
            raise ConnectionError(f"Failed to connect to {self.hostname}:{self.port}")

    async def close(self) -> None:
        if self.protocol:
            await self.protocol.close()
            log.info(
                "Connection closed | host=%s port=%d ipv6=%s",
                self.hostname,
                self.port,
                self.ipv6,
            )

    async def send(self, data: bytes) -> None:
        if not self.protocol:
            raise ConnectionError("No active connection")

        log.debug(
            "Sending %d bytes | host=%s port=%d ipv6=%s",
            len(data),
            self.hostname,
            self.port,
            self.ipv6,
        )
        await self.protocol.send(data)

    async def recv(self) -> bytes | None:
        if not self.protocol:
            raise ConnectionError("No active connection")

        data = await self.protocol.recv()
        log.debug(
            "Received %d bytes | host=%s port=%d ipv6=%s",
            len(data) if data else 0,
            self.hostname,
            self.port,
            self.ipv6,
        )
        return data
