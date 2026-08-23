from _typeshed import Incomplete

__all__ = ['EvalEnvironment', 'EvalFactor']

class VarLookupDict:
    def __init__(self, dicts) -> None: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value) -> None: ...
    def __contains__(self, key) -> bool: ...
    def get(self, key, default: Incomplete | None = None): ...

class EvalEnvironment:
    """Represents a Python execution environment.

    Encapsulates a namespace for variable lookup and set of __future__
    flags."""
    flags: Incomplete
    def __init__(self, namespaces, flags: int = 0) -> None: ...
    @property
    def namespace(self):
        """A dict-like object that can be used to look up variables accessible
        from the encapsulated environment."""
    def with_outer_namespace(self, outer_namespace):
        '''Return a new EvalEnvironment with an extra namespace added.

        This namespace will be used only for variables that are not found in
        any existing namespace, i.e., it is "outside" them all.'''
    def eval(self, expr, source_name: str = '<string>', inner_namespace={}):
        """Evaluate some Python code in the encapsulated environment.

        :arg expr: A string containing a Python expression.
        :arg source_name: A name for this string, for use in tracebacks.
        :arg inner_namespace: A dict-like object that will be checked first
          when `expr` attempts to access any variables.
        :returns: The value of `expr`.
        """
    @classmethod
    def capture(cls, eval_env: int = 0, reference: int = 0):
        '''Capture an execution environment from the stack.

        If `eval_env` is already an :class:`EvalEnvironment`, it is returned
        unchanged. Otherwise, we walk up the stack by ``eval_env + reference``
        steps and capture that function\'s evaluation environment.

        For ``eval_env=0`` and ``reference=0``, the default, this captures the
        stack frame of the function that calls :meth:`capture`. If ``eval_env
        + reference`` is 1, then we capture that function\'s caller, etc.

        This somewhat complicated calling convention is designed to be
        convenient for functions which want to capture their caller\'s
        environment by default, but also allow explicit environments to be
        specified. See the second example.

        Example::

          x = 1
          this_env = EvalEnvironment.capture()
          assert this_env.namespace["x"] == 1
          def child_func():
              return EvalEnvironment.capture(1)
          this_env_from_child = child_func()
          assert this_env_from_child.namespace["x"] == 1

        Example::

          # This function can be used like:
          #   my_model(formula_like, data)
          #     -> evaluates formula_like in caller\'s environment
          #   my_model(formula_like, data, eval_env=1)
          #     -> evaluates formula_like in caller\'s caller\'s environment
          #   my_model(formula_like, data, eval_env=my_env)
          #     -> evaluates formula_like in environment \'my_env\'
          def my_model(formula_like, data, eval_env=0):
              eval_env = EvalEnvironment.capture(eval_env, reference=1)
              return model_setup_helper(formula_like, data, eval_env)

        This is how :func:`dmatrix` works.

        .. versionadded: 0.2.0
           The ``reference`` argument.
        '''
    def subset(self, names):
        """Creates a new, flat EvalEnvironment that contains only
        the variables specified."""
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self): ...

class EvalFactor:
    code: Incomplete
    origin: Incomplete
    def __init__(self, code, origin: Incomplete | None = None) -> None:
        '''A factor class that executes arbitrary Python code and supports
        stateful transforms.

        :arg code: A string containing a Python expression, that will be
          evaluated to produce this factor\'s value.

        This is the standard factor class that is used when parsing formula
        strings and implements the standard stateful transform processing. See
        :ref:`stateful-transforms` and :ref:`expert-model-specification`.

        Two EvalFactor\'s are considered equal (e.g., for purposes of
        redundancy detection) if they contain the same token stream. Basically
        this means that the source code must be identical except for
        whitespace::

          assert EvalFactor("a + b") == EvalFactor("a+b")
          assert EvalFactor("a + b") != EvalFactor("b + a")
        '''
    def name(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self): ...
    def memorize_passes_needed(self, state, eval_env): ...
    def memorize_chunk(self, state, which_pass, data) -> None: ...
    def memorize_finish(self, state, which_pass) -> None: ...
    def eval(self, memorize_state, data): ...

class _MockTransform:
    def __init__(self) -> None: ...
    def memorize_chunk(self, data) -> None: ...
    def memorize_finish(self) -> None: ...
    def transform(self, data): ...

class _FuncallCapturer:
    func: Incomplete
    tokens: Incomplete
    paren_depth: int
    started: bool
    done: bool
    def __init__(self, start_token_type, start_token) -> None: ...
    def add_token(self, token_type, token) -> None: ...
