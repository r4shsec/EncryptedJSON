![Banner](assets/banner.png)

---

Encrypted JSON is an easy way for you to encrypt or decrypt your JSON files.

## Install

```
pip install encryptjson
```

## Encrypt

```py
import encrypted_json

KEY = "YOURSECRETKEY"

x = encrypted_json.encrypt('tests/data.json', KEY) 

"""
Write to file.
"""

with open('tests/data.json.enc', 'wb') as f:
    f.write(x)
```

## Decrypt

```py
import encrypted_json

KEY = "YOURSECRETKEY"

x = encrypted_json.decrypt('tests/data.json.enc', KEY)
print(x)
```