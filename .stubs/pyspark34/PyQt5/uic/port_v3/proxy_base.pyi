from ..Compiler.proxy_metaclass import ProxyMetaclass as ProxyMetaclass

class ProxyBase(metaclass=ProxyMetaclass):
    """ A base class for proxies using Python v3 syntax for setting the
    meta-class.
    """
