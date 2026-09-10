from enum import Enum, EnumMeta
from typing import Any

class CaseInsensitiveEnumMeta(EnumMeta):
    """Enum metaclass to allow for interoperability with case-insensitive strings.

    Consuming this metaclass in an SDK should be done in the following manner:

    .. code-block:: python

        from enum import Enum
        from azure.core import CaseInsensitiveEnumMeta

        class MyCustomEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
            FOO = 'foo'
            BAR = 'bar'

    """
    def __getitem__(cls, name: str) -> Any: ...
    def __getattr__(cls, name: str) -> Enum:
        """Return the enum member matching `name`.

        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.

        :param str name: The name of the enum member to retrieve.
        :rtype: ~azure.core.CaseInsensitiveEnumMeta
        :return: The enum member matching `name`.
        :raises AttributeError: If `name` is not a valid enum member.
        """
