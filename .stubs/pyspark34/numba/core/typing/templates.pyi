import abc
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from collections.abc import Generator
from numba.core import targetconfig as targetconfig, types as types, utils as utils
from numba.core.cpu_options import InlineOptions as InlineOptions
from numba.core.errors import InternalError as InternalError, InternalTargetMismatchError as InternalTargetMismatchError, TypingError as TypingError
from typing import NamedTuple

class _inline_info(NamedTuple):
    func_ir: Incomplete
    typemap: Incomplete
    calltypes: Incomplete
    signature: Incomplete

class Signature:
    """
    The signature of a function call or operation, i.e. its argument types
    and return type.
    """
    def __init__(self, return_type, args, recvr, pysig: Incomplete | None = None) -> None: ...
    @property
    def return_type(self): ...
    @property
    def args(self): ...
    @property
    def recvr(self): ...
    @property
    def pysig(self): ...
    def replace(self, **kwargs):
        """Copy and replace the given attributes provided as keyword arguments.
        Returns an updated copy.
        """
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    @property
    def is_method(self):
        """
        Whether this signature represents a bound method or a regular
        function.
        """
    def as_method(self):
        """
        Convert this signature to a bound method signature.
        """
    def as_function(self):
        """
        Convert this signature to a regular function signature.
        """
    def as_type(self):
        """
        Convert this signature to a first-class function type.
        """
    def __unliteral__(self): ...
    def dump(self, tab: str = '') -> None: ...
    def is_precise(self): ...

def make_concrete_template(name, key, signatures): ...
def make_callable_template(key, typer, recvr: Incomplete | None = None):
    """
    Create a callable template with the given key and typer function.
    """
def signature(return_type, *args, **kws): ...
def fold_arguments(pysig, args, kws, normal_handler, default_handler, stararg_handler):
    '''
    Given the signature *pysig*, explicit *args* and *kws*, resolve
    omitted arguments and keyword arguments. A tuple of positional
    arguments is returned.
    Various handlers allow to process arguments:
    - normal_handler(index, param, value) is called for normal arguments
    - default_handler(index, param, default) is called for omitted arguments
    - stararg_handler(index, param, values) is called for a "*args" argument
    '''

class FunctionTemplate(ABC, metaclass=abc.ABCMeta):
    unsafe_casting: bool
    exact_match_required: bool
    prefer_literal: bool
    metadata: Incomplete
    context: Incomplete
    def __init__(self, context) -> None: ...
    def get_impl_key(self, sig):
        """
        Return the key for looking up the implementation for the given
        signature on the target context.
        """
    @classmethod
    def get_source_code_info(cls, impl):
        """
        Gets the source information about function impl.
        Returns:

        code - str: source code as a string
        firstlineno - int: the first line number of the function impl
        path - str: the path to file containing impl

        if any of the above are not available something generic is returned
        """
    @abstractmethod
    def get_template_info(self):
        '''
        Returns a dictionary with information specific to the template that will
        govern how error messages are displayed to users. The dictionary must
        be of the form:
        info = {
            \'kind\': "unknown", # str: The kind of template, e.g. "Overload"
            \'name\': "unknown", # str: The name of the source function
            \'sig\': "unknown",  # str: The signature(s) of the source function
            \'filename\': "unknown", # str: The filename of the source function
            \'lines\': ("start", "end"), # tuple(int, int): The start and
                                         end line of the source function.
            \'docstring\': "unknown" # str: The docstring of the source function
        }
        '''

class AbstractTemplate(FunctionTemplate):
    """
    Defines method ``generic(self, args, kws)`` which compute a possible
    signature base on input types.  The signature does not have to match the
    input types. It is compared against the input types afterwards.
    """
    def apply(self, args, kws): ...
    def get_template_info(self): ...

class CallableTemplate(FunctionTemplate):
    """
    Base class for a template defining a ``generic(self)`` method
    returning a callable to be called with the actual ``*args`` and
    ``**kwargs`` representing the call signature.  The callable has
    to return a return type, a full signature, or None.  The signature
    does not have to match the input types. It is compared against the
    input types afterwards.
    """
    recvr: Incomplete
    def apply(self, args, kws): ...
    def get_template_info(self): ...

class ConcreteTemplate(FunctionTemplate):
    '''
    Defines attributes "cases" as a list of signature to match against the
    given input types.
    '''
    def apply(self, args, kws): ...
    def get_template_info(self): ...

class _EmptyImplementationEntry(InternalError):
    def __init__(self, reason) -> None: ...

class _OverloadFunctionTemplate(AbstractTemplate):
    """
    A base class of templates for overload functions.
    """
    def generic(self, args, kws):
        """
        Type the overloaded function by compiling the appropriate
        implementation for the given args.
        """
    def get_impl_key(self, sig):
        """
        Return the key for looking up the implementation for the given
        signature on the target context.
        """
    @classmethod
    def get_source_info(cls):
        '''Return a dictionary with information about the source code of the
        implementation.

        Returns
        -------
        info : dict
            - "kind" : str
                The implementation kind.
            - "name" : str
                The name of the function that provided the definition.
            - "sig" : str
                The formatted signature of the function.
            - "filename" : str
                The name of the source file.
            - "lines": tuple (int, int)
                First and list line number.
            - "docstring": str
                The docstring of the definition.
        '''
    def get_template_info(self): ...

def make_overload_template(func, overload_func, jit_options, strict, inline, prefer_literal: bool = False, **kwargs):
    """
    Make a template class for function *func* overloaded by *overload_func*.
    Compiler options are passed as a dictionary to *jit_options*.
    """

class _TemplateTargetHelperMixin:
    """Mixin for helper methods that assist with target/registry resolution"""

class _IntrinsicTemplate(_TemplateTargetHelperMixin, AbstractTemplate):
    """
    A base class of templates for intrinsic definition
    """
    def generic(self, args, kws):
        """
        Type the intrinsic by the arguments.
        """
    def get_impl_key(self, sig):
        """
        Return the key for looking up the implementation for the given
        signature on the target context.
        """
    def get_template_info(self): ...

def make_intrinsic_template(handle, defn, name, kwargs):
    """
    Make a template class for a intrinsic handle *handle* defined by the
    function *defn*.  The *name* is used for naming the new template class.
    """

class AttributeTemplate:
    context: Incomplete
    def __init__(self, context) -> None: ...
    def resolve(self, value, attr): ...
    generic_resolve = NotImplemented

class _OverloadAttributeTemplate(_TemplateTargetHelperMixin, AttributeTemplate):
    """
    A base class of templates for @overload_attribute functions.
    """
    is_method: bool
    context: Incomplete
    def __init__(self, context) -> None: ...

class _OverloadMethodTemplate(_OverloadAttributeTemplate):
    """
    A base class of templates for @overload_method functions.
    """
    is_method: bool

def make_overload_attribute_template(typ, attr, overload_func, inline, prefer_literal: bool = False, base=..., **kwargs):
    """
    Make a template class for attribute *attr* of *typ* overloaded by
    *overload_func*.
    """
def make_overload_method_template(typ, attr, overload_func, inline, prefer_literal: bool = False, **kwargs):
    """
    Make a template class for method *attr* of *typ* overloaded by
    *overload_func*.
    """
def bound_function(template_key):
    '''
    Wrap an AttributeTemplate resolve_* method to allow it to
    resolve an instance method\'s signature rather than a instance attribute.
    The wrapped method must return the resolved method\'s signature
    according to the given self type, args, and keywords.

    It is used thusly:

        class ComplexAttributes(AttributeTemplate):
            @bound_function("complex.conjugate")
            def resolve_conjugate(self, ty, args, kwds):
                return ty

    *template_key* (e.g. "complex.conjugate" above) will be used by the
    target to look up the method\'s implementation, as a regular function.
    '''

class Registry:
    """
    A registry of typing declarations.  The registry stores such declarations
    for functions, attributes and globals.
    """
    functions: Incomplete
    attributes: Incomplete
    globals: Incomplete
    def __init__(self) -> None: ...
    def register(self, item): ...
    def register_attr(self, item): ...
    def register_global(self, val: Incomplete | None = None, typ: Incomplete | None = None, **kwargs):
        """
        Register the typing of a global value.
        Functional usage with a Numba type::
            register_global(value, typ)

        Decorator usage with a template class::
            @register_global(value, typing_key=None)
            class Template:
                ...
        """

class BaseRegistryLoader:
    '''
    An incremental loader for a registry.  Each new call to
    new_registrations() will iterate over the not yet seen registrations.

    The reason for this object is multiple:
    - there can be several contexts
    - each context wants to install all registrations
    - registrations can be added after the first installation, so contexts
      must be able to get the "new" installations

    Therefore each context maintains its own loaders for each existing
    registry, without duplicating the registries themselves.
    '''
    def __init__(self, registry) -> None: ...
    def new_registrations(self, name) -> Generator[Incomplete, None, None]: ...

class RegistryLoader(BaseRegistryLoader):
    """
    An incremental loader for a typing registry.
    """
    registry_items: Incomplete

builtin_registry: Incomplete
infer: Incomplete
infer_getattr: Incomplete
infer_global: Incomplete
