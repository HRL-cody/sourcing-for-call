import pytest

from shoe_scraper.platforms import alibaba, made_in_china, global_sources


@pytest.mark.asyncio
@pytest.mark.parametrize("module", [alibaba, made_in_china, global_sources])
async def test_search_returns_company(module):
    results = await module.search("shoes")
    assert len(results) == 1
    assert results[0].name
