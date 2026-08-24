from .dimensions import Dimension as Dimension
from _typeshed import Incomplete
from sympy.core.add import Add as Add
from sympy.core.function import Derivative as Derivative, Function as Function
from sympy.core.mul import Mul as Mul
from sympy.core.power import Pow as Pow
from sympy.core.singleton import S as S
from sympy.physics.units.dimensions import _QuantityMapper
from sympy.physics.units.quantities import Quantity as Quantity
from typing import Dict as tDict, Set as tSet

class UnitSystem(_QuantityMapper):
    """
    UnitSystem represents a coherent set of units.

    A unit system is basically a dimension system with notions of scales. Many
    of the methods are defined in the same way.

    It is much better if all base units have a symbol.
    """
    name: Incomplete
    descr: Incomplete
    def __init__(self, base_units, units=(), name: str = '', descr: str = '', dimension_system: Incomplete | None = None, derived_units: tDict[Dimension, Quantity] = {}) -> None: ...
    def extend(self, base, units=(), name: str = '', description: str = '', dimension_system: Incomplete | None = None, derived_units: tDict[Dimension, Quantity] = {}):
        """Extend the current system into a new one.

        Take the base and normal units of the current system to merge
        them to the base and normal units given in argument.
        If not provided, name and description are overridden by empty strings.
        """
    def get_dimension_system(self): ...
    def get_quantity_dimension(self, unit): ...
    def get_quantity_scale_factor(self, unit): ...
    @staticmethod
    def get_unit_system(unit_system): ...
    @staticmethod
    def get_default_unit_system(): ...
    @property
    def dim(self):
        """
        Give the dimension of the system.

        That is return the number of units forming the basis.
        """
    @property
    def is_consistent(self):
        """
        Check if the underlying dimension system is consistent.
        """
    @property
    def derived_units(self) -> tDict[Dimension, Quantity]: ...
    def get_dimensional_expr(self, expr): ...
    def get_units_non_prefixed(self) -> tSet[Quantity]:
        """
        Return the units of the system that do not have a prefix.
        """
