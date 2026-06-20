import functools
from _typeshed import Incomplete
from collections.abc import Hashable, Iterable
from dataclasses import dataclass
from jax._src import traceback_util as traceback_util
from jax._src.lib import pytree as pytree
from jax._src.util import safe_zip as safe_zip, unzip2 as unzip2
from typing import Any, Callable, NamedTuple, Type, TypeVar, overload

T = TypeVar('T')
U = TypeVar('U', bound=type[Any])
H = TypeVar('H', bound=Hashable)
Leaf = Any
PyTreeDef: Incomplete
default_registry: Incomplete
dispatch_registry: Incomplete

def tree_flatten(tree: Any, is_leaf: Callable[[Any], bool] | None = None) -> tuple[list[Leaf], PyTreeDef]:
    """Flattens a pytree.

  The flattening order (i.e. the order of elements in the output list)
  is deterministic, corresponding to a left-to-right depth-first tree
  traversal.

  Args:
    tree: a pytree to flatten.
    is_leaf: an optionally specified function that will be called at each
      flattening step. It should return a boolean, with true stopping the
      traversal and the whole subtree being treated as a leaf, and false
      indicating the flattening should traverse the current object.

  Returns:
    A pair where the first element is a list of leaf values and the second
    element is a treedef representing the structure of the flattened tree.
  """
def tree_unflatten(treedef: PyTreeDef, leaves: Iterable[Leaf]) -> Any:
    """Reconstructs a pytree from the treedef and the leaves.

  The inverse of :func:`tree_flatten`.

  Args:
    treedef: the treedef to reconstruct
    leaves: the iterable of leaves to use for reconstruction. The iterable must
      match the leaves of the treedef.

  Returns:
    The reconstructed pytree, containing the ``leaves`` placed in the structure
    described by ``treedef``.
  """
def tree_leaves(tree: Any, is_leaf: Callable[[Any], bool] | None = None) -> list[Leaf]:
    """Gets the leaves of a pytree."""
def tree_structure(tree: Any, is_leaf: None | Callable[[Any], bool] = None) -> PyTreeDef:
    """Gets the treedef for a pytree."""
def treedef_tuple(treedefs: Iterable[PyTreeDef]) -> PyTreeDef:
    """Makes a tuple treedef from an iterable of child treedefs."""
def treedef_children(treedef: PyTreeDef) -> list[PyTreeDef]: ...
def treedef_is_leaf(treedef: PyTreeDef) -> bool: ...
def treedef_is_strict_leaf(treedef: PyTreeDef) -> bool: ...
def all_leaves(iterable: Iterable[Any], is_leaf: Callable[[Any], bool] | None = None) -> bool:
    '''Tests whether all elements in the given iterable are all leaves.

  >>> tree = {"a": [1, 2, 3]}
  >>> assert all_leaves(jax.tree_util.tree_leaves(tree))
  >>> assert not all_leaves([tree])

  This function is useful in advanced cases, for example if a library allows
  arbitrary map operations on a flat iterable of leaves it may want to check
  if the result is still a flat iterable of leaves.

  Args:
    iterable: Iterable of leaves.

  Returns:
    A boolean indicating if all elements in the input are leaves.
  '''
def register_pytree_node(nodetype: type[T], flatten_func: Callable[[T], tuple[_Children, _AuxData]], unflatten_func: Callable[[_AuxData, _Children], T]):
    """Extends the set of types that are considered internal nodes in pytrees.

  See :ref:`example usage <pytrees>`.

  Args:
    nodetype: a Python type to treat as an internal pytree node.
    flatten_func: a function to be used during flattening, taking a value of
      type ``nodetype`` and returning a pair, with (1) an iterable for the
      children to be flattened recursively, and (2) some hashable auxiliary data
      to be stored in the treedef and to be passed to the ``unflatten_func``.
    unflatten_func: a function taking two arguments: the auxiliary data that was
      returned by ``flatten_func`` and stored in the treedef, and the
      unflattened children. The function should return an instance of
      ``nodetype``.
  """
def register_pytree_node_class(cls) -> U:
    """Extends the set of types that are considered internal nodes in pytrees.

  This function is a thin wrapper around ``register_pytree_node``, and provides
  a class-oriented interface::

    @register_pytree_node_class
    class Special:
      def __init__(self, x, y):
        self.x = x
        self.y = y
      def tree_flatten(self):
        return ((self.x, self.y), None)
      @classmethod
      def tree_unflatten(cls, aux_data, children):
        return cls(*children)
  """
def tree_map(f: Callable[..., Any], tree: Any, *rest: Any, is_leaf: Callable[[Any], bool] | None = None) -> Any:
    '''Maps a multi-input function over pytree args to produce a new pytree.

  Args:
    f: function that takes ``1 + len(rest)`` arguments, to be applied at the
      corresponding leaves of the pytrees.
    tree: a pytree to be mapped over, with each leaf providing the first
      positional argument to ``f``.
    rest: a tuple of pytrees, each of which has the same structure as ``tree``
      or has ``tree`` as a prefix.
    is_leaf: an optionally specified function that will be called at each
      flattening step. It should return a boolean, which indicates whether the
      flattening should traverse the current object, or if it should be stopped
      immediately, with the whole subtree being treated as a leaf.

  Returns:
    A new pytree with the same structure as ``tree`` but with the value at each
    leaf given by ``f(x, *xs)`` where ``x`` is the value at the corresponding
    leaf in ``tree`` and ``xs`` is the tuple of values at corresponding nodes in
    ``rest``.

  Examples:

    >>> import jax.tree_util
    >>> jax.tree_util.tree_map(lambda x: x + 1, {"x": 7, "y": 42})
    {\'x\': 8, \'y\': 43}

    If multiple inputs are passed, the structure of the tree is taken from the
    first input; subsequent inputs need only have ``tree`` as a prefix:

    >>> jax.tree_util.tree_map(lambda x, y: [x] + y, [5, 6], [[7, 9], [1, 2]])
    [[5, 7, 9], [6, 1, 2]]
  '''
def build_tree(treedef: PyTreeDef, xs: Any) -> Any: ...
def tree_transpose(outer_treedef: PyTreeDef, inner_treedef: PyTreeDef, pytree_to_transpose: Any) -> Any:
    """Transform a tree having tree structure (outer, inner) into one having structure

  (inner, outer).
  """

class _RegistryEntry(NamedTuple):
    to_iter: Incomplete
    from_iter: Incomplete

no_initializer: Incomplete

@overload
def tree_reduce(function: Callable[[T, Any], T], tree: Any, *, is_leaf: Callable[[Any], bool] | None = None) -> T: ...
@overload
def tree_reduce(function: Callable[[T, Any], T], tree: Any, initializer: T, is_leaf: Callable[[Any], bool] | None = None) -> T: ...
def tree_all(tree: Any) -> bool: ...

class _HashableCallableShim:
    """Object that delegates __call__, __hash__, and __eq__ to another object."""
    fun: Incomplete
    def __init__(self, fun) -> None: ...
    def __call__(self, *args, **kw): ...
    def __hash__(self): ...
    def __eq__(self, other): ...

class Partial(functools.partial):
    """A version of functools.partial that works in pytrees.

  Use it for partial function evaluation in a way that is compatible with JAX's
  transformations, e.g., ``Partial(func, *args, **kwargs)``.

  (You need to explicitly opt-in to this behavior because we didn't want to give
  functools.partial different semantics than normal function closures.)

  For example, here is a basic usage of ``Partial`` in a manner similar to
  ``functools.partial``:

  >>> import jax.numpy as jnp
  >>> add_one = Partial(jnp.add, 1)
  >>> add_one(2)
  Array(3, dtype=int32, weak_type=True)

  Pytree compatibility means that the resulting partial function can be passed
  as an argument within transformed JAX functions, which is not possible with a
  standard ``functools.partial`` function:

  >>> from jax import jit
  >>> @jit
  ... def call_func(f, *args):
  ...   return f(*args)
  ...
  >>> call_func(add_one, 2)
  Array(3, dtype=int32, weak_type=True)

  Passing zero arguments to ``Partial`` effectively wraps the original function,
  making it a valid argument in JAX transformed functions:

  >>> call_func(Partial(jnp.add), 1, 2)
  Array(3, dtype=int32, weak_type=True)

  Had we passed ``jnp.add`` to ``call_func`` directly, it would have resulted in
  a
  ``TypeError``.

  Note that if the result of ``Partial`` is used in the context where the
  value is traced, it results in all bound arguments being traced when passed
  to the partially-evaluated function:

  >>> print_zero = Partial(print, 0)
  >>> print_zero()
  0
  >>> call_func(print_zero)  # doctest:+ELLIPSIS
  Traced<ShapedArray(int32[], weak_type=True)>with<DynamicJaxprTrace...>
  """
    def __new__(klass, func, *args, **kw): ...

def broadcast_prefix(prefix_tree: Any, full_tree: Any, is_leaf: Callable[[Any], bool] | None = None) -> list[Any]: ...
def flatten_one_level(pytree: Any) -> tuple[list[Any], Hashable]:
    """Flatten the given pytree node by one level.

  Args:
    pytree: A valid pytree node, either built-in or registered via
      ``register_pytree_node`` or ``register_pytree_with_keys``.

  Returns:
    A pair of the pytree's flattened children and its hashable metadata.

  Raises:
    ValueError: If the given pytree is not a built-in or registered container
    via ``register_pytree_node`` or ``register_pytree_with_keys``.
  """
def prefix_errors(prefix_tree: Any, full_tree: Any, is_leaf: Callable[[Any], bool] | None = None) -> list[Callable[[str], ValueError]]: ...
def equality_errors(tree1: Any, tree2: Any, is_leaf: Callable[[Any], bool] | None = None) -> Iterable[tuple[KeyPath, str, str, str]]:
    '''Helper to describe structural differences between two pytrees.

  Args:
    tree1, tree2: pytrees to compare.

  Usage:

    raise Exception(
        "Value 1 and value 2 must have the same pytree structure, but they have "
        "the following structural differences:
" +
        ("
".join(
           f"   - {keystr(path)} is a {thing1} in value 1 and a {thing2} in "
           f" value 2, so {explanation}.
"
           for path, thing1, thing2, explanation
           in equality_errors(val1, val2))))
  '''

class _DeprecatedKeyPathEntry(NamedTuple):
    key: Any
    def pprint(self) -> str: ...

class GetitemKeyPathEntry(_DeprecatedKeyPathEntry):
    def pprint(self) -> str: ...

class AttributeKeyPathEntry(_DeprecatedKeyPathEntry):
    def pprint(self) -> str: ...

@dataclass(frozen=True)
class SequenceKey:
    idx: int
    def __init__(self, idx) -> None: ...

@dataclass(frozen=True)
class DictKey:
    key: Hashable
    def __init__(self, key) -> None: ...

@dataclass(frozen=True)
class GetAttrKey:
    name: str
    def __init__(self, name) -> None: ...

@dataclass(frozen=True)
class FlattenedIndexKey:
    key: int
    def __init__(self, key) -> None: ...
BuiltInKeyEntry = SequenceKey | DictKey | GetAttrKey | FlattenedIndexKey
KeyEntry = TypeVar('KeyEntry', bound=Hashable)
KeyPath = tuple[KeyEntry, ...]

def keystr(keys: KeyPath):
    """Helper to pretty-print a tuple of keys.

  Args:
    keys: A tuple of ``KeyEntry`` or any class that can be converted to string.

  Returns:
    A string that joins all string representations of the keys.
  """

class _RegistryWithKeypathsEntry(NamedTuple):
    flatten_with_keys: Callable[..., Any]
    unflatten_func: Callable[..., Any]

def register_keypaths(ty: type[T], handler: Callable[[T], tuple[KeyEntry, ...]]) -> None:
    """[Deprecated] Register the method to get keypaths for type.

  Please use ``register_pytree_with_keys`` instead.

  Only works if the type was already registered with ``register_pytree_node``.
  """
def register_pytree_with_keys(nodetype: type[T], flatten_with_keys: Callable[[T], tuple[Iterable[tuple[KeyEntry, Any]], _AuxData]], unflatten_func: Callable[[_AuxData, Iterable[Any]], T], flatten_func: None | Callable[[T], tuple[Iterable[Any], _AuxData]] = None):
    """Extends the set of types that are considered internal nodes in pytrees.

  This is a more powerful alternative to ``register_pytree_node`` that allows
  you to access each pytree leaf's key path when flattening and tree-mapping.

  Args:
    nodetype: a Python type to treat as an internal pytree node.
    flatten_with_keys: a function to be used during flattening, taking a value
      of type ``nodetype`` and returning a pair, with (1) an iterable for tuples
      of each key path and its child, and (2) some hashable auxiliary data to be
      stored in the treedef and to be passed to the ``unflatten_func``.
    unflatten_func: a function taking two arguments: the auxiliary data that was
      returned by ``flatten_func`` and stored in the treedef, and the
      unflattened children. The function should return an instance of
      ``nodetype``.
    flatten_func: an optional function similar to ``flatten_with_keys``, but
      returns only children and auxiliary data. It must return the children
      in the same order as ``flatten_with_keys``, and return the same aux data.
      This argument is optional and only needed for faster traversal when
      calling functions without keys like ``tree_map`` and ``tree_flatten``.
  """
def register_pytree_with_keys_class(cls) -> U:
    """Extends the set of types that are considered internal nodes in pytrees.

  This function is similar to ``register_pytree_node_class``, but requires a
  class that defines how it could be flattened with keys.

  It is a thin wrapper around ``register_pytree_with_keys``, and
  provides a class-oriented interface::

    @register_pytree_with_keys_class
    class Special:
      def __init__(self, x, y):
        self.x = x
        self.y = y
      def tree_flatten_with_keys(self):
        return (((GetAttrKey('x'), self.x), (GetAttrKey('y'), self.y)), None)
      @classmethod
      def tree_unflatten(cls, aux_data, children):
        return cls(*children)
  """
def register_static(cls) -> Type[H]:
    """Registers `cls` as a pytree with no leaves.

  Instances are treated as static by `jax.jit`, `jax.pmap`, etc. This can be an
  alternative to labeling inputs as static using `jax.jit`'s `static_argnums`
  and `static_argnames` kwargs, `jax.pmap`'s `static_broadcasted_argnums`, etc.

  `cls` must be hashable, as defined in
  https://docs.python.org/3/glossary.html#term-hashable.

  `register_static` can be applied to subclasses of builtin hashable classes
  such as `str`, like this:
  ```
  @tree_util.register_static
  class StaticStr(str):
    pass
  ```
  """
def tree_flatten_with_path(tree: Any, is_leaf: Callable[[Any], bool] | None = None) -> tuple[list[tuple[KeyPath, Any]], PyTreeDef]:
    """Flattens a pytree like ``tree_flatten``, but also returns each leaf's key path.

  Args:
    tree: a pytree to flatten. If it contains a custom type, it must be
      registered with ``register_pytree_with_keys``.
  Returns:
    A pair which the first element is a list of key-leaf pairs, each of
    which contains a leaf and its key path. The second element is a treedef
    representing the structure of the flattened tree.
  """
def tree_leaves_with_path(tree: Any, is_leaf: Callable[[Any], bool] | None = None) -> list[tuple[KeyPath, Any]]:
    """Gets the leaves of a pytree like ``tree_leaves`` and returns each leaf's key path.

  Args:
    tree: a pytree. If it contains a custom type, it must be registered with
      ``register_pytree_with_keys``.
  Returns:
    A list of key-leaf pairs, each of which contains a leaf and its key path.
  """
def generate_key_paths(tree: Any, is_leaf: Callable[[Any], bool] | None = None) -> list[tuple[KeyPath, Any]]: ...
def tree_map_with_path(f: Callable[..., Any], tree: Any, *rest: Any, is_leaf: Callable[[Any], bool] | None = None) -> Any:
    """Maps a multi-input function over pytree key path and args to produce a new pytree.

  This is a more powerful alternative of ``tree_map`` that can take the key path
  of each leaf as input argument as well.

  Args:
    f: function that takes ``2 + len(rest)`` arguments, aka. the key path and
      each corresponding leaves of the pytrees.
    tree: a pytree to be mapped over, with each leaf's key path as the first
      positional argument and the leaf itself as the second argument to ``f``.
    *rest: a tuple of pytrees, each of which has the same structure as ``tree``
      or has ``tree`` as a prefix.

  Returns:
    A new pytree with the same structure as ``tree`` but with the value at each
    leaf given by ``f(kp, x, *xs)`` where ``kp`` is the key path of the leaf at
    the corresponding leaf in ``tree``, ``x`` is the leaf value and ``xs`` is
    the tuple of values at corresponding nodes in ``rest``.
  """
