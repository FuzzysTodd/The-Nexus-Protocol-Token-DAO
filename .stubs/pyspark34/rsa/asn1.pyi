from _typeshed import Incomplete
from pyasn1.type import univ

class PubKeyHeader(univ.Sequence):
    componentType: Incomplete

class OpenSSLPubKey(univ.Sequence):
    componentType: Incomplete

class AsnPubKey(univ.Sequence):
    """ASN.1 contents of DER encoded public key:

    RSAPublicKey ::= SEQUENCE {
         modulus           INTEGER,  -- n
         publicExponent    INTEGER,  -- e
    """
    componentType: Incomplete
