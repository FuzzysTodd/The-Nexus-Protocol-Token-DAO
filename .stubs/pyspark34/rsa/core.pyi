def assert_int(var: int, name: str) -> None: ...
def encrypt_int(message: int, ekey: int, n: int) -> int:
    """Encrypts a message using encryption key 'ekey', working modulo n"""
def decrypt_int(cyphertext: int, dkey: int, n: int) -> int:
    """Decrypts a cypher text using the decryption key 'dkey', working modulo n"""
