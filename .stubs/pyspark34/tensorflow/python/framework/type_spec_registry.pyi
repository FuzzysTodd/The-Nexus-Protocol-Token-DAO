from tensorflow.python.types import internal as internal

def register(name):
    '''Decorator used to register a globally unique name for a TypeSpec subclass.

  Args:
    name: The name of the type spec.  Must be globally unique.  Must have the
      form `"{project_name}.{type_name}"`.  E.g. `"my_project.MyTypeSpec"`.

  Returns:
    A class decorator that registers the decorated class with the given name.
  '''
def get_name(cls):
    """Returns the registered name for TypeSpec `cls`."""
def lookup(name):
    """Returns the TypeSpec that has been registered with name `name`."""
