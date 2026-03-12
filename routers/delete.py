from fastapi import APIRouter, HTTPException, Depends 
from . import models
from ..databasemodels import get_db
from sqlalchemy import Session


router = APIRouter()

@router.delete('/delete')
def delete_user(id: int, db: Session=Depends(get_db)):
  user = db.query(models.User).filter(models.User.id == request.id)
  if not user:
    raise HTTPException(status_code=404, detail="user not found")
  user.delete(synchronize_session=False)
  return {
    "message": "delete successful"
  }
