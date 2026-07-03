from _typeshed import Incomplete

__all__ = ['TorchVersion', 'Version', 'InvalidVersion']

class _LazyImport:
    """Wraps around classes lazy imported from packaging.version
    Output of the function v in following snippets are identical:
       from packaging.version import Version
       def v():
           return Version('1.2.3')
    and
       Version = _LazyImport('Version')
       def v():
           return Version('1.2.3')
    The difference here is that in later example imports
    do not happen until v is called
    """
    def __init__(self, cls_name: str) -> None: ...
    def get_cls(self): ...
    def __call__(self, *args, **kwargs): ...
    def __instancecheck__(self, obj): ...

Version: Incomplete
InvalidVersion: Incomplete

class TorchVersion(str):
    """A string with magic powers to compare to both Version and iterables!
    Prior to 1.10.0 torch.__version__ was stored as a str and so many did
    comparisons against torch.__version__ as if it were a str. In order to not
    break them we have TorchVersion which masquerades as a str while also
    having the ability to compare against both packaging.version.Version as
    well as tuples of values, eg. (1, 2, 1)
    Examples:
        Comparing a TorchVersion object to a Version object
            TorchVersion('1.10.0a') > Version('1.10.0a')
        Comparing a TorchVersion object to a Tuple object
            TorchVersion('1.10.0a') > (1, 2)    # 1.2
            TorchVersion('1.10.0a') > (1, 2, 1) # 1.2.1
        Comparing a TorchVersion object against a string
            TorchVersion('1.10.0a') > '1.2'
            TorchVersion('1.10.0a') > '1.2.1'
    """
