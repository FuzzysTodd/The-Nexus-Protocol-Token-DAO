from _typeshed import Incomplete
from ctypes import c_bool, c_int32, c_long, c_uint32, c_ulong, c_void_p

version: Incomplete
version_info: Incomplete

def load_cdll(name, macos10_16_path):
    """Loads a CDLL by name, falling back to known path on 10.16+"""

Security: Incomplete
CoreFoundation: Incomplete
Boolean = c_bool
CFIndex = c_long
CFStringEncoding = c_uint32
CFData = c_void_p
CFString = c_void_p
CFArray = c_void_p
CFMutableArray = c_void_p
CFDictionary = c_void_p
CFError = c_void_p
CFType = c_void_p
CFTypeID = c_ulong
CFTypeRef: Incomplete
CFAllocatorRef = c_void_p
OSStatus = c_int32
CFDataRef: Incomplete
CFStringRef: Incomplete
CFArrayRef: Incomplete
CFMutableArrayRef: Incomplete
CFDictionaryRef: Incomplete
CFArrayCallBacks = c_void_p
CFDictionaryKeyCallBacks = c_void_p
CFDictionaryValueCallBacks = c_void_p
SecCertificateRef: Incomplete
SecExternalFormat = c_uint32
SecExternalItemType = c_uint32
SecIdentityRef: Incomplete
SecItemImportExportFlags = c_uint32
SecItemImportExportKeyParameters = c_void_p
SecKeychainRef: Incomplete
SSLProtocol = c_uint32
SSLCipherSuite = c_uint32
SSLContextRef: Incomplete
SecTrustRef: Incomplete
SSLConnectionRef = c_uint32
SecTrustResultType = c_uint32
SecTrustOptionFlags = c_uint32
SSLProtocolSide = c_uint32
SSLConnectionType = c_uint32
SSLSessionOption = c_uint32
SSLReadFunc: Incomplete
SSLWriteFunc: Incomplete

class CFConst:
    """
    A class object that acts as essentially a namespace for CoreFoundation
    constants.
    """
    kCFStringEncodingUTF8: Incomplete

class SecurityConst:
    """
    A class object that acts as essentially a namespace for Security constants.
    """
    kSSLSessionOptionBreakOnServerAuth: int
    kSSLProtocol2: int
    kSSLProtocol3: int
    kTLSProtocol1: int
    kTLSProtocol11: int
    kTLSProtocol12: int
    kTLSProtocol13: int
    kTLSProtocolMaxSupported: int
    kSSLClientSide: int
    kSSLStreamType: int
    kSecFormatPEMSequence: int
    kSecTrustResultInvalid: int
    kSecTrustResultProceed: int
    kSecTrustResultDeny: int
    kSecTrustResultUnspecified: int
    kSecTrustResultRecoverableTrustFailure: int
    kSecTrustResultFatalTrustFailure: int
    kSecTrustResultOtherError: int
    errSSLProtocol: int
    errSSLWouldBlock: int
    errSSLClosedGraceful: int
    errSSLClosedNoNotify: int
    errSSLClosedAbort: int
    errSSLXCertChainInvalid: int
    errSSLCrypto: int
    errSSLInternal: int
    errSSLCertExpired: int
    errSSLCertNotYetValid: int
    errSSLUnknownRootCert: int
    errSSLNoRootCert: int
    errSSLHostNameMismatch: int
    errSSLPeerHandshakeFail: int
    errSSLPeerUserCancelled: int
    errSSLWeakPeerEphemeralDHKey: int
    errSSLServerAuthCompleted: int
    errSSLRecordOverflow: int
    errSecVerifyFailed: int
    errSecNoTrustSettings: int
    errSecItemNotFound: int
    errSecInvalidTrustSettings: int
    TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384: int
    TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384: int
    TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256: int
    TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256: int
    TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256: int
    TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256: int
    TLS_DHE_RSA_WITH_AES_256_GCM_SHA384: int
    TLS_DHE_RSA_WITH_AES_128_GCM_SHA256: int
    TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384: int
    TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384: int
    TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA: int
    TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA: int
    TLS_DHE_RSA_WITH_AES_256_CBC_SHA256: int
    TLS_DHE_RSA_WITH_AES_256_CBC_SHA: int
    TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256: int
    TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256: int
    TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA: int
    TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA: int
    TLS_DHE_RSA_WITH_AES_128_CBC_SHA256: int
    TLS_DHE_RSA_WITH_AES_128_CBC_SHA: int
    TLS_RSA_WITH_AES_256_GCM_SHA384: int
    TLS_RSA_WITH_AES_128_GCM_SHA256: int
    TLS_RSA_WITH_AES_256_CBC_SHA256: int
    TLS_RSA_WITH_AES_128_CBC_SHA256: int
    TLS_RSA_WITH_AES_256_CBC_SHA: int
    TLS_RSA_WITH_AES_128_CBC_SHA: int
    TLS_AES_128_GCM_SHA256: int
    TLS_AES_256_GCM_SHA384: int
    TLS_AES_128_CCM_8_SHA256: int
    TLS_AES_128_CCM_SHA256: int
