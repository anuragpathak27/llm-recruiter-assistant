import requests
from dotenv import load_dotenv
import os

load_dotenv()
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"

headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}

def query_huggingface(payload):
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()
        if isinstance(data, list) and "generated_text" in data[0]:
            return data[0]["generated_text"]
        elif "error" in data:
            return f"Error: {data['error']}"
        return "Message could not be generated."
    except Exception as e:
        return f"Exception occurred: {str(e)}"

def generate_messages(candidates, job_description):
    messages = []
    for cand in candidates:
        name = cand.get("name", "Candidate")
        headline = cand.get("headline", "engineering")

        prompt = f"""
        Write a professional and personalized LinkedIn message to {name} for the job:
        '{job_description}'.
        Their headline is: '{headline}'.
        Mention their background and invite them to learn more.
        """

        response = query_huggingface({
            "inputs": prompt,
            "parameters": {"max_new_tokens": 300}
        })

        try:
            text = response[0]["generated_text"]
        except:
            text = f"Failed to generate message for {name}. API response: {response}"

        messages.append({
            "candidate": name,
            "message": text.strip()
        })
    return messages
