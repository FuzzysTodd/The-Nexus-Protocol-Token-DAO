def get_qualified_name(function): ...
def add_notice_to_docstring(doc, instructions, no_doc_str, suffix_str, notice, notice_type: str = 'Warning'):
    """Adds a deprecation notice to a docstring.

  Args:
    doc: The original docstring.
    instructions: A string, describing how to fix the problem.
    no_doc_str: The default value to use for `doc` if `doc` is empty.
    suffix_str: Is added to the end of the first line.
    notice: A list of strings. The main notice warning body.
    notice_type: The type of notice to use. Should be one of `[Caution,
    Deprecated, Important, Note, Warning]`

  Returns:
    A new docstring, with the notice attached.

  Raises:
    ValueError: If `notice` is empty.
  """
def validate_callable(func, decorator_name) -> None: ...

class classproperty:
    """Class property decorator.

  Example usage:

  class MyClass(object):

    @classproperty
    def value(cls):
      return '123'

  > print MyClass.value
  123
  """
    def __init__(self, func) -> None: ...
    def __get__(self, owner_self, owner_cls): ...

class _CachedClassProperty:
    '''Cached class property decorator.

  Transforms a class method into a property whose value is computed once
  and then cached as a normal attribute for the life of the class.  Example
  usage:

  >>> class MyClass(object):
  ...   @cached_classproperty
  ...   def value(cls):
  ...     print("Computing value")
  ...     return \'<property of %s>\' % cls.__name__
  >>> class MySubclass(MyClass):
  ...   pass
  >>> MyClass.value
  Computing value
  \'<property of MyClass>\'
  >>> MyClass.value  # uses cached value
  \'<property of MyClass>\'
  >>> MySubclass.value
  Computing value
  \'<property of MySubclass>\'

  This decorator is similar to `functools.cached_property`, but it adds a
  property to the class, not to individual instances.
  '''
    def __init__(self, func) -> None: ...
    def __get__(self, obj, objtype): ...
    def __set__(self, obj, value) -> None: ...
    def __delete__(self, obj) -> None: ...

def cached_classproperty(func): ...
