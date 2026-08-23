import numpy as np
from _typeshed import Incomplete
from typing import Any, Dict, List, Sequence

np_random_generator: Incomplete
LEGACY_RNG: bool

class np_random_generator: ...

logger: Incomplete

class _BackwardsCompatibleNumpyRng:
    """Thin wrapper to ensure backwards compatibility between
        new and old numpy randomness generators.
        """
    def __init__(self, generator_or_seed: np_random_generator | np.random.RandomState | int | None = None) -> None: ...
    @property
    def legacy_rng(self) -> bool: ...
    @property
    def rng(self): ...
    def __getattr__(self, name: str) -> Any: ...

RandomState: Incomplete

class Domain:
    """Base class to specify a type and valid range to sample parameters from.
    This base class is implemented by parameter spaces, like float ranges
    (``Float``), integer ranges (``Integer``), or categorical variables
    (``Categorical``). The ``Domain`` object contains information about
    valid values (e.g. minimum and maximum values), and exposes methods that
    allow specification of specific samplers (e.g. ``uniform()`` or
    ``loguniform()``).
    """
    sampler: Incomplete
    default_sampler_cls: Incomplete
    def cast(self, value):
        """Cast value to domain type"""
    def set_sampler(self, sampler, allow_override: bool = False) -> None: ...
    def get_sampler(self): ...
    def sample(self, spec: List[Dict] | Dict | None = None, size: int = 1, random_state: RandomState = None): ...
    def is_grid(self): ...
    def is_function(self): ...
    def is_valid(self, value: Any):
        """Returns True if `value` is a valid value in this domain."""
    @property
    def domain_str(self): ...

class Sampler:
    def sample(self, domain: Domain, spec: List[Dict] | Dict | None = None, size: int = 1, random_state: RandomState = None): ...

class BaseSampler(Sampler): ...
class Uniform(Sampler): ...

class LogUniform(Sampler):
    base: Incomplete
    def __init__(self, base: float = 10) -> None: ...

class Normal(Sampler):
    mean: Incomplete
    sd: Incomplete
    def __init__(self, mean: float = 0.0, sd: float = 0.0) -> None: ...

class Grid(Sampler):
    """Dummy sampler used for grid search"""
    def sample(self, domain: Domain, spec: List[Dict] | Dict | None = None, size: int = 1, random_state: RandomState = None): ...

class Float(Domain):
    class _Uniform(Uniform):
        def sample(self, domain: Float, spec: List[Dict] | Dict | None = None, size: int = 1, random_state: RandomState = None): ...
    class _LogUniform(LogUniform):
        def sample(self, domain: Float, spec: List[Dict] | Dict | None = None, size: int = 1, random_state: RandomState = None): ...
    class _Normal(Normal):
        def sample(self, domain: Float, spec: List[Dict] | Dict | None = None, size: int = 1, random_state: RandomState = None): ...
    default_sampler_cls: Incomplete
    lower: Incomplete
    upper: Incomplete
    def __init__(self, lower: float | None, upper: float | None) -> None: ...
    def cast(self, value): ...
    def uniform(self): ...
    def loguniform(self, base: float = 10): ...
    def normal(self, mean: float = 0.0, sd: float = 1.0): ...
    def quantized(self, q: float): ...
    def is_valid(self, value: float): ...
    @property
    def domain_str(self): ...

class Integer(Domain):
    class _Uniform(Uniform):
        def sample(self, domain: Integer, spec: List[Dict] | Dict | None = None, size: int = 1, random_state: RandomState = None): ...
    class _LogUniform(LogUniform):
        def sample(self, domain: Integer, spec: List[Dict] | Dict | None = None, size: int = 1, random_state: RandomState = None): ...
    default_sampler_cls: Incomplete
    lower: Incomplete
    upper: Incomplete
    def __init__(self, lower, upper) -> None: ...
    def cast(self, value): ...
    def quantized(self, q: int): ...
    def uniform(self): ...
    def loguniform(self, base: float = 10): ...
    def is_valid(self, value: int): ...
    @property
    def domain_str(self): ...

class Categorical(Domain):
    class _Uniform(Uniform):
        def sample(self, domain: Categorical, spec: List[Dict] | Dict | None = None, size: int = 1, random_state: RandomState = None): ...
    default_sampler_cls: Incomplete
    categories: Incomplete
    def __init__(self, categories: Sequence) -> None: ...
    def uniform(self): ...
    def grid(self): ...
    def __len__(self) -> int: ...
    def __getitem__(self, item): ...
    def is_valid(self, value: Any): ...
    @property
    def domain_str(self): ...

class Quantized(Sampler):
    sampler: Incomplete
    q: Incomplete
    def __init__(self, sampler: Sampler, q: float | int) -> None: ...
    def get_sampler(self): ...
    def sample(self, domain: Domain, spec: List[Dict] | Dict | None = None, size: int = 1, random_state: RandomState = None): ...

class PolynomialExpansionSet:
    def __init__(self, init_monomials: set = (), highest_poly_order: int = None, allow_self_inter: bool = False) -> None: ...
    @property
    def init_monomials(self): ...
    @property
    def highest_poly_order(self): ...
    @property
    def allow_self_inter(self): ...

def uniform(lower: float, upper: float):
    """Sample a float value uniformly between ``lower`` and ``upper``.
    Sampling from ``tune.uniform(1, 10)`` is equivalent to sampling from
    ``np.random.uniform(1, 10))``
    """
def quniform(lower: float, upper: float, q: float):
    """Sample a quantized float value uniformly between ``lower`` and ``upper``.
    Sampling from ``tune.uniform(1, 10)`` is equivalent to sampling from
    ``np.random.uniform(1, 10))``
    The value will be quantized, i.e. rounded to an integer increment of ``q``.
    Quantization makes the upper bound inclusive.
    """
def loguniform(lower: float, upper: float, base: float = 10):
    """Sugar for sampling in different orders of magnitude.
    Args:
        lower (float): Lower boundary of the output interval (e.g. 1e-4)
        upper (float): Upper boundary of the output interval (e.g. 1e-2)
        base (int): Base of the log. Defaults to 10.
    """
def qloguniform(lower: float, upper: float, q: float, base: float = 10):
    """Sugar for sampling in different orders of magnitude.
    The value will be quantized, i.e. rounded to an integer increment of ``q``.
    Quantization makes the upper bound inclusive.
    Args:
        lower (float): Lower boundary of the output interval (e.g. 1e-4)
        upper (float): Upper boundary of the output interval (e.g. 1e-2)
        q (float): Quantization number. The result will be rounded to an
            integer increment of this value.
        base (int): Base of the log. Defaults to 10.
    """
def choice(categories: Sequence):
    """Sample a categorical value.
    Sampling from ``tune.choice([1, 2])`` is equivalent to sampling from
    ``np.random.choice([1, 2])``
    """
def randint(lower: int, upper: int):
    """Sample an integer value uniformly between ``lower`` and ``upper``.
    ``lower`` is inclusive, ``upper`` is exclusive.
    Sampling from ``tune.randint(10)`` is equivalent to sampling from
    ``np.random.randint(10)``
    """
def lograndint(lower: int, upper: int, base: float = 10):
    """Sample an integer value log-uniformly between ``lower`` and ``upper``,
    with ``base`` being the base of logarithm.
    ``lower`` is inclusive, ``upper`` is exclusive.
    """
def qrandint(lower: int, upper: int, q: int = 1):
    """Sample an integer value uniformly between ``lower`` and ``upper``.

    ``lower`` is inclusive, ``upper`` is also inclusive (!).

    The value will be quantized, i.e. rounded to an integer increment of ``q``.
    Quantization makes the upper bound inclusive.
    """
def qlograndint(lower: int, upper: int, q: int, base: float = 10):
    """Sample an integer value log-uniformly between ``lower`` and ``upper``,
    with ``base`` being the base of logarithm.
    ``lower`` is inclusive, ``upper`` is also inclusive (!).
    The value will be quantized, i.e. rounded to an integer increment of ``q``.
    Quantization makes the upper bound inclusive.
    """
def randn(mean: float = 0.0, sd: float = 1.0):
    """Sample a float value normally with ``mean`` and ``sd``.
    Args:
        mean (float): Mean of the normal distribution. Defaults to 0.
        sd (float): SD of the normal distribution. Defaults to 1.
    """
def qrandn(mean: float, sd: float, q: float):
    """Sample a float value normally with ``mean`` and ``sd``.

    The value will be quantized, i.e. rounded to an integer increment of ``q``.

    Args:
        mean: Mean of the normal distribution.
        sd: SD of the normal distribution.
        q: Quantization number. The result will be rounded to an
            integer increment of this value.

    """
def polynomial_expansion_set(init_monomials: set, highest_poly_order: int = None, allow_self_inter: bool = False): ...
