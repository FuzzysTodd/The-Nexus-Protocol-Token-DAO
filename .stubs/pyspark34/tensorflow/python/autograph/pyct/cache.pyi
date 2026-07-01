class _TransformedFnCache:
    """Generic hierarchical cache for transformed functions.

  The keys are soft references (i.e. they are discarded when the key is
  destroyed) created from the source function by `_get_key`. The subkeys are
  strong references and can be any value. Typically they identify different
  kinds of transformation.
  """
    def __init__(self) -> None: ...
    def has(self, entity, subkey): ...
    def __getitem__(self, entity): ...
    def __len__(self) -> int: ...

class CodeObjectCache(_TransformedFnCache):
    """A function cache based on code objects.

  Code objects are good proxies for the source code of a function.

  This cache efficiently handles functions that share code objects, such as
  functions defined in a loop, bound methods, etc.

  The cache falls back to the function object, if it doesn't have a code object.
  """
class UnboundInstanceCache(_TransformedFnCache):
    """A function cache based on unbound function objects.

  Using the function for the cache key allows efficient handling of object
  methods.

  Unlike the _CodeObjectCache, this discriminates between different functions
  even if they have the same code. This is needed for decorators that may
  masquerade as another function.
  """
