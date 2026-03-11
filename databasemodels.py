from sqlalchemy.orm import sessionmaker, relationship 
from sqlalcmehy import Column, Integer, String, ForeignKey
from database import declarative_base

engine = create_engine(".sqlite:///blog.db", echo=True)
SessionLocal = sessionmaker(auto_commit=False, auto_Flush=False, bind=engine)
Base = declarative_base()
class Blog(Base):
   __tablename__ = "blogs"
   id = Column(Integer, primary_key=True, unique=True)
   name = Column(String)
   user_id = Column(Integer, ForeignKey("users.id"))
   creator = relationship("User", back_populates="blogs")
  
class User(Base):
   __tablename__ = "users"
   id = Column(Integer, primary_key=True, unique=True)
   name = Column(String)
   email = Column(String)
   password = Column(String)
   blogs = relationship("Blog", back_populates="creator")
class Transfer(Base):
   __tablename__ = "transfers"
   id = Column(Integer, primary_key=True, unique=True)
   from_user_id = Column(Integer)
   to_user_id = Column(Integer)
   amount = Column(Integer)
class Deposit(Base):
   __tablename__ = "deposits"
   id = Column(Integer, primary_key=True, unique=True)
   amount= Column(Integer)


def get_db():
   db = SessionLocal()
   try:
     yield db
   finally:
     db.close()
     
