from sqlalchemy.orm.session import Session
from sqlalchemy.exc import SQLAlchemyError
from schemas import UserBase
from db.models import DbUser
from db.hash import Hash
from fastapi import HTTPException


def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_users(db: Session):
    return db.query(DbUser).all()

def update_user(db: Session, id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: Hash.bcrypt(request.password)
    })
    db.commit()
    return "Ok"

def delete_user(db: Session, id: int):
    try:
        user = db.query(DbUser).filter(DbUser.id == id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found!")
        db.delete(user)
        db.commit()
        return {"message": "User deleted successfully"}
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")