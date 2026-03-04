import encrypted_json

KEY = "SECRET"

"""
ENCRYPT
"""
x = encrypted_json.encrypt('tests/data.json', KEY)
with open('tests/data.json.enc', 'wb') as f:
    f.write(x)

#RETURNS encrypted data

"""
DECRYPT
"""

x = encrypted_json.decrypt('tests/data.json.enc', KEY)
print(x) 

#RETURNS {'text': 'helloworld'}