from ..models import Company


async def search(query: str) -> list[Company]:
    return [
        Company(
            name="GlobalSources Supplier",
            phone="222-2222",
            source="global-sources",
            url="https://globalsources.example.com",
        )
    ]
