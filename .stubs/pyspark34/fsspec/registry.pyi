from _typeshed import Incomplete

__all__ = ['registry', 'get_filesystem_class', 'default']

registry: Incomplete
default: str

def get_filesystem_class(protocol):
    '''Fetch named protocol implementation from the registry

    The dict ``known_implementations`` maps protocol names to the locations
    of classes implementing the corresponding file-system. When used for the
    first time, appropriate imports will happen and the class will be placed in
    the registry. All subsequent calls will fetch directly from the registry.

    Some protocol implementations require additional dependencies, and so the
    import may fail. In this case, the string in the "err" field of the
    ``known_implementations`` will be given as the error message.
    '''
