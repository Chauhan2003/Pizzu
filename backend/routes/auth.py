from fastapi import APIRouter
from pydantic import BaseModel

auth_router = APIRouter(prefix="/auth", tags=["Auth Management"])

class LoginUserRequestPayload(BaseModel):
    email: str
    password: str

@auth_router.post("/login")
async def login_user(req: LoginUserRequestPayload):
    return {
        "success": "true",
        "message": "User logged in successfully"
    }