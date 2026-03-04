from cryptography.fernet import Fernet
import hashlib
import base64
import json

def make_key(user_string: str) -> bytes:
    hashed = hashlib.sha256(user_string.encode()).digest()
    return base64.urlsafe_b64encode(hashed)

def encrypt(file, key):
    """
    Load the unencrypted JSON file and encrypt the data.
    """
    with open(file, 'r') as f:
        data = json.load(f)
    ready_data = json.dumps(data).encode()
    f_enc = Fernet(make_key(key))
    return f_enc.encrypt(ready_data)

def decrypt(file, key):
    """
    Load the encrypted EJSON file and decrypt the data.
    """
    with open(file, 'r') as f:
        data = f.read().encode()
    f_enc = Fernet(make_key(key))
    return json.loads(f_enc.decrypt(data).decode())