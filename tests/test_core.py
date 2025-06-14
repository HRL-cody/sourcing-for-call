import httpx
import pytest

from shoe_scraper.core import fetch


@pytest.mark.asyncio
async def test_fetch_success():
    async def handler(request):
        return httpx.Response(200, text="hello")

    transport = httpx.MockTransport(handler)
    async with httpx.AsyncClient(transport=transport) as client:
        data = await fetch("https://example.com", client=client)
    assert data == "hello"
