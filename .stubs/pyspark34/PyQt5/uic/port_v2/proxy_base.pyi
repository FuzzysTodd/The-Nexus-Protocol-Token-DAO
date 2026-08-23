from ..Compiler.proxy_metaclass import ProxyMetaclass as ProxyMetaclass

class ProxyBase:
    """ A base class for proxies using Python v2 syntax for setting the
    meta-class.
    """
    __metaclass__ = ProxyMetaclass
