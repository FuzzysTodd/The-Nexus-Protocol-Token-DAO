from mypy.nodes import MypyFile as MypyFile, SymbolTableNode as SymbolTableNode, TypeInfo as TypeInfo

def lookup_fully_qualified(name: str, modules: dict[str, MypyFile], *, raise_on_missing: bool = False) -> SymbolTableNode | None:
    """Find a symbol using it fully qualified name.

    The algorithm has two steps: first we try splitting the name on '.' to find
    the module, then iteratively look for each next chunk after a '.' (e.g. for
    nested classes).

    This function should *not* be used to find a module. Those should be looked
    in the modules dictionary.
    """
