from fastapi import APIRouter, Depends, HTTPException 
from ..databasemodels import get_db
from .models import Transfermoney
from . import models
from sqlalchemy import Session

router = APIRouter()

@router.post('/transfer')
def transfer(request: Transfermoney, db: Session=Depends(get_db):
  if request.from_user_id == request.to_user_id:
    raise HTTPException(status_code=400, detail="cant transfer to self")
  from_user = db.query(models.User).filter(models.User.id == request.from_user_id).first()
  to_user = db.query(models.User).filter(models.User.id == request.to_used_id).first()
  if not from_user:
    raise HTTPException(status_code=404, detail="User not found")
  if not to_user:
    raise HTTPException(status_code=404, detail="user not found")
  if request.amount <= 0:
    raise HTTPException(status_code=400, detail="amount is too low")
  if request.amount > from_user.balance:
    raise HTTPException(status_code=400, detail="insufficient funds")
  from_user.balance -= request.amount
  to_user.balance += request.amount
  transfer_info = {
    "from_user": from_user.balance,
    "to_user": to_user.balance,
    "amount": request.amount
  }
  db.commit()
  db.refresh(from_user)
  db.refresh(to_user)
  return {
    "message": "transaction successful",
    "transfer_info": transfer_info
  }
