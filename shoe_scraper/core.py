import random
from typing import Optional

import httpx

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
]


async def fetch(
    url: str,
    *,
    retries: int = 3,
    timeout: float = 10.0,
    client: Optional[httpx.AsyncClient] = None,
) -> str:
    """Fetch a URL and return the response text."""
    last_exc: Optional[Exception] = None
    headers = {"User-Agent": random.choice(USER_AGENTS)}
    for _ in range(retries):
        try:
            if client is None:
                async with httpx.AsyncClient(
                    http2=True, headers=headers, timeout=timeout
                ) as session:
                    resp = await session.get(url)
            else:
                resp = await client.get(url, headers=headers, timeout=timeout)
            resp.raise_for_status()
            return resp.text
        except Exception as exc:  # pragma: no cover - network errors
            last_exc = exc
    if last_exc:
        raise last_exc
    raise RuntimeError("Failed to fetch")
