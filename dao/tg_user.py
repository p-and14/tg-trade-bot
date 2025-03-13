from typing import Optional

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from dao.models import TgUser


class TgUserDAO:
    def __init__(self, session: Session):
        self.session = session

    def get_one_by_user_id(self, user_id: int) -> Optional[TgUser]:
        return self.session.query(TgUser).filter_by(user_id=user_id).one_or_none()
    
    def get_all(self) -> list[TgUser]:
        return self.session.query(TgUser).all()
    
    def create(self, **kwargs) -> Optional[TgUser]:
        user = TgUser(**kwargs)
        user.wallet
        self.session.add(user)
        try:
            self.session.commit()
        except SQLAlchemyError:
            self.session.rollback()
            return None
        return user
    
    def get_or_create(self, **kwargs) -> Optional[TgUser]:
        user = self.get_one_by_user_id(kwargs.get("user_id"))
        if user:
            return user
        
        user = self.create(**kwargs)
        return user
        
    def delete(self, user_id: int) -> None:
        user = self.get_one_by_user_id(user_id)
        if user:
            self.session.delete(user)
            self.session.commit()
    
    def update(self, **kwargs):
        user = self.get_one_by_user_id(kwargs.get("user_id"))
        if user:
            user.username = kwargs.get("username")
            user.first_name = kwargs.get("first_name")
            user.last_name = kwargs.get("last_name")
            self.session.add(user)
            self.session.commit()
    