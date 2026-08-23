from _typeshed import Incomplete
from enum import IntEnum
from numba.core import cgutils as cgutils, types as types
from numba.core.errors import TypingError as TypingError
from numba.core.extending import intrinsic as intrinsic, overload as overload, register_jitable as register_jitable
from numba.core.imputils import impl_ret_untracked as impl_ret_untracked
from typing import NamedTuple

class typerecord(NamedTuple):
    upper: Incomplete
    lower: Incomplete
    title: Incomplete
    decimal: Incomplete
    digit: Incomplete
    flags: Incomplete

class _PyUnicode_TyperecordMasks(IntEnum):
    ALPHA_MASK: int
    DECIMAL_MASK: int
    DIGIT_MASK: int
    LOWER_MASK: int
    LINEBREAK_MASK: int
    SPACE_MASK: int
    TITLE_MASK: int
    UPPER_MASK: int
    XID_START_MASK: int
    XID_CONTINUE_MASK: int
    PRINTABLE_MASK: int
    NUMERIC_MASK: int
    CASE_IGNORABLE_MASK: int
    CASED_MASK: int
    EXTENDED_CASE_MASK: int

def gettyperecord_impl(a):
    """
    Provides a _PyUnicode_gettyperecord binding, for convenience it will accept
    single character strings and code points.
    """

class _PY_CTF(IntEnum):
    LOWER: int
    UPPER: int
    ALPHA: Incomplete
    DIGIT: int
    ALNUM: Incomplete
    SPACE: int
    XDIGIT: int

class _PY_CTF_LB(IntEnum):
    LINE_BREAK: int
    LINE_FEED: int
    CARRIAGE_RETURN: int
