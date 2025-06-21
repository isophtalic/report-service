from pydantic import BaseModel


class AppendixDLDocument(BaseModel):
    filename: str
    path: str
    size: int
    created: int
