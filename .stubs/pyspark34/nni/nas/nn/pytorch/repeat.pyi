import torch.nn as nn
from .choice import ChoiceOf
from .mutation_utils import Mutable
from _typeshed import Incomplete
from typing import Callable, List, Tuple

__all__ = ['Repeat']

class Repeat(Mutable):
    """
    Repeat a block by a variable number of times.

    Parameters
    ----------
    blocks : function, list of function, module or list of module
        The block to be repeated. If not a list, it will be replicated (**deep-copied**) into a list.
        If a list, it should be of length ``max_depth``, the modules will be instantiated in order and a prefix will be taken.
        If a function, it will be called (the argument is the index) to instantiate a module.
        Otherwise the module will be deep-copied.
    depth : int or tuple of int
        If one number, the block will be repeated by a fixed number of times. If a tuple, it should be (min, max),
        meaning that the block will be repeated at least ``min`` times and at most ``max`` times.
        If a ValueChoice, it should choose from a series of positive integers.

        .. versionadded:: 2.8

           Minimum depth can be 0. But this feature is NOT supported on graph engine.

    Examples
    --------
    Block() will be deep copied and repeated 3 times. ::

        self.blocks = nn.Repeat(Block(), 3)

    Block() will be repeated 1, 2, or 3 times. ::

        self.blocks = nn.Repeat(Block(), (1, 3))

    Can be used together with layer choice.
    With deep copy, the 3 layers will have the same label, thus share the choice. ::

        self.blocks = nn.Repeat(nn.LayerChoice([...]), (1, 3))

    To make the three layer choices independent,
    we need a factory function that accepts index (0, 1, 2, ...) and returns the module of the ``index``-th layer. ::

        self.blocks = nn.Repeat(lambda index: nn.LayerChoice([...], label=f'layer{index}'), (1, 3))

    Depth can be a ValueChoice to support arbitrary depth candidate list. ::

        self.blocks = nn.Repeat(Block(), nn.ValueChoice([1, 3, 5]))
    """
    @classmethod
    def create_fixed_module(cls, blocks: Callable[[int], nn.Module] | List[Callable[[int], nn.Module]] | nn.Module | List[nn.Module], depth: int | Tuple[int, int] | ChoiceOf[int], *, label: str | None = None): ...
    depth_choice: Incomplete
    min_depth: Incomplete
    max_depth: Incomplete
    blocks: Incomplete
    def __init__(self, blocks: Callable[[int], nn.Module] | List[Callable[[int], nn.Module]] | nn.Module | List[nn.Module], depth: int | Tuple[int, int] | ChoiceOf[int], *, label: str | None = None) -> None: ...
    @property
    def label(self) -> str | None: ...
    def forward(self, x): ...
    def __getitem__(self, index): ...
    def __len__(self) -> int: ...
