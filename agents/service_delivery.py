from fastapi import APIRouter
from services.openai_service import generate_service_deliverables
from services.notion_service import send_to_notion
from models.lead import LeadGenerationRequest

router = APIRouter()

@router.post("/")
async def deliver_service(data: LeadGenerationRequest):
    service_deliverable = await generate_service_deliverables(data.dict())
    notion_response = await send_to_notion(service_deliverable)
    return {"service_deliverable": service_deliverable, "notion_response": notion_response}
