from hashlib import sha512
from paramiko.kex_group1 import KexGroup1 as KexGroup1

class KexGroup16SHA512(KexGroup1):
    name: str
    P: int
    G: int
    hash_algo = sha512
