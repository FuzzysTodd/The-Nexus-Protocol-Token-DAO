import tensorrt as trt
from _typeshed import Incomplete

logger: Incomplete

class Calibrator(trt.IInt8Calibrator):
    algorithm: Incomplete
    cache_file: Incomplete
    data: Incomplete
    batch_size: Incomplete
    current_index: int
    device_input: Incomplete
    def __init__(self, training_data, cache_file, batch_size: int = 64, algorithm=...) -> None:
        """
        Parameters
        ----------
        training_data : numpy array
            The data using to calibrate quantization model
        cache_file : str
            The path user want to store calibrate cache file
        batch_size : int
            The batch_size of calibrating process
        algorithm : tensorrt.tensorrt.CalibrationAlgoType
            The algorithms of calibrating contains LEGACY_CALIBRATION,
            ENTROPY_CALIBRATION, ENTROPY_CALIBRATION_2, MINMAX_CALIBRATION.
            Please refer to https://docs.nvidia.com/deeplearning/tensorrt/api/
            python_api/infer/Int8/Calibrator.html for detail
        """
    def get_algorithm(self): ...
    def get_batch_size(self): ...
    def get_batch(self, names):
        """
        This function is used to define the way of feeding calibrating data each batch.

        Parameters
        ----------
        names : str
             The names of the network inputs for each object in the bindings array

        Returns
        -------
        list
            A list of device memory pointers set to the memory containing each network
            input data, or an empty list if there are no more batches for calibration.
            You can allocate these device buffers with pycuda, for example, and then
            cast them to int to retrieve the pointer
        """
    def read_calibration_cache(self):
        """
        If there is a cache, use it instead of calibrating again. Otherwise, implicitly return None.

        Returns
        -------
        cache object
            A cache object which contains calibration parameters for quantization
        """
    def write_calibration_cache(self, cache) -> None:
        """
        Write calibration cache to specific path.

        Parameters
        ----------
        cache : str
             The calibration cache to write
        """
