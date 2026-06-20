from .. import Features as Features
from ..packaged_modules.generator.generator import Generator as Generator
from .abc import AbstractDatasetInputStream as AbstractDatasetInputStream
from _typeshed import Incomplete
from typing import Callable

class GeneratorDatasetInputStream(AbstractDatasetInputStream):
    builder: Incomplete
    def __init__(self, generator: Callable, features: Features | None = None, cache_dir: str = None, keep_in_memory: bool = False, streaming: bool = False, gen_kwargs: dict | None = None, num_proc: int | None = None, **kwargs) -> None: ...
    def read(self): ...
