from pyasn1_modules.rfc2459 import *
from _typeshed import Incomplete

class Attribute(univ.Sequence):
    componentType: Incomplete

class AttributeValueAssertion(univ.Sequence):
    componentType: Incomplete

pkcs_7: Incomplete
data: Incomplete
signedData: Incomplete
envelopedData: Incomplete
signedAndEnvelopedData: Incomplete
digestedData: Incomplete
encryptedData: Incomplete

class ContentType(univ.ObjectIdentifier): ...
class ContentEncryptionAlgorithmIdentifier(AlgorithmIdentifier): ...
class EncryptedContent(univ.OctetString): ...

contentTypeMap: Incomplete

class EncryptedContentInfo(univ.Sequence):
    componentType: Incomplete

class Version(univ.Integer): ...

class EncryptedData(univ.Sequence):
    componentType: Incomplete

class DigestAlgorithmIdentifier(AlgorithmIdentifier): ...

class DigestAlgorithmIdentifiers(univ.SetOf):
    componentType: Incomplete

class Digest(univ.OctetString): ...

class ContentInfo(univ.Sequence):
    componentType: Incomplete

class DigestedData(univ.Sequence):
    componentType: Incomplete

class IssuerAndSerialNumber(univ.Sequence):
    componentType: Incomplete

class KeyEncryptionAlgorithmIdentifier(AlgorithmIdentifier): ...
class EncryptedKey(univ.OctetString): ...

class RecipientInfo(univ.Sequence):
    componentType: Incomplete

class RecipientInfos(univ.SetOf):
    componentType: Incomplete

class Attributes(univ.SetOf):
    componentType: Incomplete

class ExtendedCertificateInfo(univ.Sequence):
    componentType: Incomplete

class SignatureAlgorithmIdentifier(AlgorithmIdentifier): ...
class Signature(univ.BitString): ...

class ExtendedCertificate(univ.Sequence):
    componentType: Incomplete

class ExtendedCertificateOrCertificate(univ.Choice):
    componentType: Incomplete

class ExtendedCertificatesAndCertificates(univ.SetOf):
    componentType: Incomplete

class SerialNumber(univ.Integer): ...

class CRLEntry(univ.Sequence):
    componentType: Incomplete

class TBSCertificateRevocationList(univ.Sequence):
    componentType: Incomplete

class CertificateRevocationList(univ.Sequence):
    componentType: Incomplete

class CertificateRevocationLists(univ.SetOf):
    componentType: Incomplete

class DigestEncryptionAlgorithmIdentifier(AlgorithmIdentifier): ...
class EncryptedDigest(univ.OctetString): ...

class SignerInfo(univ.Sequence):
    componentType: Incomplete

class SignerInfos(univ.SetOf):
    componentType: Incomplete

class SignedAndEnvelopedData(univ.Sequence):
    componentType: Incomplete

class EnvelopedData(univ.Sequence):
    componentType: Incomplete

class DigestInfo(univ.Sequence):
    componentType: Incomplete

class SignedData(univ.Sequence):
    componentType: Incomplete

class Data(univ.OctetString): ...
