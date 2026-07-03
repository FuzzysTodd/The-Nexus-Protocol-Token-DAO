from .functoolz import has_keywords as has_keywords, has_varargs as has_varargs, is_arity as is_arity, is_partial_args as is_partial_args, num_required_args as num_required_args
from _typeshed import Incomplete

module_info: Incomplete

def num_pos_args(sigspec):
    """ Return the number of positional arguments.  ``f(x, y=1)`` has 1"""
def get_exclude_keywords(num_pos_only, sigspec):
    """ Return the names of position-only arguments if func has **kwargs"""
def signature_or_spec(func): ...
def expand_sig(sig):
    """ Convert the signature spec in ``module_info`` to add to ``signatures``

    The input signature spec is one of:
        - ``lambda_func``
        - ``(num_position_args, lambda_func)``
        - ``(num_position_args, lambda_func, keyword_only_args)``

    The output signature spec is:
        ``(num_position_args, lambda_func, keyword_exclude, sigspec)``

    where ``keyword_exclude`` includes keyword only arguments and, if variadic
    keywords is present, the names of position-only argument.  The latter is
    included to support builtins such as ``partial(func, *args, **kwargs)``,
    which allows ``func=`` to be used as a keyword even though it's the name
    of a positional argument.
    """

signatures: Incomplete

def create_signature_registry(module_info=..., signatures=...) -> None: ...
def check_valid(sig, args, kwargs):
    """ Like ``is_valid_args`` for the given signature spec"""
def check_partial(sig, args, kwargs):
    """ Like ``is_partial_args`` for the given signature spec"""
def check_arity(n, sig): ...
def check_varargs(sig): ...
def check_keywords(sig): ...
def check_required_args(sig): ...
