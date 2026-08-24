from _typeshed import Incomplete
from sentry_sdk._types import TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.api import set_context as set_context
from sentry_sdk.integrations import Integration as Integration
from sentry_sdk.utils import logger as logger

CONTEXT_TYPE: str
AWS_METADATA_HOST: str
AWS_TOKEN_URL: Incomplete
AWS_METADATA_URL: Incomplete
GCP_METADATA_HOST: str
GCP_METADATA_URL: Incomplete

class CLOUD_PROVIDER:
    """
    Name of the cloud provider.
    see https://opentelemetry.io/docs/reference/specification/resource/semantic_conventions/cloud/
    """
    ALIBABA: str
    AWS: str
    AZURE: str
    GCP: str
    IBM: str
    TENCENT: str

class CLOUD_PLATFORM:
    """
    The cloud platform.
    see https://opentelemetry.io/docs/reference/specification/resource/semantic_conventions/cloud/
    """
    AWS_EC2: str
    GCP_COMPUTE_ENGINE: str

class CloudResourceContextIntegration(Integration):
    """
    Adds cloud resource context to the Senty scope
    """
    identifier: str
    cloud_provider: str
    aws_token: str
    http: Incomplete
    gcp_metadata: Incomplete
    def __init__(self, cloud_provider: str = '') -> None: ...
    @staticmethod
    def setup_once() -> None: ...

context_getters: Incomplete
