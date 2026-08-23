from _typeshed import Incomplete
from numba import njit as njit
from numba.core import cgutils as cgutils, errors as errors, imputils as imputils, types as types, utils as utils
from numba.core.datamodel import default_manager as default_manager, models as models
from numba.core.registry import cpu_target as cpu_target
from numba.core.serialize import disable_pickling as disable_pickling
from numba.core.typing import templates as templates
from numba.core.typing.asnumbatype import as_numba_type as as_numba_type

class InstanceModel(models.StructModel):
    def __init__(self, dmm, fe_typ) -> None: ...

class InstanceDataModel(models.StructModel):
    def __init__(self, dmm, fe_typ) -> None: ...

class JitClassType(type):
    """
    The type of any jitclass.
    """
    def __new__(cls, name, bases, dct): ...
    def __instancecheck__(cls, instance): ...
    def __call__(cls, *args, **kwargs): ...

def register_class_type(cls, spec, class_ctor, builder):
    """
    Internal function to create a jitclass.

    Args
    ----
    cls: the original class object (used as the prototype)
    spec: the structural specification contains the field types.
    class_ctor: the numba type to represent the jitclass
    builder: the internal jitclass builder
    """

class ConstructorTemplate(templates.AbstractTemplate):
    """
    Base class for jitclass constructor templates.
    """
    def generic(self, args, kws): ...

class ClassBuilder:
    """
    A jitclass builder for a mutable jitclass.  This will register
    typing and implementation hooks to the given typing and target contexts.
    """
    class_impl_registry: Incomplete
    implemented_methods: Incomplete
    class_type: Incomplete
    typingctx: Incomplete
    targetctx: Incomplete
    def __init__(self, class_type, typingctx, targetctx) -> None: ...
    def register(self) -> None:
        """
        Register to the frontend and backend.
        """

class ClassAttribute(templates.AttributeTemplate):
    key = types.ClassInstanceType
    def generic_resolve(self, instance, attr): ...

def get_attr_impl(context, builder, typ, value, attr):
    """
    Generic getattr() for @jitclass instances.
    """
def set_attr_impl(context, builder, sig, args, attr) -> None:
    """
    Generic setattr() for @jitclass instances.
    """
def imp_dtor(context, module, instance_type): ...
def ctor_impl(context, builder, sig, args):
    """
    Generic constructor (__new__) for jitclasses.
    """
