from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import User
from ..schemas import UserCreate
from ..auth import hash_password,verify_password,create_token
router=APIRouter(prefix='/api/auth')
def get_db():db=SessionLocal();yield db;db.close()
@router.post('/register')
def register(user:UserCreate,db:Session=Depends(get_db)):
    db.add(User(username=user.username,password=hash_password(user.password)));db.commit();return {'message':'registered'}
@router.post('/login')
def login(user:UserCreate,db:Session=Depends(get_db)):
    u=db.query(User).filter(User.username==user.username).first()
    if not u or not verify_password(user.password,u.password):return {'error':'invalid'}
    return {'access_token':create_token({'sub':u.username,'role':u.role})}
