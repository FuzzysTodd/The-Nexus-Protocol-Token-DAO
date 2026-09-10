import typing as t
from .environment import Environment as Environment
from .runtime import Undefined as Undefined
from .utils import pass_environment as pass_environment
from _typeshed import Incomplete

def test_odd(value: int) -> bool:
    """Return true if the variable is odd."""
def test_even(value: int) -> bool:
    """Return true if the variable is even."""
def test_divisibleby(value: int, num: int) -> bool:
    """Check if a variable is divisible by a number."""
def test_defined(value: t.Any) -> bool:
    """Return true if the variable is defined:

    .. sourcecode:: jinja

        {% if variable is defined %}
            value of variable: {{ variable }}
        {% else %}
            variable is not defined
        {% endif %}

    See the :func:`default` filter for a simple way to set undefined
    variables.
    """
def test_undefined(value: t.Any) -> bool:
    """Like :func:`defined` but the other way round."""
def test_filter(env: Environment, value: str) -> bool:
    """Check if a filter exists by name. Useful if a filter may be
    optionally available.

    .. code-block:: jinja

        {% if 'markdown' is filter %}
            {{ value | markdown }}
        {% else %}
            {{ value }}
        {% endif %}

    .. versionadded:: 3.0
    """
def test_test(env: Environment, value: str) -> bool:
    """Check if a test exists by name. Useful if a test may be
    optionally available.

    .. code-block:: jinja

        {% if 'loud' is test %}
            {% if value is loud %}
                {{ value|upper }}
            {% else %}
                {{ value|lower }}
            {% endif %}
        {% else %}
            {{ value }}
        {% endif %}

    .. versionadded:: 3.0
    """
def test_none(value: t.Any) -> bool:
    """Return true if the variable is none."""
def test_boolean(value: t.Any) -> bool:
    """Return true if the object is a boolean value.

    .. versionadded:: 2.11
    """
def test_false(value: t.Any) -> bool:
    """Return true if the object is False.

    .. versionadded:: 2.11
    """
def test_true(value: t.Any) -> bool:
    """Return true if the object is True.

    .. versionadded:: 2.11
    """
def test_integer(value: t.Any) -> bool:
    """Return true if the object is an integer.

    .. versionadded:: 2.11
    """
def test_float(value: t.Any) -> bool:
    """Return true if the object is a float.

    .. versionadded:: 2.11
    """
def test_lower(value: str) -> bool:
    """Return true if the variable is lowercased."""
def test_upper(value: str) -> bool:
    """Return true if the variable is uppercased."""
def test_string(value: t.Any) -> bool:
    """Return true if the object is a string."""
def test_mapping(value: t.Any) -> bool:
    """Return true if the object is a mapping (dict etc.).

    .. versionadded:: 2.6
    """
def test_number(value: t.Any) -> bool:
    """Return true if the variable is a number."""
def test_sequence(value: t.Any) -> bool:
    """Return true if the variable is a sequence. Sequences are variables
    that are iterable.
    """
def test_sameas(value: t.Any, other: t.Any) -> bool:
    """Check if an object points to the same memory address than another
    object:

    .. sourcecode:: jinja

        {% if foo.attribute is sameas false %}
            the foo attribute really is the `False` singleton
        {% endif %}
    """
def test_iterable(value: t.Any) -> bool:
    """Check if it's possible to iterate over an object."""
def test_escaped(value: t.Any) -> bool:
    """Check if the value is escaped."""
def test_in(value: t.Any, seq: t.Container) -> bool:
    """Check if value is in seq.

    .. versionadded:: 2.10
    """

TESTS: Incomplete
