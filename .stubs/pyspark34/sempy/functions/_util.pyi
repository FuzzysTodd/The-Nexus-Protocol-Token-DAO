from _typeshed import Incomplete
from sempy.functions.matcher import AlwaysTrueMatcher as AlwaysTrueMatcher, OrMatcher as OrMatcher, SeriesMatcher as SeriesMatcher, TypeMatcher as TypeMatcher

class _ParameterRequirement:
    name: Incomplete
    mandatory: Incomplete
    matcher: Incomplete
    is_list: Incomplete
    def __init__(self, name: str, mandatory: bool, matcher: SeriesMatcher, is_list: bool) -> None: ...
