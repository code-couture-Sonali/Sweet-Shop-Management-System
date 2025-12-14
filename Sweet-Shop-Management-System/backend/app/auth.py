from passlib.context import CryptContext
from jose import jwt
from datetime import datetime,timedelta
SECRET_KEY='student_secret'
ALGORITHM='HS256'
pwd_context=CryptContext(schemes=['bcrypt'])
def hash_password(p):return pwd_context.hash(p)
def verify_password(p,h):return pwd_context.verify(p,h)
def create_token(data):data['exp']=datetime.utcnow()+timedelta(hours=1);return jwt.encode(data,SECRET_KEY,algorithm=ALGORITHM)
