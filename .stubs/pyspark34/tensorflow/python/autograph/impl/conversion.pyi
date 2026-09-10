from tensorflow.python.autograph.core import config as config
from tensorflow.python.autograph.pyct import cache as cache, inspect_utils as inspect_utils
from tensorflow.python.eager import function as function
from tensorflow.python.util import tf_inspect as tf_inspect

def is_unsupported(o):
    """Checks whether an entity is supported by AutoGraph at all."""
def is_allowlisted(o, check_call_override: bool = True, allow_namedtuple_subclass: bool = False):
    """Checks whether an entity is allowed for use in graph mode.

  Examples of allowed entities include all members of the tensorflow
  package.

  Args:
    o: A Python entity.
    check_call_override: Reserved for internal use. When set to `False`, it
      disables the rule according to which classes are allowed if their
      __call__ method is allowed.
    allow_namedtuple_subclass: Reserved for internal use. When `True`,
      namedtuple subclasses are not allowed.

  Returns:
    Boolean
  """
def is_in_allowlist_cache(entity, options): ...
def cache_allowlisted(entity, options) -> None: ...
