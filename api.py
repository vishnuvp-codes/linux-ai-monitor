from fastapi import FastAPI
from monitor import get_system_data

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Linux AI Monitoring API"}

@app.get("/system")
def system_monitor():
    data = get_system_data()
    return data
