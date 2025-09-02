from fastapi import FastAPI

# Création de l’application FastAPI
app = FastAPI()

# Route GET
@app.get("/hello")
def read_root():
    return {"message": "Hello romario"}
