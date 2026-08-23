from _typeshed import Incomplete

__all__ = ['Options']

class Option:
    """Base class for all kinds of options. """
    option: str | None
    is_Flag: bool
    requires: list[str]
    excludes: list[str]
    after: list[str]
    before: list[str]
    @classmethod
    def default(cls) -> None: ...
    @classmethod
    def preprocess(cls, option) -> None: ...
    @classmethod
    def postprocess(cls, options) -> None: ...

class Flag(Option):
    """Base class for all kinds of flags. """
    is_Flag: bool

class BooleanOption(Option):
    """An option that must have a boolean value or equivalent assigned. """
    @classmethod
    def preprocess(cls, value): ...

class OptionType(type):
    """Base type for all options that does registers options. """
    def __init__(cls, *args, **kwargs) -> None: ...

class Options(dict):
    """
    Options manager for polynomial manipulation module.

    Examples
    ========

    >>> from sympy.polys.polyoptions import Options
    >>> from sympy.polys.polyoptions import build_options

    >>> from sympy.abc import x, y, z

    >>> Options((x, y, z), {'domain': 'ZZ'})
    {'auto': False, 'domain': ZZ, 'gens': (x, y, z)}

    >>> build_options((x, y, z), {'domain': 'ZZ'})
    {'auto': False, 'domain': ZZ, 'gens': (x, y, z)}

    **Options**

    * Expand --- boolean option
    * Gens --- option
    * Wrt --- option
    * Sort --- option
    * Order --- option
    * Field --- boolean option
    * Greedy --- boolean option
    * Domain --- option
    * Split --- boolean option
    * Gaussian --- boolean option
    * Extension --- option
    * Modulus --- option
    * Symmetric --- boolean option
    * Strict --- boolean option

    **Flags**

    * Auto --- boolean flag
    * Frac --- boolean flag
    * Formal --- boolean flag
    * Polys --- boolean flag
    * Include --- boolean flag
    * All --- boolean flag
    * Gen --- flag
    * Series --- boolean flag

    """
    __order__: Incomplete
    __options__: dict[str, type[Option]]
    def __init__(self, gens, args, flags: Incomplete | None = None, strict: bool = False) -> None: ...
    def clone(self, updates={}):
        """Clone ``self`` and update specified options. """
    def __setattr__(self, attr, value) -> None: ...
    @property
    def args(self): ...
    @property
    def options(self): ...
    @property
    def flags(self): ...

class Expand(BooleanOption, metaclass=OptionType):
    """``expand`` option to polynomial manipulation functions. """
    option: str
    requires: list[str]
    excludes: list[str]
    @classmethod
    def default(cls): ...

class Gens(Option, metaclass=OptionType):
    """``gens`` option to polynomial manipulation functions. """
    option: str
    requires: list[str]
    excludes: list[str]
    @classmethod
    def default(cls): ...
    @classmethod
    def preprocess(cls, gens): ...

class Wrt(Option, metaclass=OptionType):
    """``wrt`` option to polynomial manipulation functions. """
    option: str
    requires: list[str]
    excludes: list[str]
    @classmethod
    def preprocess(cls, wrt): ...

class Sort(Option, metaclass=OptionType):
    """``sort`` option to polynomial manipulation functions. """
    option: str
    requires: list[str]
    excludes: list[str]
    @classmethod
    def default(cls): ...
    @classmethod
    def preprocess(cls, sort): ...

class Order(Option, metaclass=OptionType):
    """``order`` option to polynomial manipulation functions. """
    option: str
    requires: list[str]
    excludes: list[str]
    @classmethod
    def default(cls): ...
    @classmethod
    def preprocess(cls, order): ...

class Field(BooleanOption, metaclass=OptionType):
    """``field`` option to polynomial manipulation functions. """
    option: str
    requires: list[str]
    excludes: Incomplete

class Greedy(BooleanOption, metaclass=OptionType):
    """``greedy`` option to polynomial manipulation functions. """
    option: str
    requires: list[str]
    excludes: Incomplete

class Composite(BooleanOption, metaclass=OptionType):
    """``composite`` option to polynomial manipulation functions. """
    option: str
    @classmethod
    def default(cls) -> None: ...
    requires: list[str]
    excludes: Incomplete

class Domain(Option, metaclass=OptionType):
    """``domain`` option to polynomial manipulation functions. """
    option: str
    requires: list[str]
    excludes: Incomplete
    after: Incomplete
    @classmethod
    def preprocess(cls, domain): ...
    @classmethod
    def postprocess(cls, options) -> None: ...

class Split(BooleanOption, metaclass=OptionType):
    """``split`` option to polynomial manipulation functions. """
    option: str
    requires: list[str]
    excludes: Incomplete
    @classmethod
    def postprocess(cls, options) -> None: ...

class Gaussian(BooleanOption, metaclass=OptionType):
    """``gaussian`` option to polynomial manipulation functions. """
    option: str
    requires: list[str]
    excludes: Incomplete
    @classmethod
    def postprocess(cls, options) -> None: ...

class Extension(Option, metaclass=OptionType):
    """``extension`` option to polynomial manipulation functions. """
    option: str
    requires: list[str]
    excludes: Incomplete
    @classmethod
    def preprocess(cls, extension): ...
    @classmethod
    def postprocess(cls, options) -> None: ...

class Modulus(Option, metaclass=OptionType):
    """``modulus`` option to polynomial manipulation functions. """
    option: str
    requires: list[str]
    excludes: Incomplete
    @classmethod
    def preprocess(cls, modulus): ...
    @classmethod
    def postprocess(cls, options) -> None: ...

class Symmetric(BooleanOption, metaclass=OptionType):
    """``symmetric`` option to polynomial manipulation functions. """
    option: str
    requires: Incomplete
    excludes: Incomplete

class Strict(BooleanOption, metaclass=OptionType):
    """``strict`` option to polynomial manipulation functions. """
    option: str
    @classmethod
    def default(cls): ...

class Auto(BooleanOption, Flag, metaclass=OptionType):
    """``auto`` flag to polynomial manipulation functions. """
    option: str
    after: Incomplete
    @classmethod
    def default(cls): ...
    @classmethod
    def postprocess(cls, options) -> None: ...

class Frac(BooleanOption, Flag, metaclass=OptionType):
    """``auto`` option to polynomial manipulation functions. """
    option: str
    @classmethod
    def default(cls): ...

class Formal(BooleanOption, Flag, metaclass=OptionType):
    """``formal`` flag to polynomial manipulation functions. """
    option: str
    @classmethod
    def default(cls): ...

class Polys(BooleanOption, Flag, metaclass=OptionType):
    """``polys`` flag to polynomial manipulation functions. """
    option: str

class Include(BooleanOption, Flag, metaclass=OptionType):
    """``include`` flag to polynomial manipulation functions. """
    option: str
    @classmethod
    def default(cls): ...

class All(BooleanOption, Flag, metaclass=OptionType):
    """``all`` flag to polynomial manipulation functions. """
    option: str
    @classmethod
    def default(cls): ...

class Gen(Flag, metaclass=OptionType):
    """``gen`` flag to polynomial manipulation functions. """
    option: str
    @classmethod
    def default(cls): ...
    @classmethod
    def preprocess(cls, gen): ...

class Series(BooleanOption, Flag, metaclass=OptionType):
    """``series`` flag to polynomial manipulation functions. """
    option: str
    @classmethod
    def default(cls): ...

class Symbols(Flag, metaclass=OptionType):
    """``symbols`` flag to polynomial manipulation functions. """
    option: str
    @classmethod
    def default(cls): ...
    @classmethod
    def preprocess(cls, symbols): ...

class Method(Flag, metaclass=OptionType):
    """``method`` flag to polynomial manipulation functions. """
    option: str
    @classmethod
    def preprocess(cls, method): ...
