from _typeshed import Incomplete
from openai.api_resources import Audio as Audio, ChatCompletion as ChatCompletion, Completion as Completion, Customer as Customer, Deployment as Deployment, Edit as Edit, Embedding as Embedding, Engine as Engine, ErrorObject as ErrorObject, File as File, FineTune as FineTune, Image as Image, Model as Model, Moderation as Moderation
from openai.error import APIError as APIError, InvalidRequestError as InvalidRequestError, OpenAIError as OpenAIError
from openai.version import VERSION

__all__ = ['APIError', 'Audio', 'ChatCompletion', 'Completion', 'Customer', 'Edit', 'Image', 'Deployment', 'Embedding', 'Engine', 'ErrorObject', 'File', 'FineTune', 'InvalidRequestError', 'Model', 'Moderation', 'OpenAIError', 'api_base', 'api_key', 'api_type', 'api_key_path', 'api_version', 'app_info', 'ca_bundle_path', 'debug', 'enable_telemetry', 'log', 'organization', 'proxy', 'verify_ssl_certs']

api_key: Incomplete
api_key_path: str | None
organization: Incomplete
api_base: Incomplete
api_type: Incomplete
api_version: Incomplete
verify_ssl_certs: bool
proxy: Incomplete
app_info: Incomplete
enable_telemetry: bool
ca_bundle_path: Incomplete
debug: bool
log: Incomplete
__version__ = VERSION
