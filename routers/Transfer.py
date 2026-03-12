from fastapi import APIRouter, Depends 
from sqlalchemy import Session
from ..databasemodels import get_db

router = APIRouter()


@router.get('/transfer')

def transfer_history(id: int, db: Session=Depends(get_db)):
  transfer = db.query(Transfer).filter(
    Transfer.from_user_id == user.id
    OR
    Transfer.from_user_id == user.id
  ).all()
  return tranfer
  
