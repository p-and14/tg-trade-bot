import base64

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def generate_key(password: str, salt: str) -> bytes:
    password = bytes(password, encoding="utf-8")
    salt = bytes(salt, encoding="utf-16")

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=1_000_000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password))
