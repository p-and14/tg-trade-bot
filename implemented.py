from db import session
from dao.tg_user import TgUserDAO
from dao.wallet import WalletDAO


tg_user_dao = TgUserDAO(session)
wallet_dao = WalletDAO(session)
