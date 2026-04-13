from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

class CoffeeLogCreate(BaseModel):
    bean_name: str = Field(min_length=1)
    water_g: int
    dose_g: int
    overall_score: int = Field(ge=1, le=5)

logs = [
    {
        "id": 1,
        "bean_name": "Ethiopia",
        "water_g": 250,
        "dose_g": 15,
        "overall_score": 4
    }
]

@app.get("/logs")
def read_logs():
    return logs

@app.get("/logs/{log_id}")
def read_log_detail(log_id: int):
    for log in logs:
        if log["id"] == log_id:
            return log
    raise HTTPException(status_code=404, detail="Log not found")

@app.post("/logs")
def create_log(log: CoffeeLogCreate):
    new_log = {
    "id": len(logs) + 1,
    "bean_name": log.bean_name,
    "water_g": log.water_g,
    "dose_g": log.dose_g,
    "overall_score": log.overall_score
    }
    
    logs.append(new_log)
    return new_log

