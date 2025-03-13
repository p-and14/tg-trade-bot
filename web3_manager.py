from web3 import AsyncWeb3
from web3.providers import AsyncHTTPProvider

from config import INFURA_KEY


web3 = AsyncWeb3(AsyncHTTPProvider(f"https://mainnet.infura.io/v3/{INFURA_KEY}"))
