from pydantic import BaseModel


class AppendixCampaign(BaseModel):
    name: str
    country: str
    sector: str
    created: int
