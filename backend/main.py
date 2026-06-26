from fastapi import FastAPI
from dotenv import load_dotenv

app = FastAPI()

@app.get("/health")
def check_health():
    return {
        "success": "true",
        "message": "Server is healthy"
    }