class NumPyBackend:
    """Backend that uses numpy.fft"""
    __ua_domain__: str
    @staticmethod
    def __ua_function__(method, args, kwargs): ...

class EchoBackend:
    """Backend that just prints the __ua_function__ arguments"""
    __ua_domain__: str
    @staticmethod
    def __ua_function__(method, args, kwargs) -> None: ...
