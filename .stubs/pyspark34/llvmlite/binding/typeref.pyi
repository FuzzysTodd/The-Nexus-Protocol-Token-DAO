import enum
from llvmlite.binding import ffi as ffi

class TypeKind(enum.IntEnum):
    void: int
    half: int
    float: int
    double: int
    x86_fp80: int
    fp128: int
    ppc_fp128: int
    label: int
    integer: int
    function: int
    struct: int
    array: int
    pointer: int
    vector: int
    metadata: int
    x86_mmx: int
    token: int
    scalable_vector: int
    bfloat: int
    x86_amx: int

class TypeRef(ffi.ObjectRef):
    """A weak reference to a LLVM type
    """
    @property
    def name(self):
        """
        Get type name
        """
    @property
    def is_struct(self):
        """
        Returns true if the type is a struct type.
        """
    @property
    def is_pointer(self):
        """
        Returns true if the type is a pointer type.
        """
    @property
    def is_array(self):
        """
        Returns true if the type is an array type.
        """
    @property
    def is_vector(self):
        """
        Returns true if the type is a vector type.
        """
    @property
    def is_function_vararg(self):
        """
        Returns true if a function type accepts a variable number of arguments.
        When the type is not a function, raises exception.
        """
    @property
    def elements(self):
        """
        Returns iterator over enclosing types
        """
    @property
    def element_type(self):
        """
        Returns the pointed-to type. When the type is not a pointer,
        raises exception.
        """
    @property
    def element_count(self):
        """
        Returns the number of elements in an array or a vector. For scalable
        vectors, returns minimum number of elements. When the type is neither
        an array nor a vector, raises exception.
        """
    @property
    def type_width(self):
        """
        Return the basic size of this type if it is a primitive type. These are
        fixed by LLVM and are not target-dependent.
        This will return zero if the type does not have a size or is not a
        primitive type.

        If this is a scalable vector type, the scalable property will be set and
        the runtime size will be a positive integer multiple of the base size.

        Note that this may not reflect the size of memory allocated for an
        instance of the type or the number of bytes that are written when an
        instance of the type is stored to memory.
        """
    @property
    def type_kind(self):
        """
        Returns the LLVMTypeKind enumeration of this type.
        """

class _TypeIterator(ffi.ObjectRef):
    def __next__(self): ...
    next = __next__
    def __iter__(self): ...

class _TypeListIterator(_TypeIterator): ...
