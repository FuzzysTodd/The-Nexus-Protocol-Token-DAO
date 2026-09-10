from .cloudpickle import CellType as CellType, DEFAULT_PROTOCOL as DEFAULT_PROTOCOL, PYPY as PYPY, builtin_code_type as builtin_code_type, cell_set as cell_set, dynamic_subimport as dynamic_subimport, parametrized_type_hint_getinitargs as parametrized_type_hint_getinitargs, subimport as subimport
from .compat import Pickler as Pickler, pickle as pickle
from _typeshed import Incomplete

def dump(obj, file, protocol: Incomplete | None = None, buffer_callback: Incomplete | None = None) -> None:
    """Serialize obj as bytes streamed into file

        protocol defaults to cloudpickle.DEFAULT_PROTOCOL which is an alias to
        pickle.HIGHEST_PROTOCOL. This setting favors maximum communication
        speed between processes running the same Python version.

        Set protocol=pickle.DEFAULT_PROTOCOL instead if you need to ensure
        compatibility with older versions of Python.
        """
def dumps(obj, protocol: Incomplete | None = None, buffer_callback: Incomplete | None = None):
    """Serialize obj as a string of bytes allocated in memory

        protocol defaults to cloudpickle.DEFAULT_PROTOCOL which is an alias to
        pickle.HIGHEST_PROTOCOL. This setting favors maximum communication
        speed between processes running the same Python version.

        Set protocol=pickle.DEFAULT_PROTOCOL instead if you need to ensure
        compatibility with older versions of Python.
        """

load: Incomplete
loads: Incomplete

class CloudPickler(Pickler):
    dispatch_table: Incomplete
    def dump(self, obj): ...
    globals_ref: Incomplete
    proto: Incomplete
    def __init__(self, file, protocol: Incomplete | None = None, buffer_callback: Incomplete | None = None) -> None: ...
    def __init__(self, file, protocol: Incomplete | None = None) -> None: ...
    dispatch = dispatch_table
    def reducer_override(self, obj):
        """Type-agnostic reducing callback for function and classes.

            For performance reasons, subclasses of the C _pickle.Pickler class
            cannot register custom reducers for functions and classes in the
            dispatch_table. Reducer for such types must instead implemented in
            the special reducer_override method.

            Note that method will be called for any object except a few
            builtin-types (int, lists, dicts etc.), which differs from reducers
            in the Pickler's dispatch_table, each of them being invoked for
            objects of a specific type only.

            This property comes in handy for classes: although most classes are
            instances of the ``type`` metaclass, some of them can be instances
            of other custom metaclasses (such as enum.EnumMeta for example). In
            particular, the metaclass will likely not be known in advance, and
            thus cannot be special-cased using an entry in the dispatch_table.
            reducer_override, among other things, allows us to register a
            reducer that will be called for any class, independently of its
            type.


            Notes:

            * reducer_override has the priority over dispatch_table-registered
            reducers.
            * reducer_override can be used to fix other limitations of
              cloudpickle for other types that suffered from type-specific
              reducers, such as Exceptions. See
              https://github.com/cloudpipe/cloudpickle/issues/248
            """
    def save_global(self, obj, name: Incomplete | None = None, pack=...):
        '''
            Save a "global".

            The name of this method is somewhat misleading: all types get
            dispatched here.
            '''
    def save_function(self, obj, name: Incomplete | None = None):
        """ Registered with the dispatch to handle all function types.

            Determines what kind of function obj is (e.g. lambda, defined at
            interactive prompt, etc) and handles the pickling appropriately.
            """
    def save_pypy_builtin_func(self, obj) -> None:
        """Save pypy equivalent of builtin functions.
            PyPy does not have the concept of builtin-functions. Instead,
            builtin-functions are simple function instances, but with a
            builtin-code attribute.
            Most of the time, builtin functions should be pickled by attribute.
            But PyPy has flaky support for __qualname__, so some builtin
            functions such as float.__new__ will be classified as dynamic. For
            this reason only, we created this special routine. Because
            builtin-functions are not expected to have closure or globals,
            there is no additional hack (compared the one already implemented
            in pickle) to protect ourselves from reference cycles. A simple
            (reconstructor, newargs, obj.__dict__) tuple is save_reduced.  Note
            also that PyPy improved their support for __qualname__ in v3.6, so
            this routing should be removed when cloudpickle supports only PyPy
            3.6 and later.
            """
