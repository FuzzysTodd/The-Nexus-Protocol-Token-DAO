import requests
from ..service_discovery import get_fabric_env_config as get_fabric_env_config
from ..token_utils import TokenUtils as TokenUtils
from .iprerun import IPrerun as IPrerun
from _typeshed import Incomplete
from pyspark.sql.session import SparkSession as SparkSession

logger: Incomplete

class TokenCredentialAuth:
    token_utils: Incomplete
    feature_name: Incomplete
    host: Incomplete
    def __init__(self, host: str = '', feature_name: str = ...) -> None: ...
    def __call__(self, req: requests.Request): ...

class OpenAIPrerun(IPrerun):
    api_base: Incomplete
    def __init__(self, api_base: str = '') -> None: ...
    def post_openai(self, module) -> None: ...
    def set_env_var(self) -> None: ...
    def get_api_base(self) -> str: ...
    def initialize(self, global_namespace: dict) -> None: ...
    def init_personalized_session(self, spark: SparkSession) -> None:
        """
        Migrate the openai prerun from Markus Cozowicz. This redirects openai to fabirc Cogservice

        """
    def add_custom_magic(self, jvmMagicHelper) -> None: ...
