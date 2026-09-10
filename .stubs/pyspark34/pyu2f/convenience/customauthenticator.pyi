from _typeshed import Incomplete
from pyu2f import errors as errors, model as model
from pyu2f.convenience import baseauthenticator as baseauthenticator

SK_SIGNING_PLUGIN_ENV_VAR: str
U2F_SIGNATURE_TIMEOUT_SECONDS: int
SK_SIGNING_PLUGIN_NO_ERROR: int
SK_SIGNING_PLUGIN_TOUCH_REQUIRED: int
SK_SIGNING_PLUGIN_WRONG_DATA: int

class CustomAuthenticator(baseauthenticator.BaseAuthenticator):
    '''Offloads U2F signing to a pluggable command-line tool.

  Offloads U2F signing to a signing plugin which takes the form of a
  command-line tool. The command-line tool is configurable via the
  SK_SIGNING_PLUGIN environment variable.

  The signing plugin should implement the following interface:

  Communication occurs over stdin/stdout, and messages are both sent and
  received in the form:

  [4 bytes - payload size (little-endian)][variable bytes - json payload]

  Signing Request JSON
  {
    "type": "sign_helper_request",
    "signData": [{
        "keyHandle": <url-safe base64-encoded key handle>,
        "appIdHash": <url-safe base64-encoded SHA-256 hash of application ID>,
        "challengeHash": <url-safe base64-encoded SHA-256 hash of ClientData>,
        "version": U2F protocol version (usually "U2F_V2")
        },...],
    "timeoutSeconds": <security key touch timeout>
  }

  Signing Response JSON
  {
    "type": "sign_helper_reply",
    "code": <result code>.
    "errorDetail": <text description of error>,
    "responseData": {
      "appIdHash": <url-safe base64-encoded SHA-256 hash of application ID>,
      "challengeHash": <url-safe base64-encoded SHA-256 hash of ClientData>,
      "keyHandle": <url-safe base64-encoded key handle>,
      "version": <U2F protocol version>,
      "signatureData": <url-safe base64-encoded signature>
    }
  }

  Possible response error codes are:

    NoError            = 0
    UnknownError       = -127
    TouchRequired      = 0x6985
    WrongData          = 0x6a80
  '''
    origin: Incomplete
    def __init__(self, origin) -> None: ...
    def Authenticate(self, app_id, challenge_data, print_callback=...):
        """See base class."""
    def IsAvailable(self):
        """See base class."""
