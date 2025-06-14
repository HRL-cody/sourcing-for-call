from ..models import Company


async def search(query: str) -> list[Company]:
    return [
        Company(
            name="MadeInChina Supplier",
            phone="111-1111",
            source="made-in-china",
            url="https://madeinchina.example.com",
        )
    ]
