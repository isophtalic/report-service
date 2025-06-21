from pydantic import BaseModel


class AppendixDLCredential(BaseModel):
    path: str
    username: str
    password: str
    created: int
