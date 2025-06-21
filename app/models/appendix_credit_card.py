from pydantic import BaseModel


class AppendixDLCreditCard(BaseModel):
    number: str
    expiry: str
    created: int
