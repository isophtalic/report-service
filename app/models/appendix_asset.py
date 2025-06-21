from pydantic import BaseModel, Field
from typing import List


class AppendixAssetItem(BaseModel):
    value: str
    description: str


class AppendixAssetDomainIP(BaseModel):
    group: str
    assets: List[AppendixAssetItem]


class AppendixAsset(BaseModel):
    domain_ip: List[AppendixAssetDomainIP] = Field(alias="domain-ip")
    products: List[AppendixAssetItem]
    identify: List[AppendixAssetItem]
