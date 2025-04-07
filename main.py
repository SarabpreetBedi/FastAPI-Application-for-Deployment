from fastapi import FastAPI
from pydantic import BaseModel
import openai
from services.openai_service import generate_lead
from agents import lead_generation, appointment_setting, service_delivery

app = FastAPI()

# Define the Pydantic model for input validation
class LeadRequest(BaseModel):
    data: dict

# Register the routes for each agent
app.include_router(lead_generation.router, prefix="/lead-generation", tags=["Lead Generation"])
app.include_router(appointment_setting.router, prefix="/appointment-setting", tags=["Appointment Setting"])
app.include_router(service_delivery.router, prefix="/service-delivery", tags=["Service Delivery"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Growth Infrastructure Backend"}


@app.post("/generate-lead")
async def create_lead(request: LeadRequest):
    """
    This route will take input data and generate a lead using OpenAI.
    """
    data = request.data
    lead_info = await generate_lead(data)
    return {"lead_info": lead_info}

@app.get("/health")
def health_check():
    # A simple health check to make sure the app is running fine
    return {"status": "healthy"}



@app.get("/generate-multiple-leads")
async def generate_multiple_leads(data: dict, num_results: int = 5):
    """
    A route to generate multiple leads based on input data.
    num_results (default=5) specifies how many results to generate.
    """
    from services.openai_service import generate_multiple_leads

    leads = await generate_multiple_leads(data, num_results)
    return {"leads": leads}


# This will allow FastAPI to be hosted on any IP address (required for deployment).
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)