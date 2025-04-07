from pydantic import BaseModel
from typing import Optional

class Lead(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    company: Optional[str] = None
    position: Optional[str] = None
    source: Optional[str] = None
    lead_score: Optional[int] = None

    class Config:
        from_attributes = True

class LeadGenerationRequest(BaseModel):
    company_name: str
    industry: str
    budget: Optional[int] = None
    target_region: Optional[str] = None

    class Config:
        from_attributes = True
