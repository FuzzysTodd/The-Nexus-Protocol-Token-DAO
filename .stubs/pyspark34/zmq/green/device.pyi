from zmq.green import Poller as Poller

def device(device_type, isocket, osocket) -> None:
    """Start a zeromq device (gevent-compatible).

    Unlike the true zmq.device, this does not release the GIL.

    Parameters
    ----------
    device_type : (QUEUE, FORWARDER, STREAMER)
        The type of device to start (ignored).
    isocket : Socket
        The Socket instance for the incoming traffic.
    osocket : Socket
        The Socket instance for the outbound traffic.
    """
