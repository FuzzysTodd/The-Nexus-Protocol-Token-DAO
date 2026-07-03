from _typeshed import Incomplete

__all__ = ['make_all', 'remove_undocumented', 'reveal_undocumented']

def make_all(module_name, doc_string_modules: Incomplete | None = None):
    """Generates `__all__` from the docstring of one or more modules.

  Usage: `make_all(__name__)` or
  `make_all(__name__, [sys.modules(__name__), other_module])`. The doc string
  modules must each a docstring, and `__all__` will contain all symbols with
  `@@` references, where that symbol currently exists in the module named
  `module_name`.

  Args:
    module_name: The name of the module (usually `__name__`).
    doc_string_modules: a list of modules from which to take docstring.
    If None, then a list containing only the module named `module_name` is used.

  Returns:
    A list suitable for use as `__all__`.
  """
def reveal_undocumented(symbol_name, target_module: Incomplete | None = None) -> None:
    """Reveals a symbol that was previously removed by `remove_undocumented`.

  This should be used by tensorflow internal tests only. It explicitly
  defeats the encapsulation afforded by `remove_undocumented`.

  It throws an exception when the symbol was not hidden in the first place.

  Args:
    symbol_name: a string representing the full absolute path of the symbol.
    target_module: if specified, the module in which to restore the symbol.
  """
def remove_undocumented(module_name, allowed_exception_list: Incomplete | None = None, doc_string_modules: Incomplete | None = None) -> None:
    """Removes symbols in a module that are not referenced by a docstring.

  Args:
    module_name: the name of the module (usually `__name__`).
    allowed_exception_list: a list of names that should not be removed.
    doc_string_modules: a list of modules from which to take the docstrings.
    If None, then a list containing only the module named `module_name` is used.

    Furthermore, if a symbol previously added with `add_to_global_allowlist`,
    then it will always be allowed. This is useful for internal tests.

  Returns:
    None
  """
