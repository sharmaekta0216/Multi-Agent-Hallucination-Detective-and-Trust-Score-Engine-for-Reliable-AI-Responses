from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import hashlib

from services.database_service import (
    create_user,
    get_user_by_email
)

router = APIRouter()


# -----------------------------
# SIGNUP MODEL
# -----------------------------
class SignupRequest(BaseModel):
    full_name: str
    email: str
    password: str


# -----------------------------
# LOGIN MODEL
# -----------------------------
class LoginRequest(BaseModel):
    email: str
    password: str


# -----------------------------
# SIGNUP
# -----------------------------
@router.post("/signup")
def signup(request: SignupRequest):

    existing = get_user_by_email(request.email)

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Email already exists."
        )

    password_hash = hashlib.sha256(
        request.password.encode()
    ).hexdigest()

    create_user(
        request.full_name,
        request.email,
        password_hash
    )

    return {
        "success": True,
        "message": "User registered successfully."
    }


# -----------------------------
# LOGIN
# -----------------------------
@router.post("/login")
def login(request: LoginRequest):

    user = get_user_by_email(request.email)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )

    password_hash = hashlib.sha256(
        request.password.encode()
    ).hexdigest()

    if password_hash != user["password_hash"]:
        raise HTTPException(
            status_code=401,
            detail="Incorrect password."
        )

    return {
    "success": True,
    "message": "Login successful.",
    "user_id": user["user_id"],
    "name": user["full_name"],
    "email": user["email"]
}