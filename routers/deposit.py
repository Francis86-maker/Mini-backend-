from ..models import Deposit
from fastapi import APIRouter, Depends, HTTPException 
from ..databasemodels import get_db
from sqlalchemy import Session
from . import models 

router = APIRouter()

@router.post('/deposit')
def deposit(request: Deposit, db: Session=Depends(get_db)):
  user = db.query(models.User).filter(models.User.id == request.id).first()
  if not user:
    raise HTTPException(status_code=404, detail="user not found")
  if request.amount <= 0:
    raise HTTPException(status_code=400, detail="amount is too low")
  user.balance += request.amount
  db.commit()
  db.refresh(user)
  return {
    "message": "successful"
  }
