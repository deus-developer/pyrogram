from typing import (
    Any,
    Protocol,
)

from .tl_object import TLObject


class Invoker(Protocol):
    async def invoke[T](self, query: "TLFunction[T]") -> T:
        raise NotImplementedError


class TLFunction[T: Any](TLObject):
    async def emit(self, client: Invoker) -> T:
        return await client.invoke(self)
