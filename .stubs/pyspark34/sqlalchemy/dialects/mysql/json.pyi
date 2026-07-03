from ... import types as sqltypes

class JSON(sqltypes.JSON):
    """MySQL JSON type.

    MySQL supports JSON as of version 5.7.
    MariaDB supports JSON (as an alias for LONGTEXT) as of version 10.2.

    :class:`_mysql.JSON` is used automatically whenever the base
    :class:`_types.JSON` datatype is used against a MySQL or MariaDB backend.

    .. seealso::

        :class:`_types.JSON` - main documentation for the generic
        cross-platform JSON datatype.

    The :class:`.mysql.JSON` type supports persistence of JSON values
    as well as the core index operations provided by :class:`_types.JSON`
    datatype, by adapting the operations to render the ``JSON_EXTRACT``
    function at the database level.

    """

class _FormatTypeMixin:
    def bind_processor(self, dialect): ...
    def literal_processor(self, dialect): ...

class JSONIndexType(_FormatTypeMixin, sqltypes.JSON.JSONIndexType): ...
class JSONPathType(_FormatTypeMixin, sqltypes.JSON.JSONPathType): ...
