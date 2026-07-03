from _typeshed import Incomplete

__all__ = ['device', 'proxy', 'proxy_steerable']

def device(device_type, frontend, backend): ...
def proxy(frontend, backend, capture: Incomplete | None = None) -> None: ...
def proxy_steerable(frontend, backend, capture: Incomplete | None = None, control: Incomplete | None = None) -> None:
    """proxy_steerable(frontend, backend, capture, control)

    Start a zeromq proxy with control flow.

    .. versionadded:: libzmq-4.1
    .. versionadded:: 18.0

    Parameters
    ----------
    frontend : Socket
        The Socket instance for the incoming traffic.
    backend : Socket
        The Socket instance for the outbound traffic.
    capture : Socket (optional)
        The Socket instance for capturing traffic.
    control : Socket (optional)
        The Socket instance for control flow.
    """
