# src/des_utils.py
# Utility functions shared by pages

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


def des_encrypt(plaintext: bytes, key: bytes) -> bytes:
    """Encrypt plaintext (bytes) using DES ECB mode with PKCS7 padding."""
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(pad(plaintext, DES.block_size))


def des_decrypt(ciphertext: bytes, key: bytes) -> bytes:
    """Decrypt ciphertext (bytes) using DES ECB mode and remove padding."""
    cipher = DES.new(key, DES.MODE_ECB)
    return unpad(cipher.decrypt(ciphertext), DES.block_size)


def int_to_bytes64(i: int) -> bytes:
    """Convert integer to 8-byte big-endian bytes."""
    return i.to_bytes(8, byteorder="big")


def bytes_to_int64(b: bytes) -> int:
    """Convert 8-byte big-endian bytes to integer."""
    return int.from_bytes(b, byteorder="big")


def generate_random_key() -> bytes:
    """Generate a random 8-byte DES key."""
    return get_random_bytes(8)
