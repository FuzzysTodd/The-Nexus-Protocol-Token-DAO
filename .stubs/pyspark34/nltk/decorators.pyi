__all__ = ['decorator', 'new_wrapper', 'getinfo']

def getinfo(func):
    '''
    Returns an info dictionary containing:
    - name (the name of the function : str)
    - argnames (the names of the arguments : list)
    - defaults (the values of the default arguments : tuple)
    - signature (the signature : str)
    - fullsignature (the full signature : Signature)
    - doc (the docstring : str)
    - module (the module name : str)
    - dict (the function __dict__ : str)

    >>> def f(self, x=1, y=2, *args, **kw): pass

    >>> info = getinfo(f)

    >>> info["name"]
    \'f\'
    >>> info["argnames"]
    [\'self\', \'x\', \'y\', \'args\', \'kw\']

    >>> info["defaults"]
    (1, 2)

    >>> info["signature"]
    \'self, x, y, *args, **kw\'

    >>> info["fullsignature"]
    <Signature (self, x=1, y=2, *args, **kw)>
    '''
def new_wrapper(wrapper, model):
    """
    An improvement over functools.update_wrapper. The wrapper is a generic
    callable object. It works by generating a copy of the wrapper with the
    right signature and by updating the copy, not the original.
    Moreovoer, 'model' can be a dictionary with keys 'name', 'doc', 'module',
    'dict', 'defaults'.
    """
def decorator(caller):
    '''
    General purpose decorator factory: takes a caller function as
    input and returns a decorator with the same attributes.
    A caller function is any function like this::

     def caller(func, *args, **kw):
         # do something
         return func(*args, **kw)

    Here is an example of usage:

    >>> @decorator
    ... def chatty(f, *args, **kw):
    ...     print("Calling %r" % f.__name__)
    ...     return f(*args, **kw)

    >>> chatty.__name__
    \'chatty\'

    >>> @chatty
    ... def f(): pass
    ...
    >>> f()
    Calling \'f\'

    decorator can also take in input a class with a .caller method; in this
    case it converts the class into a factory of callable decorator objects.
    See the documentation for an example.
    '''
