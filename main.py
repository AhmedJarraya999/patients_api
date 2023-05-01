from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import json


class Patient(BaseModel):
    name: str = "John Smith"
    age: int = 45
    gender: str = "Male"
    height: str = "5'10\""
    weight: str = "185 lbs"
    blood_pressure: str = "120/80 mmHg"
    heart_rate: int = 70
    medical_history: str = "Hypertension, High Cholesterol, Family history of Heart Disease"
    medications: str = "Lisinopril, Atorvastatin"
    allergies: str = "None"
    lab_results: dict = {"Total Cholesterol": "210 mg/dL",
                         "LDL Cholesterol": "140 mg/dL",
                         "HDL Cholesterol": "50 mg/dL",
                         "Triglycerides": "120 mg/dL",
                         "Fasting Blood Glucose": "90 mg/dL"}
    notes: str = "Patient reports occasional chest pain and shortness of breath during exercise. Recommended stress test and echo cardiogram to evaluate cardiac function."

app = FastAPI()

@app.get("/patients")
async def get_patients():
    # Read and parse the JSON file
    with open('patients.json') as f:
        patients = json.load(f)

    # Return a JSON response for the list of patients
    return JSONResponse(content=patients)
