from fastapi import APIRouter
from services.openai_service import generate_appointment_email
from services.notion_service import send_to_notion
from models.lead import LeadGenerationRequest

router = APIRouter()

@router.post("/")
async def create_appointment(data: LeadGenerationRequest):
    appointment_email = await generate_appointment_email(data.dict())
    notion_response = await send_to_notion(appointment_email)
    return {"appointment_email": appointment_email, "notion_response": notion_response}
