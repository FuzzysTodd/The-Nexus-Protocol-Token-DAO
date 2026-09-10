from .utils import within_credential_chain as within_credential_chain

def log_get_token(class_name):
    """Adds logging around get_token calls.

    :param str class_name: required for the sake of Python 2.7, which lacks an easy way to get the credential's class
        name from the decorated function
    :return: decorator function
    :rtype: callable
    """
def wrap_exceptions(fn):
    """Prevents leaking exceptions defined outside azure-core by raising ClientAuthenticationError from them.

    :param fn: The function to wrap.
    :type fn: ~typing.Callable
    :return: The wrapped function.
    :rtype: callable
    """
