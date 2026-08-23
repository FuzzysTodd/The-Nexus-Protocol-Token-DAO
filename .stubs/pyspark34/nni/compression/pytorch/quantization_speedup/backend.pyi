from _typeshed import Incomplete

class BaseModelSpeedup:
    """
    Base speedup class for backend engine
    """
    model: Incomplete
    config: Incomplete
    def __init__(self, model, config) -> None:
        """
        Parameters
        ----------
        model : pytorch model
            The model to speedup by quantization.
        config : dict
            Config recording bit number and name of layers.
        """
    def inference(self, test_data) -> None:
        """
        This function should be overrided by subclass to provide inference ability,
        which should return output and inference time.

        Parameters
        ----------
        test_data : numpy data
            test data given to the inference engine

        Returns
        -------
        numpy data
            output data will be generated after inference
        float
            latency of such inference process
        """
    def compress(self) -> None:
        """
        This function should be overrided by subclass to build inference
        engine which will be used to process input data
        """
    def export_quantized_model(self, path) -> None:
        """
        This function should be overrided by subclass to build inference
        engine which will be used to process input data
        """
