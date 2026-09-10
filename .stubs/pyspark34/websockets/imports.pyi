from typing import Any, Dict

__all__ = ['lazy_import']

def lazy_import(namespace: Dict[str, Any], aliases: Dict[str, str] | None = None, deprecated_aliases: Dict[str, str] | None = None) -> None:
    '''
    Provide lazy, module-level imports.

    Typical use::

        __getattr__, __dir__ = lazy_import(
            globals(),
            aliases={
                "<name>": "<source module>",
                ...
            },
            deprecated_aliases={
                ...,
            }
        )

    This function defines ``__getattr__`` and ``__dir__`` per :pep:`562`.

    '''
