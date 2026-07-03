from . import attributes as attributes, loading as loading, sync as sync
from .. import future as future, sql as sql, util as util
from ..sql import operators as operators
from ..sql.elements import BooleanClauseList as BooleanClauseList
from ..sql.selectable import LABEL_STYLE_TABLENAME_PLUS_COL as LABEL_STYLE_TABLENAME_PLUS_COL
from .base import state_str as state_str

def save_obj(base_mapper, states, uowtransaction, single: bool = False) -> None:
    """Issue ``INSERT`` and/or ``UPDATE`` statements for a list
    of objects.

    This is called within the context of a UOWTransaction during a
    flush operation, given a list of states to be flushed.  The
    base mapper in an inheritance hierarchy handles the inserts/
    updates for all descendant mappers.

    """
def post_update(base_mapper, states, uowtransaction, post_update_cols) -> None:
    """Issue UPDATE statements on behalf of a relationship() which
    specifies post_update.

    """
def delete_obj(base_mapper, states, uowtransaction) -> None:
    """Issue ``DELETE`` statements for a list of objects.

    This is called within the context of a UOWTransaction during a
    flush operation.

    """
