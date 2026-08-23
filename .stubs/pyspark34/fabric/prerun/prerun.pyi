from .mlflow_prerun import MlflowPrerun as MlflowPrerun
from .openai_prerun import OpenAIPrerun as OpenAIPrerun
from .usage_telemetry_prerun import UsageTelemetryPrerun as UsageTelemetryPrerun, without_usage_telemetry as without_usage_telemetry
from pyspark.sql.session import SparkSession as SparkSession

class FabricMLPrerun:
    @staticmethod
    def initialize(global_namespace: dict) -> None:
        """
        This is called when live session is pooled(so prior to init_personalized_session), no ws settings
        And after init_personalized_session if is not called in pooling stage (%pip install, which restarts notebook session)
        """
    @staticmethod
    def init_personalized_session(spark: SparkSession) -> None:
        """
        This is called after notebook attach to live pool session, ws settings are available
        """
    @staticmethod
    def add_custom_magic(jvmMagicHelper) -> None: ...
