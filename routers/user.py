from ..models import UserCreate 
from fastapi import APIRouter, Depends, HTTPException 
from ..databasemodels import get_db
from sqlalchemy import Session
from . import models
import bcrypt

router = APIRouter()

@router.post('/user')
def createuser(request: UserCreate, db: Session=Depends(get_db)):
  existing_email = db.query(models.User).filter(models.User.email == request.email).first()
  if existing_email:
    raise HTTPException(status_code=400, detail="Email already exists")
  password = request.password.encode("UTF-8")
  hashedpassword= bcrypt.hashpw(password, bcrypt.gensalt())
  new_user = models.User(name=request.name, email=request.email, password= hashedpassword)
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return {
    "name": new_user.name,
    "email": new_user.email,
    "message": "user created"
  }
