from pydantic import BaseModel


class AppendixAssetItem(BaseModel):
    value: str
    description: str


class AppendixOpenPort(BaseModel):
    ip: str
    port: int
    service: str
    version: str
