from pydantic import BaseModel


class AppendixInvestigate(BaseModel):
    domain: str
    status: int
    created: int
    completed: int
