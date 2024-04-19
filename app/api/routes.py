from fastapi import APIRouter, HTTPException, status
from app.models.user import User
from app.schemas.user import  UserCreate
from app.services.auth_service import hash_password
from app.services import auth_service, user_service, evaluation_service

router = APIRouter()

@router.post("/signup", response_model=UserCreate)
async def signup(user_data: UserCreate):
    if User.objects(email=user_data.email).first() is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    hashed_password = hash_password(user_data.password)
    user_data.password = hashed_password  # Replace the password with the hashed one
    user_obj = User(**user_data.dict()).save()  # Save the new user to the database
    return user_data

@router.post("/login")
async def login():
    return {"message": "Login endpoint"}

@router.post("/logout")
async def logout():
    return {"message": "Logout endpoint"}

@router.put("/update_profile")
async def update_profile():
    return {"message": "Update profile endpoint"}

@router.post("/create_evaluation_request")
async def create_evaluation_request():
    return {"message": "Create evaluation request endpoint"}

@router.get("/browse_evaluations")
async def browse_evaluations():
    return {"message": "Browse evaluations endpoint"}

@router.get("/view_evaluation")
async def view_evaluation():
    return {"message": "View evaluation details endpoint"}

@router.get("/search")
async def search():
    return {"message": "Search endpoint"}

@router.post("/ask")
async def ask():
    return {"message": "Ask questions endpoint"}

