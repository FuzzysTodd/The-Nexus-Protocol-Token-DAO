from ..._internal import within_credential_chain as within_credential_chain

def log_get_token_async(fn): ...
def wrap_exceptions(fn):
    """Prevents leaking exceptions defined outside azure-core by raising ClientAuthenticationError from them.

    :param fn: The function to wrap.
    :type fn: ~typing.Callable
    :return: The wrapped function.
    :rtype: callable
    """
