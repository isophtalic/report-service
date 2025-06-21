from pydantic import BaseModel, model_validator, field_validator
from typing import Literal, List, Dict
from datetime import datetime

from .chart import ChartData
from .appendix import Appendix

PermissionType = Literal[
    "risk",
    "dl-credential",
    "dl-credit-card",
    "dl-document",
    "brand-abuse",
    "investigate",
    "campaign-botnet",
    "campaign-campaign",
    "open-port"
]


class Destiny(BaseModel):
    total: int
    destiny: str


class OverviewData(BaseModel):
    overview: Dict[str, Destiny]
    chart: ChartData


class ExecutionTime(BaseModel):
    start: int
    end: int

    @model_validator(mode="after")
    def check_order(self) -> 'ExecutionTime':
        if self.end <= self.start:
            raise ValueError("`end` must be greater than `start`")
        return self

    @property
    def start_dt(self) -> datetime:
        return datetime.fromtimestamp(self.start)

    @property
    def end_dt(self) -> datetime:
        return datetime.fromtimestamp(self.end)


class Organization(BaseModel):
    name: str
    address: str
    execution_time: ExecutionTime


class Report(BaseModel):
    type: Literal["daily", "weekly", "monthly", "yearly"]
    organization: Organization
    permission: List[PermissionType]
    overview: OverviewData
    appendix: Appendix

    @field_validator("permission")
    def check_unique(self, v: List[str]):
        if len(set(v)) != len(v):
            raise ValueError("Duplicate permissions are not allowed")
        return v

    @model_validator(mode="after")
    def ensure_key_in_permission(self):
        filtered = {
            key: value
            for key, value in self.overview.overview.items()
            if key in self.permission
        }
        self.overview.overview = filtered
        return self
