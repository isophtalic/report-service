from pydantic import BaseModel


class AppendixBrandAbuse(BaseModel):
    name: str
    description: str
    created: int
