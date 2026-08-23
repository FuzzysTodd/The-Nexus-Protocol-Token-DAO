from .. import util as util
from ..util.typing import Literal as Literal
from enum import Enum
from typing import Callable, Tuple

class _StateChangeState(Enum): ...

class _StateChangeStates(_StateChangeState):
    ANY: int
    NO_CHANGE: int
    CHANGE_IN_PROGRESS: int

class _StateChange:
    """Supplies state assertion decorators.

    The current use case is for the :class:`_orm.SessionTransaction` class. The
    :class:`_StateChange` class itself is agnostic of the
    :class:`_orm.SessionTransaction` class so could in theory be generalized
    for other systems as well.

    """
    @classmethod
    def declare_states(cls, prerequisite_states: Literal[_StateChangeStates.ANY] | Tuple[_StateChangeState, ...], moves_to: _StateChangeState) -> Callable[[_F], _F]:
        """Method decorator declaring valid states.

        :param prerequisite_states: sequence of acceptable prerequisite
         states.   Can be the single constant _State.ANY to indicate no
         prerequisite state

        :param moves_to: the expected state at the end of the method, assuming
         no exceptions raised.   Can be the constant _State.NO_CHANGE to
         indicate state should not change at the end of the method.

        """
