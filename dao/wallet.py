from typing import Optional

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from dao.models import Wallet


class WalletDAO:
    def __init__(self, session: Session):
        self.session = session

    def get_one_by_address(self, address: str) -> Optional[Wallet]:
        return self.session.query(Wallet).filter_by(address=address).one_or_none()
    
    def get_one_by_tg_user_id(self, tg_user_id: int) -> Optional[Wallet]:
        return self.session.query(Wallet).filter(Wallet.tg_user.has(user_id=tg_user_id)).one_or_none()
    
    def get_all(self) -> list[Wallet]:
        return self.session.query(Wallet).all()
    
    def create(self, **kwargs) -> Optional[Wallet]:
        wallet = Wallet(**kwargs)
        self.session.add(wallet)
        try:
            self.session.commit()
        except SQLAlchemyError:
            self.session.rollback()
            return None
        return wallet
    
    def delete(self, address: str) -> None:
        wallet = self.get_one_by_address(address)
        if wallet:
            self.session.delete(wallet)
            self.session.commit()
    