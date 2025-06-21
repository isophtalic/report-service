from pydantic import BaseModel, Field
from typing import List, Optional
from .appendix_asset import AppendixAsset
from .appendix_open_port import AppendixOpenPort
from .appendix_vulnerability import AppendixVulnerability
from .appendix_credential import AppendixDLCredential
from .appendix_credit_card import AppendixDLCreditCard
from .appendix_document import AppendixDLDocument
from .appendix_brand_abuse import AppendixBrandAbuse
from .appendix_investigate import AppendixInvestigate
from .appendix_campaign_botnet import AppendixCampaignBotnet
from .appendix_campaign_campaign import AppendixCampaign


class Appendix(BaseModel):
    asset: Optional[AppendixAsset]
    open_port: Optional[List[AppendixOpenPort]] = Field(default=None, alias="open-port")
    vulnerability: Optional[AppendixVulnerability]
    dl_credential: List[AppendixDLCredential] = Field(default=None, alias="dl-credential")
    dl_credit_card: List[AppendixDLCreditCard] = Field(default=None, alias="dl-credit-card")
    dl_document: List[AppendixDLDocument] = Field(default=None, alias="dl-document")
    brand_abuse: List[AppendixBrandAbuse] = Field(default=None, alias="brand-abuse")
    investigate: List[AppendixInvestigate]
    campaign_botnet: List[AppendixCampaignBotnet] = Field(default=None, alias="campaign-botnet")
    campaign_campaign: List[AppendixCampaign] = Field(default=None, alias="campaign-campaign")
