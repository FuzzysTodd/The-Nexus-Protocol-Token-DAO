from _typeshed import Incomplete
from mlflow.models import FlavorBackend as FlavorBackend
from mlflow.utils.string_utils import quote as quote

class RFuncBackend(FlavorBackend):
    """
    Flavor backend implementation for the generic R models.
    Predict and serve locally models with 'crate' flavor.
    """
    def build_image(self, model_uri, image_name, install_mlflow, mlflow_home, enable_mlserver) -> None: ...
    def generate_dockerfile(self, model_uri, output_path, install_mlflow, mlflow_home, enable_mlserver) -> None: ...
    version_pattern: Incomplete
    def predict(self, model_uri, input_path, output_path, content_type) -> None:
        """
        Generate predictions using R model saved with MLflow.
        Return the prediction results as a JSON.
        """
    def serve(self, model_uri, port, host, timeout, enable_mlserver, synchronous: bool = True, stdout: Incomplete | None = None, stderr: Incomplete | None = None) -> None:
        """
        Generate R model locally.

        NOTE: The `enable_mlserver` parameter is there to comply with the
        FlavorBackend interface but is not supported by MLServer yet.
        https://github.com/SeldonIO/MLServer/issues/183
        """
    def can_score_model(self): ...
