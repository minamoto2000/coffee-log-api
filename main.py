from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class CoffeeLogCreate(BaseModel):
    bean_name: str = Field(min_length=1)
    water_g: int
    dose_g: int
    overall_score: int = Field(ge=1, le=5)


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.post("/logs")
def create_log(log: CoffeeLogCreate):
    return log