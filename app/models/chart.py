from pydantic import BaseModel, Field
from typing import List, Optional


class ValueCountItem(BaseModel):
    value: str
    count: int


class FileCountItem(BaseModel):
    file: str
    count: int


class VulnerabilityChart(BaseModel):
    critical: int
    high: int
    medium: int
    low: int
    info: int


class DLCredentialChart(BaseModel):
    domain: List[ValueCountItem]
    account: List[ValueCountItem]


class ChartData(BaseModel):
    dl_credential: Optional[DLCredentialChart] = Field(default=None, alias="dl-credential")
    vulnerability: Optional[VulnerabilityChart] = Field(default=None)
    dl_document: Optional[List[FileCountItem]] = Field(default=None, alias="dl-document")

