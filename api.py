from fastapi import FastAPI
from SYSTEM_INFO import get_system_details

app = FastAPI(title="Devops Utilites API")

@app.get("/hello")
def hello():
    return {"message" : "Hellow this is sample python api"}
@app.get("/metrics")
def metrics():
    return get_system_details()