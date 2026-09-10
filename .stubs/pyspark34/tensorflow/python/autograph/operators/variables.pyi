from _typeshed import Incomplete

def ld(v):
    """Load variable operator."""
def ldu(load_v, name):
    '''Load variable operator that returns Undefined when failing to evaluate.

  Note: the name ("load or return undefined") is abbreviated to minimize
  the amount of clutter in generated code.

  This variant of `ld` is useful when loading symbols that may be undefined at
  runtime, such as composite symbols, and whether they are defined or not cannot
  be determined statically. For example `d[\'a\']` is undefined when `d` is an
  empty dict.

  Args:
    load_v: Lambda that executes the actual read.
    name: Human-readable name of the symbol being read.
  Returns:
    Either the value of the symbol, or Undefined, if the symbol is not fully
    defined.
  '''

class Undefined:
    """Represents an undefined symbol in Python.

  This is used to reify undefined symbols, which is required to use the
  functional form of loops.
  Example:

    while n > 0:
      n = n - 1
      s = n
    return s  # Runtime error if n == 0

  This is valid Python code and will not result in an error as long as n
  is positive. The use of this class is to stay as close to Python semantics
  as possible for staged code of this nature.

  Converted version of the above showing the possible usage of this class:

    s = Undefined('s')
    init_state = (s,)
    s = while_loop(cond, body, init_state)
    return s  # s is an instance of Undefined if the loop never runs

  Attributes:
    symbol_name: Text, identifier for the undefined symbol
  """
    symbol_name: Incomplete
    def __init__(self, symbol_name) -> None: ...
    def read(self) -> None: ...
    def __getattribute__(self, name): ...
    def __getitem__(self, i): ...

class UndefinedReturnValue:
    """Represents a return value that is undefined."""
