from contextvars import ContextVar
from dataclasses import dataclass
from typing import List, Optional

_http_exchanges: ContextVar[List["HttpExchange"]] = ContextVar("http_exchanges", default=[])


@dataclass
class HttpExchange:
    method: str
    url: str
    status_code: int
    request_body: str
    response_body: str
    curl: str


def begin_test() -> None:
    _http_exchanges.set([])


def record_exchange(
    *,
    method: str,
    url: str,
    status_code: int,
    request_body: str,
    response_body: str,
    curl: str,
) -> None:
    exchanges = list(_http_exchanges.get([]))
    exchanges.append(
        HttpExchange(
            method=method,
            url=url,
            status_code=status_code,
            request_body=request_body,
            response_body=response_body,
            curl=curl,
        )
    )
    _http_exchanges.set(exchanges)


def get_last_exchange() -> Optional[HttpExchange]:
    exchanges = _http_exchanges.get([])
    return exchanges[-1] if exchanges else None


def get_all_exchanges() -> List[HttpExchange]:
    return list(_http_exchanges.get([]))
