from ._signatures import Parameter as Parameter, signature as signature
from _typeshed import Incomplete

PY3: Incomplete

def callback_prototype(prototype):
    """Decorator to process a callback prototype.
    
    A callback prototype is a function whose signature includes all the values
    that will be passed by the callback API in question.
    
    The original function will be returned, with a ``prototype.adapt`` attribute
    which can be used to prepare third party callbacks.
    """
