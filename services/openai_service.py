from dotenv import load_dotenv
import os
import openai
import time
from openai.error import RateLimitError

#openai.api_key = "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"

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is loaded successfully
if openai.api_key is None:
    raise ValueError("OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")

import openai
import time
from openai.error import RateLimitError

# Function to generate a lead
async def generate_lead(data: dict):
    prompt = f"Generate a lead based on the following information: {data}"
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",  # Use the newer engine (instead of text-davinci-003)
            prompt=prompt,
            max_tokens=100,
            n=1  # Only one result
        )
        return response.choices[0].text.strip()

    except RateLimitError as e:
        print("Rate limit exceeded, waiting before retrying...")
        time.sleep(60)  # Sleep for 1 minute
        return await generate_lead(data)  # Retry the request


# Function to generate an appointment setting email
async def generate_appointment_email(data: dict):
    prompt = f"Generate an appointment setting email based on: {data}"
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",  # Use the newer engine (instead of text-davinci-003)
            prompt=prompt,
            max_tokens=150,
            n=1  # Only one result
        )
        return response.choices[0].text.strip()

    except RateLimitError as e:
        print("Rate limit exceeded, waiting before retrying...")
        time.sleep(60)  # Sleep for 1 minute
        return await generate_appointment_email(data)  # Retry the request


# Function to generate service deliverables
async def generate_service_deliverables(data: dict):
    prompt = f"Generate a service deliverable document based on: {data}"
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",  # Use the newer engine (instead of text-davinci-003)
            prompt=prompt,
            max_tokens=250,
            n=1  # Only one result
        )
        return response.choices[0].text.strip()

    except RateLimitError as e:
        print("Rate limit exceeded, waiting before retrying...")
        time.sleep(60)  # Sleep for 1 minute
        return await generate_service_deliverables(data)  # Retry the request


# New method to fetch multiple leads
async def generate_multiple_leads(data: dict, num_results: int = 5):
    prompt = f"Generate multiple leads based on the following information: {data}"
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",  # Use the newer engine (instead of text-davinci-003)
            prompt=prompt,
            max_tokens=100,
            n=num_results  # Specify how many completions to generate
        )
        leads = [choice.text.strip() for choice in response.choices]
        return leads

    except RateLimitError as e:
        print("Rate limit exceeded, waiting before retrying...")
        time.sleep(60)  # Sleep for 1 minute
        return await generate_multiple_leads(data)  # Retry the request
