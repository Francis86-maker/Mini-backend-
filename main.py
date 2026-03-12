from fastapi import FastAPI 
from .databasemodels import Base
from sqlalchemy.orm import engine 

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(transfer.routers)
app.include_router(Deposit.routers)
app.include_router(user.routers)
app.include_router(Login.routers)
app.include_router(delete.routers)
app.include_router(Transfer.routers)
app.include_router(blog.routers)
