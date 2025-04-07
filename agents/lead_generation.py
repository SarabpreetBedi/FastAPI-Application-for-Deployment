from fastapi import APIRouter
from services.openai_service import generate_lead
from services.notion_service import send_to_notion
from models.lead import LeadGenerationRequest

router = APIRouter()

@router.post("/")
async def create_lead(data: LeadGenerationRequest):
    lead_info = await generate_lead(data.dict())
    notion_response = await send_to_notion(lead_info)
    return {"lead_info": lead_info, "notion_response": notion_response}
