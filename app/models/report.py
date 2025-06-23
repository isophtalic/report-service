from pydantic import BaseModel, model_validator, field_validator
from typing import Literal, List, Dict, Optional
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


class Density(BaseModel):
    total: int
    density: str


class OverviewData(BaseModel):
    overview: Dict[str, Density]
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
    permission: Optional[List[PermissionType]]
    overview: Optional[OverviewData]
    appendix: Optional[Appendix]

    @model_validator(mode="after")
    def check_unique(self):
        if len(set(self.permission)) != len(self.permission):
            raise ValueError("Duplicate permissions are not allowed")
        return self

    @model_validator(mode="after")
    def ensure_key_overview_in_permission(self):
        if len(self.permission) == 0:
            self.overview.overview = {}
            return self


        filtered = {
            key: value
            for key, value in self.overview.overview.items()
            if key in self.permission
        }
        self.overview.overview = filtered
        return self

    @model_validator(mode="after")
    def ensure_key_appendix_in_permission(self):
        if len(self.permission) == 0:
            self.appendix = None
            return self

        permission = set(self.permission)
        if "risk" not in permission:
            self.appendix.vulnerability = None

        if "open-port" not in permission:
            self.appendix.open_port = None

        if "dl-credential" not in permission:
            self.appendix.dl_credential = None

        if "dl-credit-card" not in permission:
            self.appendix.dl_credit_card = None

        if "dl-document" not in permission:
            self.appendix.dl_document = None

        if "brand-abuse" not in permission:
            self.appendix.brand_abuse = None

        if "investigate" not in permission:
            self.appendix.investigate = None

        if "campaign-botnet" not in permission:
            self.appendix.campaign_botnet = None

        if "campaign-campaign" not in permission:
            self.appendix.campaign_campaign = None
        return self
