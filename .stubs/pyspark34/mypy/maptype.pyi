from mypy.expandtype import expand_type as expand_type
from mypy.nodes import TypeInfo as TypeInfo
from mypy.types import AnyType as AnyType, Instance as Instance, TupleType as TupleType, Type as Type, TypeOfAny as TypeOfAny, TypeVarId as TypeVarId, has_type_vars as has_type_vars

def map_instance_to_supertype(instance: Instance, superclass: TypeInfo) -> Instance:
    """Produce a supertype of `instance` that is an Instance
    of `superclass`, mapping type arguments up the chain of bases.

    If `superclass` is not a nominal superclass of `instance.type`,
    then all type arguments are mapped to 'Any'.
    """
def map_instance_to_supertypes(instance: Instance, supertype: TypeInfo) -> list[Instance]: ...
def class_derivation_paths(typ: TypeInfo, supertype: TypeInfo) -> list[list[TypeInfo]]:
    """Return an array of non-empty paths of direct base classes from
    type to supertype.  Return [] if no such path could be found.

      InterfaceImplementationPaths(A, B) == [[B]] if A inherits B
      InterfaceImplementationPaths(A, C) == [[B, C]] if A inherits B and
                                                        B inherits C
    """
def map_instance_to_direct_supertypes(instance: Instance, supertype: TypeInfo) -> list[Instance]: ...
def instance_to_type_environment(instance: Instance) -> dict[TypeVarId, Type]:
    """Given an Instance, produce the resulting type environment for type
    variables bound by the Instance's class definition.

    An Instance is a type application of a class (a TypeInfo) to its
    required number of type arguments.  So this environment consists
    of the class's type variables mapped to the Instance's actual
    arguments.  The type variables are mapped by their `id`.

    """
