import hashlib
import os


def hash_password(salt, password):
    """Apply salted hashing"""
    return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)


def generate_salt():
    """Generate random salt of length 32 bytes"""
    return os.urandom(32)
