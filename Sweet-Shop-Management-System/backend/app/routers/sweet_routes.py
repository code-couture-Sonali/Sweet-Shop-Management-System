from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from ..models import Sweet
from ..schemas import SweetCreate
from ..database import SessionLocal
from ..dependencies import get_current_user
router=APIRouter(prefix='/api/sweets')
def get_db():db=SessionLocal();yield db;db.close()
@router.post('')
def add_sweet(s:SweetCreate,db:Session=Depends(get_db),u=Depends(get_current_user)):
    db.add(Sweet(**s.dict()));db.commit();return {'message':'added'}
@router.get('')
def list_sweets(db:Session=Depends(get_db),u=Depends(get_current_user)):
    return db.query(Sweet).all()
@router.post('/{id}/purchase')
def purchase(id:int,db:Session=Depends(get_db),u=Depends(get_current_user)):
    sw=db.query(Sweet).get(id)
    if sw.quantity<=0:raise HTTPException(status_code=400,detail='Out of stock')
    sw.quantity-=1;db.commit();return {'message':'purchased'}
