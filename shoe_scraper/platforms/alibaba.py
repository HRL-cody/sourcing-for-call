from ..models import Company


async def search(query: str) -> list[Company]:
    return [
        Company(
            name="Alibaba Supplier",
            phone="000-0000",
            source="alibaba",
            url="https://alibaba.example.com",
        )
    ]
