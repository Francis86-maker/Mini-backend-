from sqlalchemy import Session
from fastapi import APIRouter, Depends, HTTPException 
from ..databasemodels import get_db
from . import models 
from ..models import Login

router = APIRouter()

@router.post('/login')
def login(request: Login, db: Session=Depends(get_db)):
  user = db.query(models.User).filter(models.User.email == request.email)
  if not user:
    raise HTTPException(status_code=404, detail=" email not found")
  password = request.password.encode("UTF-8")
  hashed = bcrypt.checkpw(password, user.password)
  if not hashed:
    raise HTTPException(status_code= 404, detail="password not found")
  db.commit()
  return {
    "message": "login successful"
  }
