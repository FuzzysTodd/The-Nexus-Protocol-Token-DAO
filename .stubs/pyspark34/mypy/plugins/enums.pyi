import mypy.plugin
from _typeshed import Incomplete
from mypy.nodes import TypeInfo as TypeInfo
from mypy.semanal_enum import ENUM_BASES as ENUM_BASES
from mypy.subtypes import is_equivalent as is_equivalent
from mypy.typeops import fixup_partial_type as fixup_partial_type, make_simplified_union as make_simplified_union
from mypy.types import CallableType as CallableType, Instance as Instance, LiteralType as LiteralType, ProperType as ProperType, Type as Type, get_proper_type as get_proper_type
from typing_extensions import Final

ENUM_NAME_ACCESS: Final[Incomplete]
ENUM_VALUE_ACCESS: Final[Incomplete]

def enum_name_callback(ctx: mypy.plugin.AttributeContext) -> Type:
    '''This plugin refines the \'name\' attribute in enums to act as if
    they were declared to be final.

    For example, the expression \'MyEnum.FOO.name\' normally is inferred
    to be of type \'str\'.

    This plugin will instead make the inferred type be a \'str\' where the
    last known value is \'Literal["FOO"]\'. This means it would be legal to
    use \'MyEnum.FOO.name\' in contexts that expect a Literal type, just like
    any other Final variable or attribute.

    This plugin assumes that the provided context is an attribute access
    matching one of the strings found in \'ENUM_NAME_ACCESS\'.
    '''
def enum_value_callback(ctx: mypy.plugin.AttributeContext) -> Type:
    """This plugin refines the 'value' attribute in enums to refer to
    the original underlying value. For example, suppose we have the
    following:

        class SomeEnum:
            FOO = A()
            BAR = B()

    By default, mypy will infer that 'SomeEnum.FOO.value' and
    'SomeEnum.BAR.value' both are of type 'Any'. This plugin refines
    this inference so that mypy understands the expressions are
    actually of types 'A' and 'B' respectively. This better reflects
    the actual runtime behavior.

    This plugin works simply by looking up the original value assigned
    to the enum. For example, when this plugin sees 'SomeEnum.BAR.value',
    it will look up whatever type 'BAR' had in the SomeEnum TypeInfo and
    use that as the inferred type of the overall expression.

    This plugin assumes that the provided context is an attribute access
    matching one of the strings found in 'ENUM_VALUE_ACCESS'.
    """
