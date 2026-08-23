from _typeshed import Incomplete
from sympy.physics.quantum.operator import HermitianOperator
from sympy.physics.quantum.state import Bra, Ket, State

__all__ = ['XOp', 'YOp', 'ZOp', 'PxOp', 'X', 'Y', 'Z', 'Px', 'XKet', 'XBra', 'PxKet', 'PxBra', 'PositionState3D', 'PositionKet3D', 'PositionBra3D']

class XOp(HermitianOperator):
    """1D cartesian position operator."""
    @classmethod
    def default_args(self): ...

class YOp(HermitianOperator):
    """ Y cartesian coordinate operator (for 2D or 3D systems) """
    @classmethod
    def default_args(self): ...

class ZOp(HermitianOperator):
    """ Z cartesian coordinate operator (for 3D systems) """
    @classmethod
    def default_args(self): ...

class PxOp(HermitianOperator):
    """1D cartesian momentum operator."""
    @classmethod
    def default_args(self): ...

X: Incomplete
Y: Incomplete
Z: Incomplete
Px: Incomplete

class XKet(Ket):
    """1D cartesian position eigenket."""
    @classmethod
    def default_args(self): ...
    @classmethod
    def dual_class(self): ...
    @property
    def position(self):
        """The position of the state."""

class XBra(Bra):
    """1D cartesian position eigenbra."""
    @classmethod
    def default_args(self): ...
    @classmethod
    def dual_class(self): ...
    @property
    def position(self):
        """The position of the state."""

class PositionState3D(State):
    """ Base class for 3D cartesian position eigenstates """
    @classmethod
    def default_args(self): ...
    @property
    def position_x(self):
        """ The x coordinate of the state """
    @property
    def position_y(self):
        """ The y coordinate of the state """
    @property
    def position_z(self):
        """ The z coordinate of the state """

class PositionKet3D(Ket, PositionState3D):
    """ 3D cartesian position eigenket """
    @classmethod
    def dual_class(self): ...

class PositionBra3D(Bra, PositionState3D):
    """ 3D cartesian position eigenbra """
    @classmethod
    def dual_class(self): ...

class PxKet(Ket):
    """1D cartesian momentum eigenket."""
    @classmethod
    def default_args(self): ...
    @classmethod
    def dual_class(self): ...
    @property
    def momentum(self):
        """The momentum of the state."""

class PxBra(Bra):
    """1D cartesian momentum eigenbra."""
    @classmethod
    def default_args(self): ...
    @classmethod
    def dual_class(self): ...
    @property
    def momentum(self):
        """The momentum of the state."""
