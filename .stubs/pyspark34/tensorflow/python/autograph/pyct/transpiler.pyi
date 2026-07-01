from _typeshed import Incomplete
from tensorflow.python.autograph.pyct import cache as cache, inspect_utils as inspect_utils, loader as loader, naming as naming, origin_info as origin_info, parser as parser, templates as templates, transformer as transformer

class _PythonFnFactory:
    """Helper object that wraps a Python function factory."""
    module: Incomplete
    source_map: Incomplete
    def __init__(self, name, freevars, extra_locals) -> None:
        """Creates a new factory for a Python function.

    Args:
      name: The function name.
      freevars: The list of non-global free variables for the function.
      extra_locals: Dict[Text, Any], names and values for custom variables that
        are accessible to the generated code as local variables.
    """
    def create(self, nodes, namer, inner_factory_name: str = 'inner_factory', outer_factory_name: str = 'outer_factory', future_features=()) -> None:
        """Initializes a function."""
    def instantiate(self, globals_, closure, defaults: Incomplete | None = None, kwdefaults: Incomplete | None = None):
        """Creates a new function instance."""

class GenericTranspiler:
    """A generic transpiler for Python functions.

  Its interface is the `transform` API, which can process Python function
  objects. Internally, it handles parsing.

  Users typically subclass this, customizing the `transform_ast` method. The
  output of transformed_ast is returned directly by `transform`. Existing
  methods like `transform_function` may also be overloaded.

  Example:

      class MyTransformer(GenericTranspiler):

        def transform_ast(self, node, ctx):
          result = <<transform node>>
          return result

      transformer = MyTransfomer()

      result = transformer.transform(f, ...)
      # result is the output
  """
    def get_transformed_name(self, node):
        """Returns a name for the output function. Subclasses may override this."""
    def transform_ast(self, node, ctx) -> None:
        """Performs an actual transformation of a function's AST.

    Subclasses must implement this method, and do not usually call it.

    Args:
      node: One or more ast.AST nodes representing the AST to be transformed.
      ctx: transformer.Context.
    """
    def transform(self, obj, user_context):
        """Transforms a Python object.

    Users typically call this method.

    Args:
      obj: A Python object, function, type, etc.
      user_context: An opaque object (may be None) that is forwarded to
        transform_ast, through the ctx.user attribute.
    Returns:
      The result of calling transform_function.

    Raises:
      NotImplementedError: if the type of obj is not handled.
    """
    def transform_module(self, mod, user_context):
        """Transforms a module.

    Subclasses may override this method. The return value is opaque.

    The method receives the original AST. The result is passed as-is to the
    output of `transform`.

    Args:
      mod: A Python module.
      user_context: An opaque object (may be None) that is forwarded to
        transform_ast, through the ctx.user attribute.
    Returns:
      List[Tuple[Any, Any]]. By default it returns the output of transform_ast,
      evaluated on each supported member, other than modules, together with a
      `transformer.Context` containing information about the transformation
      process.
    """
    def transform_function(self, fn, user_context):
        """Transforms a function.

    Subclasses may override this method. The return value is opaque.

    The method receives the original AST. The result is passed as-is to the
    output of `transform`.

    Args:
      fn: A function or lambda.
      user_context: An opaque object (may be None) that is forwarded to
        transform_ast, through the ctx.user attribute.
    Returns:
      Tuple[Any, Any]. By default it returns the output of transform_ast,
      together with a `transformer.Context` containing information about the
      transformation process.
    """

class PyToPy(GenericTranspiler):
    """A generic Python-to-Python transpiler.

  Its `transform` method offers a function-in, function-out interface.
  Internally, it takes care of parsing, caching and loading of the translated
  code.

  Users typically subclass this, overriding `transform_ast`.

  Usually, instances of this class are singletons, since each instance manages
  its own cache. The caching can be controlled by overriding `get_caching_key`.

  Example:

      class MyTransformer(PyToPy):

        def transform_ast(self, node, ctx):
          node = <<transform node, usually using ast.NodeTransformer classes>>
          return node

      transformer = MyTransfomer()

      new_f, module, source_map = transformer.transform_function(f, ...)
      # new_f is a function with signature identical to f

  The transformed function has access to the same namespace as the original
  function. To allow access to internal APIs, users may inject additional
  symbols by overriding `get_extra_locals`.
  """
    def __init__(self) -> None: ...
    def get_extra_locals(self) -> None:
        """Returns extra static local variables to be made to transformed code.

    Subclasses must override this.

    Returns:
      extra_locals: A Dict[Text, Any] containing additional variables to make
        available to the transformed code.
    """
    def get_caching_key(self, user_context) -> None:
        """Returns a unique key to use for caching.

    Subclasses must override this.

    Calls made to `transform_function` with functions that have the same code
    object and caching key will return a cached instance on subsequent
    invocations.

    Args:
      user_context: The context object which was passed to `transform`.

    Returns:
      extra_locals: A hashable.
    """
    def transform_function(self, fn, user_context):
        """Transforms a function. See GenericTranspiler.trasnform_function.

    This overload wraps the parent's `transform_function`, adding caching and
    facilities to instantiate the output as a Python object. It also
    adds facilities to make new symbols available to the generated Python code,
    visible as local variables - see `get_extra_locals`.

    Args:
      fn: A function or lambda.
      user_context: An opaque object (may be None) that is forwarded to
        transform_ast, through the ctx.user attribute.
    Returns:
      A tuple:
        * A function or lambda with the same signature and closure as `fn`
        * The temporary module into which the transformed function was loaded
        * The source map as a
            Dict[origin_info.LineLocation, origin_info.OriginInfo]
    """
