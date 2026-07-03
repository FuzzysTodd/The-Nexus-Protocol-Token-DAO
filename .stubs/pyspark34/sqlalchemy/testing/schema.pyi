from .. import schema
from _typeshed import Incomplete

__all__ = ['Table', 'Column']

def Table(*args, **kw) -> schema.Table:
    """A schema.Table wrapper/hook for dialect-specific tweaks."""
def Column(*args, **kw):
    """A schema.Column wrapper/hook for dialect-specific tweaks."""

class eq_type_affinity:
    '''Helper to compare types inside of datastructures based on affinity.

    E.g.::

        eq_(
            inspect(connection).get_columns("foo"),
            [
                {
                    "name": "id",
                    "type": testing.eq_type_affinity(sqltypes.INTEGER),
                    "nullable": False,
                    "default": None,
                    "autoincrement": False,
                },
                {
                    "name": "data",
                    "type": testing.eq_type_affinity(sqltypes.NullType),
                    "nullable": True,
                    "default": None,
                    "autoincrement": False,
                },
            ],
        )

    '''
    target: Incomplete
    def __init__(self, target) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

class eq_compile_type:
    """similar to eq_type_affinity but uses compile"""
    target: Incomplete
    def __init__(self, target) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

class eq_clause_element:
    """Helper to compare SQL structures based on compare()"""
    target: Incomplete
    def __init__(self, target) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
