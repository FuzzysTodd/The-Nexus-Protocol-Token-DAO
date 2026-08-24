from _typeshed import Incomplete
from itertools import product as product
from numba.core import types as types
from numba.core.typing.templates import AbstractTemplate as AbstractTemplate, AttributeTemplate as AttributeTemplate, ConcreteTemplate as ConcreteTemplate, infer as infer, infer_getattr as infer_getattr, infer_global as infer_global, signature as signature
from numba.np import npdatetime_helpers as npdatetime_helpers

class TimedeltaUnaryOp(AbstractTemplate):
    def generic(self, args, kws): ...

class TimedeltaBinOp(AbstractTemplate):
    def generic(self, args, kws): ...

class TimedeltaCmpOp(AbstractTemplate):
    def generic(self, args, kws): ...

class TimedeltaOrderedCmpOp(AbstractTemplate):
    def generic(self, args, kws): ...

class TimedeltaMixOp(AbstractTemplate):
    def generic(self, args, kws):
        """
        (timedelta64, {int, float}) -> timedelta64
        ({int, float}, timedelta64) -> timedelta64
        """

class TimedeltaDivOp(AbstractTemplate):
    def generic(self, args, kws):
        """
        (timedelta64, {int, float}) -> timedelta64
        (timedelta64, timedelta64) -> float
        """

class TimedeltaUnaryPos(TimedeltaUnaryOp):
    key: Incomplete

class TimedeltaUnaryNeg(TimedeltaUnaryOp):
    key: Incomplete

class TimedeltaBinAdd(TimedeltaBinOp):
    key: Incomplete

class TimedeltaBinSub(TimedeltaBinOp):
    key: Incomplete

class TimedeltaBinMult(TimedeltaMixOp):
    key: Incomplete

class TimedeltaTrueDiv(TimedeltaDivOp):
    key: Incomplete

class TimedeltaFloorDiv(TimedeltaDivOp):
    key: Incomplete

class TimedeltaCmpEq(TimedeltaCmpOp):
    key: Incomplete

class TimedeltaCmpNe(TimedeltaCmpOp):
    key: Incomplete

class TimedeltaCmpLt(TimedeltaOrderedCmpOp):
    key: Incomplete

class TimedeltaCmpLE(TimedeltaOrderedCmpOp):
    key: Incomplete

class TimedeltaCmpGt(TimedeltaOrderedCmpOp):
    key: Incomplete

class TimedeltaCmpGE(TimedeltaOrderedCmpOp):
    key: Incomplete

class TimedeltaAbs(TimedeltaUnaryOp): ...

class DatetimePlusTimedelta(AbstractTemplate):
    key: Incomplete
    def generic(self, args, kws): ...

class DatetimeMinusTimedelta(AbstractTemplate):
    key: Incomplete
    def generic(self, args, kws): ...

class DatetimeMinusDatetime(AbstractTemplate):
    key: Incomplete
    def generic(self, args, kws): ...

class DatetimeCmpOp(AbstractTemplate):
    def generic(self, args, kws): ...

class DatetimeCmpEq(DatetimeCmpOp):
    key: Incomplete

class DatetimeCmpNe(DatetimeCmpOp):
    key: Incomplete

class DatetimeCmpLt(DatetimeCmpOp):
    key: Incomplete

class DatetimeCmpLE(DatetimeCmpOp):
    key: Incomplete

class DatetimeCmpGt(DatetimeCmpOp):
    key: Incomplete

class DatetimeCmpGE(DatetimeCmpOp):
    key: Incomplete

class DatetimeMinMax(AbstractTemplate):
    def generic(self, args, kws): ...
