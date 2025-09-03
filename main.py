from http.client import HTTPException
from typing import List

from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

@app.get("/ping")
def hello():
    return "pong"



class Car(BaseModel):
    id: str
    brand: str
    model: str
    maxSpeed: int
    maxFuelCapacity:int


voiture: List[Car] = []


@app.get("/cars", response_model=List[Car])
def get_car():
    return voiture


@app.post("/cars", response_model=Car)
def create_car(voiture: Car):
    voiture.append(voiture)
    return voiture

@app.get("/etudiants/{id}", response_model=Car)
def update_car(id: int, updated_car: Car):
    for i, e in enumerate(voiture):
        if e.id == id:
            voiture[i] = updated_car
            return updated_car
    raise HTTPException(status_code=404, detail="car non trouvé")

