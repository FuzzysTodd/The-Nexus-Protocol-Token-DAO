from _typeshed import Incomplete

EXPLICIT_BATCH: int

def GiB(val): ...

class HostDeviceMem:
    host: Incomplete
    device: Incomplete
    def __init__(self, host_mem, device_mem) -> None:
        """
        This function builds an engine from an onnx model with calibration process.

        Parameters
        ----------
        host_mem : host memory
            Memory buffers of host
        device_mem : device memory
            Memory buffers of device
        """

def allocate_buffers(engine):
    """
    Allocates all buffers required for an engine, i.e. host/device inputs/outputs.

    Parameters
    ----------
    engine : tensorrt.ICudaEngine
        An ICudaEngine for executing inference on a built network

    Returns
    -------
    list
        All input HostDeviceMem of an engine
    list
        All output HostDeviceMem of an engine
    GPU bindings
        Device bindings
    GPU stream
        A stream is a sequence of commands (possibly issued by different host threads) that execute in order
    """
def do_inference_v2(context, bindings, inputs, outputs, stream): ...
