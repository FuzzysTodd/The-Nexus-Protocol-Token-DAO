from typing import Type, TypeVar

C = TypeVar('C')

def get_class(fqn: str, type: Type[C]) -> Type[C]:
    """Given a fully qualifed class name, import the module and return the class"""
