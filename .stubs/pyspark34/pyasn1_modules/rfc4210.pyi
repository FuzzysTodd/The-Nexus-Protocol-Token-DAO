from _typeshed import Incomplete
from pyasn1.type import univ
from pyasn1_modules import rfc2314 as rfc2314, rfc2459 as rfc2459, rfc2511 as rfc2511

MAX: Incomplete

class KeyIdentifier(univ.OctetString): ...
class CMPCertificate(rfc2459.Certificate): ...
class OOBCert(CMPCertificate): ...
class CertAnnContent(CMPCertificate): ...

class PKIFreeText(univ.SequenceOf):
    """
    PKIFreeText ::= SEQUENCE SIZE (1..MAX) OF UTF8String
    """
    componentType: Incomplete
    sizeSpec: Incomplete

class PollRepContent(univ.SequenceOf):
    """
         PollRepContent ::= SEQUENCE OF SEQUENCE {
         certReqId              INTEGER,
         checkAfter             INTEGER,  -- time in seconds
         reason                 PKIFreeText OPTIONAL
     }
    """
    class CertReq(univ.Sequence):
        componentType: Incomplete
    componentType: Incomplete

class PollReqContent(univ.SequenceOf):
    """
         PollReqContent ::= SEQUENCE OF SEQUENCE {
         certReqId              INTEGER
     }

    """
    class CertReq(univ.Sequence):
        componentType: Incomplete
    componentType: Incomplete

class InfoTypeAndValue(univ.Sequence):
    """
    InfoTypeAndValue ::= SEQUENCE {
     infoType               OBJECT IDENTIFIER,
     infoValue              ANY DEFINED BY infoType  OPTIONAL
    }"""
    componentType: Incomplete

class GenRepContent(univ.SequenceOf):
    componentType: Incomplete

class GenMsgContent(univ.SequenceOf):
    componentType: Incomplete

class PKIConfirmContent(univ.Null): ...

class CRLAnnContent(univ.SequenceOf):
    componentType: Incomplete

class CAKeyUpdAnnContent(univ.Sequence):
    """
    CAKeyUpdAnnContent ::= SEQUENCE {
         oldWithNew   CMPCertificate,
         newWithOld   CMPCertificate,
         newWithNew   CMPCertificate
     }
    """
    componentType: Incomplete

class RevDetails(univ.Sequence):
    """
    RevDetails ::= SEQUENCE {
         certDetails         CertTemplate,
         crlEntryDetails     Extensions       OPTIONAL
     }
    """
    componentType: Incomplete

class RevReqContent(univ.SequenceOf):
    componentType: Incomplete

class CertOrEncCert(univ.Choice):
    """
     CertOrEncCert ::= CHOICE {
         certificate     [0] CMPCertificate,
         encryptedCert   [1] EncryptedValue
     }
    """
    componentType: Incomplete

class CertifiedKeyPair(univ.Sequence):
    """
    CertifiedKeyPair ::= SEQUENCE {
         certOrEncCert       CertOrEncCert,
         privateKey      [0] EncryptedValue      OPTIONAL,
         publicationInfo [1] PKIPublicationInfo  OPTIONAL
     }
    """
    componentType: Incomplete

class POPODecKeyRespContent(univ.SequenceOf):
    componentType: Incomplete

class Challenge(univ.Sequence):
    """
    Challenge ::= SEQUENCE {
         owf                 AlgorithmIdentifier  OPTIONAL,
         witness             OCTET STRING,
         challenge           OCTET STRING
     }
    """
    componentType: Incomplete

class PKIStatus(univ.Integer):
    """
    PKIStatus ::= INTEGER {
         accepted                (0),
         grantedWithMods        (1),
         rejection              (2),
         waiting                (3),
         revocationWarning      (4),
         revocationNotification (5),
         keyUpdateWarning       (6)
     }
    """
    namedValues: Incomplete

class PKIFailureInfo(univ.BitString):
    """
    PKIFailureInfo ::= BIT STRING {
         badAlg              (0),
         badMessageCheck     (1),
         badRequest          (2),
         badTime             (3),
         badCertId           (4),
         badDataFormat       (5),
         wrongAuthority      (6),
         incorrectData       (7),
         missingTimeStamp    (8),
         badPOP              (9),
         certRevoked         (10),
         certConfirmed       (11),
         wrongIntegrity      (12),
         badRecipientNonce   (13),
         timeNotAvailable    (14),
         unacceptedPolicy    (15),
         unacceptedExtension (16),
         addInfoNotAvailable (17),
         badSenderNonce      (18),
         badCertTemplate     (19),
         signerNotTrusted    (20),
         transactionIdInUse  (21),
         unsupportedVersion  (22),
         notAuthorized       (23),
         systemUnavail       (24),
         systemFailure       (25),
         duplicateCertReq    (26)
    """
    namedValues: Incomplete

class PKIStatusInfo(univ.Sequence):
    """
    PKIStatusInfo ::= SEQUENCE {
         status        PKIStatus,
         statusString  PKIFreeText     OPTIONAL,
         failInfo      PKIFailureInfo  OPTIONAL
     }
    """
    componentType: Incomplete

class ErrorMsgContent(univ.Sequence):
    """
    ErrorMsgContent ::= SEQUENCE {
         pKIStatusInfo          PKIStatusInfo,
         errorCode              INTEGER           OPTIONAL,
         -- implementation-specific error codes
         errorDetails           PKIFreeText       OPTIONAL
         -- implementation-specific error details
     }
    """
    componentType: Incomplete

class CertStatus(univ.Sequence):
    """
    CertStatus ::= SEQUENCE {
        certHash    OCTET STRING,
        certReqId   INTEGER,
        statusInfo  PKIStatusInfo OPTIONAL
     }
    """
    componentType: Incomplete

class CertConfirmContent(univ.SequenceOf):
    componentType: Incomplete

class RevAnnContent(univ.Sequence):
    """
    RevAnnContent ::= SEQUENCE {
         status              PKIStatus,
         certId              CertId,
         willBeRevokedAt     GeneralizedTime,
         badSinceDate        GeneralizedTime,
         crlDetails          Extensions  OPTIONAL
     }
    """
    componentType: Incomplete

class RevRepContent(univ.Sequence):
    """
    RevRepContent ::= SEQUENCE {
         status       SEQUENCE SIZE (1..MAX) OF PKIStatusInfo,
         revCerts [0] SEQUENCE SIZE (1..MAX) OF CertId
                                             OPTIONAL,
         crls     [1] SEQUENCE SIZE (1..MAX) OF CertificateList
                                             OPTIONAL
    """
    componentType: Incomplete

class KeyRecRepContent(univ.Sequence):
    """
    KeyRecRepContent ::= SEQUENCE {
         status                  PKIStatusInfo,
         newSigCert          [0] CMPCertificate OPTIONAL,
         caCerts             [1] SEQUENCE SIZE (1..MAX) OF
                                             CMPCertificate OPTIONAL,
         keyPairHist         [2] SEQUENCE SIZE (1..MAX) OF
                                             CertifiedKeyPair OPTIONAL
     }
    """
    componentType: Incomplete

class CertResponse(univ.Sequence):
    """
    CertResponse ::= SEQUENCE {
         certReqId           INTEGER,
         status              PKIStatusInfo,
         certifiedKeyPair    CertifiedKeyPair    OPTIONAL,
         rspInfo             OCTET STRING        OPTIONAL
     }
    """
    componentType: Incomplete

class CertRepMessage(univ.Sequence):
    """
    CertRepMessage ::= SEQUENCE {
         caPubs       [1] SEQUENCE SIZE (1..MAX) OF CMPCertificate
                          OPTIONAL,
         response         SEQUENCE OF CertResponse
     }
    """
    componentType: Incomplete

class POPODecKeyChallContent(univ.SequenceOf):
    componentType: Incomplete

class OOBCertHash(univ.Sequence):
    """
    OOBCertHash ::= SEQUENCE {
         hashAlg     [0] AlgorithmIdentifier     OPTIONAL,
         certId      [1] CertId                  OPTIONAL,
         hashVal         BIT STRING
     }
    """
    componentType: Incomplete

class NestedMessageContent(univ.SequenceOf):
    """
    NestedMessageContent ::= PKIMessages
    """
    componentType: Incomplete

class DHBMParameter(univ.Sequence):
    """
    DHBMParameter ::= SEQUENCE {
         owf                 AlgorithmIdentifier,
         -- AlgId for a One-Way Function (SHA-1 recommended)
         mac                 AlgorithmIdentifier
         -- the MAC AlgId (e.g., DES-MAC, Triple-DES-MAC [PKCS11],
     }   -- or HMAC [RFC2104, RFC2202])
    """
    componentType: Incomplete

id_DHBasedMac: Incomplete

class PBMParameter(univ.Sequence):
    """
    PBMParameter ::= SEQUENCE {
         salt                OCTET STRING,
         owf                 AlgorithmIdentifier,
         iterationCount      INTEGER,
         mac                 AlgorithmIdentifier
     }
    """
    componentType: Incomplete

id_PasswordBasedMac: Incomplete

class PKIProtection(univ.BitString): ...

nestedMessageContent: Incomplete

class PKIBody(univ.Choice):
    """
    PKIBody ::= CHOICE {       -- message-specific body elements
         ir       [0]  CertReqMessages,        --Initialization Request
         ip       [1]  CertRepMessage,         --Initialization Response
         cr       [2]  CertReqMessages,        --Certification Request
         cp       [3]  CertRepMessage,         --Certification Response
         p10cr    [4]  CertificationRequest,   --imported from [PKCS10]
         popdecc  [5]  POPODecKeyChallContent, --pop Challenge
         popdecr  [6]  POPODecKeyRespContent,  --pop Response
         kur      [7]  CertReqMessages,        --Key Update Request
         kup      [8]  CertRepMessage,         --Key Update Response
         krr      [9]  CertReqMessages,        --Key Recovery Request
         krp      [10] KeyRecRepContent,       --Key Recovery Response
         rr       [11] RevReqContent,          --Revocation Request
         rp       [12] RevRepContent,          --Revocation Response
         ccr      [13] CertReqMessages,        --Cross-Cert. Request
         ccp      [14] CertRepMessage,         --Cross-Cert. Response
         ckuann   [15] CAKeyUpdAnnContent,     --CA Key Update Ann.
         cann     [16] CertAnnContent,         --Certificate Ann.
         rann     [17] RevAnnContent,          --Revocation Ann.
         crlann   [18] CRLAnnContent,          --CRL Announcement
         pkiconf  [19] PKIConfirmContent,      --Confirmation
         nested   [20] NestedMessageContent,   --Nested Message
         genm     [21] GenMsgContent,          --General Message
         genp     [22] GenRepContent,          --General Response
         error    [23] ErrorMsgContent,        --Error Message
         certConf [24] CertConfirmContent,     --Certificate confirm
         pollReq  [25] PollReqContent,         --Polling request
         pollRep  [26] PollRepContent          --Polling response

    """
    componentType: Incomplete

class PKIHeader(univ.Sequence):
    """
    PKIHeader ::= SEQUENCE {
    pvno                INTEGER     { cmp1999(1), cmp2000(2) },
    sender              GeneralName,
    recipient           GeneralName,
    messageTime     [0] GeneralizedTime         OPTIONAL,
    protectionAlg   [1] AlgorithmIdentifier     OPTIONAL,
    senderKID       [2] KeyIdentifier           OPTIONAL,
    recipKID        [3] KeyIdentifier           OPTIONAL,
    transactionID   [4] OCTET STRING            OPTIONAL,
    senderNonce     [5] OCTET STRING            OPTIONAL,
    recipNonce      [6] OCTET STRING            OPTIONAL,
    freeText        [7] PKIFreeText             OPTIONAL,
    generalInfo     [8] SEQUENCE SIZE (1..MAX) OF
                     InfoTypeAndValue     OPTIONAL
    }

    """
    componentType: Incomplete

class ProtectedPart(univ.Sequence):
    """
     ProtectedPart ::= SEQUENCE {
         header    PKIHeader,
         body      PKIBody
     }
    """
    componentType: Incomplete

class PKIMessage(univ.Sequence):
    """
    PKIMessage ::= SEQUENCE {
    header           PKIHeader,
    body             PKIBody,
    protection   [0] PKIProtection OPTIONAL,
    extraCerts   [1] SEQUENCE SIZE (1..MAX) OF CMPCertificate
                  OPTIONAL
     }"""
    componentType: Incomplete

class PKIMessages(univ.SequenceOf):
    """
    PKIMessages ::= SEQUENCE SIZE (1..MAX) OF PKIMessage
    """
    componentType: Incomplete
    sizeSpec: Incomplete
