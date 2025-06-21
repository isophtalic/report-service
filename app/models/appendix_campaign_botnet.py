from pydantic import BaseModel


class AppendixCampaignBotnet(BaseModel):
    ip: str
    info: str
    created: int
