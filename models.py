from pydantic import BaseModel 

class User(BaseModel):
  name: str
  email: str
  password: str
  
class Blog(BaseModel):
  name: str
  
class Transfer(BaseModel):
  from_user_id: int
  to_user_id: int
  amount: int
  
class Deposit(BaseModel):
  amount: int
  
