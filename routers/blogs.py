from .models import BlogCreste
from ..databasemodels import get_db
from fastapi import APIRouter, Depends, HTTPException 
from sqlalchemy import Session
from . import models

router = APIRouter()

@router.post('/blog')
def blogs(request: BlogCreate, db: Session=Depends(get_db)):
  new_blog = db.query(models.User).gilter(models.User.id == request.id).first()
  db.add(new_blog)
  db.commit()
  db.refresh(new_blog)
  return new_blog
