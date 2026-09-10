from hashlib import sha1, sha256
from paramiko.kex_group1 import KexGroup1 as KexGroup1

class KexGroup14(KexGroup1):
    P: int
    G: int
    name: str
    hash_algo = sha1

class KexGroup14SHA256(KexGroup14):
    name: str
    hash_algo = sha256
