from datetime import datetime

from typing import Optional

from sqlalchemy import String, Integer, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    created: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_onupdate=func.now(), nullable=True)


class TgUser(Base):
    __tablename__ = "tg_user"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer(), unique=True)
    chat_id: Mapped[int] = mapped_column(Integer(), unique=True)
    username: Mapped[str] = mapped_column(String(50))
    first_name: Mapped[Optional[str]] = mapped_column(String(65), nullable=True)
    last_name: Mapped[Optional[str]] = mapped_column(String(65), nullable=True)
    wallet: Mapped["Wallet"] = relationship(back_populates="tg_user")


class Wallet(Base):
    __tablename__ = "wallet"

    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str] = mapped_column(String(45), unique=True)
    private_key: Mapped[str] = mapped_column(String(200), unique=True)
    tg_user_id: Mapped[int] = mapped_column(ForeignKey("tg_user.id", ondelete="CASCADE"))
    tg_user: Mapped["TgUser"] = relationship(back_populates="wallet")
