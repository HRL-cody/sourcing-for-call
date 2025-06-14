from pydantic import BaseModel


class Company(BaseModel):
    name: str
    phone: str
    source: str
    url: str
