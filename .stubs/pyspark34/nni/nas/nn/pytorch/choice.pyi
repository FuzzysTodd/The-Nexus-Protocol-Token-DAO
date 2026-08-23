import torch
import torch.nn as nn
from .mutation_utils import Mutable
from _typeshed import Incomplete
from nni.common.serializer import Translatable
from typing import Any, Callable, Dict, Generic, Iterable, List, NoReturn, Sequence, SupportsRound, TypeVar

__all__ = ['LayerChoice', 'InputChoice', 'ValueChoice', 'ModelParameterChoice', 'Placeholder', 'ChosenInputs', 'ReductionType', 'MaybeChoice', 'ChoiceOf']

class LayerChoice(Mutable):
    '''
    Layer choice selects one of the ``candidates``, then apply it on inputs and return results.

    It allows users to put several candidate operations (e.g., PyTorch modules), one of them is chosen in each explored model.

    *New in v2.2:* Layer choice can be nested.

    Parameters
    ----------
    candidates : list of nn.Module or OrderedDict
        A module list to be selected from.
    prior : list of float
        Prior distribution used in random sampling.
    label : str
        Identifier of the layer choice.

    Attributes
    ----------
    length : int
        Deprecated. Number of ops to choose from. ``len(layer_choice)`` is recommended.
    names : list of str
        Names of candidates.
    choices : list of Module
        Deprecated. A list of all candidate modules in the layer choice module.
        ``list(layer_choice)`` is recommended, which will serve the same purpose.

    Examples
    --------

    ::

        # import nni.retiarii.nn.pytorch as nn
        # declared in `__init__` method
        self.layer = nn.LayerChoice([
            ops.PoolBN(\'max\', channels, 3, stride, 1),
            ops.SepConv(channels, channels, 3, stride, 1),
            nn.Identity()
        ])
        # invoked in `forward` method
        out = self.layer(x)

    Notes
    -----
    ``candidates`` can be a list of modules or a ordered dict of named modules, for example,

    .. code-block:: python

        self.op_choice = LayerChoice(OrderedDict([
            ("conv3x3", nn.Conv2d(3, 16, 128)),
            ("conv5x5", nn.Conv2d(5, 16, 128)),
            ("conv7x7", nn.Conv2d(7, 16, 128))
        ]))

    Elements in layer choice can be modified or deleted. Use ``del self.op_choice["conv5x5"]`` or
    ``self.op_choice[1] = nn.Conv3d(...)``. Adding more choices is not supported yet.
    '''
    @classmethod
    def create_fixed_module(cls, candidates: Dict[str, nn.Module] | List[nn.Module], *, label: str | None = None, **kwargs): ...
    candidates: Incomplete
    prior: Incomplete
    names: Incomplete
    def __init__(self, candidates: Dict[str, nn.Module] | List[nn.Module], *, prior: List[float] | None = None, label: str | None = None, **kwargs) -> None: ...
    @property
    def label(self): ...
    def __getitem__(self, idx: int | str) -> nn.Module: ...
    def __setitem__(self, idx, module) -> None: ...
    def __delitem__(self, idx) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    def forward(self, x):
        """
        The forward of layer choice is simply running the first candidate module.
        It shouldn't be called directly by users in most cases.
        """

ReductionType: Incomplete

class InputChoice(Mutable):
    """
    Input choice selects ``n_chosen`` inputs from ``choose_from`` (contains ``n_candidates`` keys).

    It is mainly for choosing (or trying) different connections. It takes several tensors and chooses ``n_chosen`` tensors from them.
    When specific inputs are chosen, ``InputChoice`` will become :class:`ChosenInputs`.

    Use ``reduction`` to specify how chosen inputs are reduced into one output. A few options are:

    * ``none``: do nothing and return the list directly.
    * ``sum``: summing all the chosen inputs.
    * ``mean``: taking the average of all chosen inputs.
    * ``concat``: concatenate all chosen inputs at dimension 1.

    We don't support customizing reduction yet.

    Parameters
    ----------
    n_candidates : int
        Number of inputs to choose from. It is required.
    n_chosen : int
        Recommended inputs to choose. If None, mutator is instructed to select any.
    reduction : str
        ``mean``, ``concat``, ``sum`` or ``none``.
    prior : list of float
        Prior distribution used in random sampling.
    label : str
        Identifier of the input choice.

    Examples
    --------
    ::

        # import nni.retiarii.nn.pytorch as nn
        # declared in `__init__` method
        self.input_switch = nn.InputChoice(n_chosen=1)
        # invoked in `forward` method, choose one from the three
        out = self.input_switch([tensor1, tensor2, tensor3])
    """
    @classmethod
    def create_fixed_module(cls, n_candidates: int, n_chosen: int | None = 1, reduction: ReductionType = 'sum', *, prior: List[float] | None = None, label: str | None = None, **kwargs): ...
    n_candidates: Incomplete
    n_chosen: Incomplete
    reduction: Incomplete
    prior: Incomplete
    def __init__(self, n_candidates: int, n_chosen: int | None = 1, reduction: str = 'sum', *, prior: List[float] | None = None, label: str | None = None, **kwargs) -> None: ...
    @property
    def label(self): ...
    def forward(self, candidate_inputs: List[torch.Tensor]) -> torch.Tensor:
        """
        The forward of input choice is simply the first item of ``candidate_inputs``.
        It shouldn't be called directly by users in most cases.
        """

class ChosenInputs(nn.Module):
    """
    A module that chooses from a tensor list and outputs a reduced tensor.
    The already-chosen version of InputChoice.

    When forward, ``chosen`` will be used to select inputs from ``candidate_inputs``,
    and ``reduction`` will be used to choose from those inputs to form a tensor.

    Attributes
    ----------
    chosen : list of int
        Indices of chosen inputs.
    reduction : ``mean`` | ``concat`` | ``sum`` | ``none``
        How to reduce the inputs when multiple are selected.
    """
    chosen: Incomplete
    reduction: Incomplete
    def __init__(self, chosen: List[int] | int, reduction: ReductionType) -> None: ...
    def forward(self, candidate_inputs):
        """
        Compute the reduced input based on ``chosen`` and ``reduction``.
        """

class ValueChoiceX(Translatable, nn.Module, Generic[_cand]):
    """Internal API. Implementation note:

    The transformed (X) version of value choice.
    It can be the result of composition (transformation) of one or several value choices. For example,

    .. code-block:: python

        nn.ValueChoice([1, 2]) + nn.ValueChoice([3, 4]) + 5

    The instance of base class cannot be created directly. Instead, they should be only the result of transformation of value choice.
    Therefore, there is no need to implement ``create_fixed_module`` in this class, because,
    1. For python-engine, value choice itself has create fixed module. Consequently, the transformation is born to be fixed.
    2. For graph-engine, it uses evaluate to calculate the result.

    Potentially, we have to implement the evaluation logic in oneshot algorithms. I believe we can postpone the discussion till then.

    This class is implemented as a ``nn.Module`` so that it can be scanned by python engine / torchscript.
    """
    function: Incomplete
    repr_template: Incomplete
    arguments: Incomplete
    def __init__(self, function: Callable[..., _cand] = ..., repr_template: str = ..., arguments: List[Any] = ..., dry_run: bool = True) -> None: ...
    def forward(self) -> None: ...
    def inner_choices(self) -> Iterable['ValueChoice']:
        """
        Return a generator of all leaf value choices.
        Useful for composition of value choices.
        No deduplication on labels. Mutators should take care.
        """
    def dry_run(self) -> _cand:
        """
        Dry run the value choice to get one of its possible evaluation results.
        """
    def all_options(self) -> Iterable[_cand]:
        """Explore all possibilities of a value choice.
        """
    def evaluate(self, values: Iterable[_cand]) -> _cand:
        """
        Evaluate the result of this group.
        ``values`` should in the same order of ``inner_choices()``.
        """
    @staticmethod
    def to_int(obj: MaybeChoice[Any]) -> MaybeChoice[int]:
        """
        Convert a ``ValueChoice`` to an integer.
        """
    @staticmethod
    def to_float(obj: MaybeChoice[Any]) -> MaybeChoice[float]:
        """
        Convert a ``ValueChoice`` to a float.
        """
    @staticmethod
    def condition(pred: MaybeChoice[bool], true: MaybeChoice[_value], false: MaybeChoice[_value]) -> MaybeChoice[_value]:
        """
        Return ``true`` if the predicate ``pred`` is true else ``false``.

        Examples
        --------
        >>> ValueChoice.condition(ValueChoice([1, 2]) > ValueChoice([0, 3]), 2, 1)
        """
    @staticmethod
    def max(arg0: Iterable['MaybeChoice[_value]'] | MaybeChoice[_value], *args: MaybeChoice[_value]) -> MaybeChoice[_value]:
        """
        Returns the maximum value from a list of value choices.
        The usage should be similar to Python's built-in value choices,
        where the parameters could be an iterable, or at least two arguments.
        """
    @staticmethod
    def min(arg0: Iterable['MaybeChoice[_value]'] | MaybeChoice[_value], *args: MaybeChoice[_value]) -> MaybeChoice[_value]:
        """
        Returns the minunum value from a list of value choices.
        The usage should be similar to Python's built-in value choices,
        where the parameters could be an iterable, or at least two arguments.
        """
    def __hash__(self): ...
    def __getitem__(self, key: Any) -> ChoiceOf[Any]: ...
    def __round__(self, ndigits: MaybeChoice[int] | None = None) -> ChoiceOf[int | SupportsRound[_value]]: ...
    def __trunc__(self) -> NoReturn: ...
    def __floor__(self) -> ChoiceOf[int]: ...
    def __ceil__(self) -> ChoiceOf[int]: ...
    def __index__(self) -> NoReturn: ...
    def __bool__(self) -> NoReturn: ...
    def __neg__(self) -> ChoiceOf[_value]: ...
    def __pos__(self) -> ChoiceOf[_value]: ...
    def __invert__(self) -> ChoiceOf[_value]: ...
    def __add__(self, other: MaybeChoice[Any]) -> ChoiceOf[Any]: ...
    def __radd__(self, other: MaybeChoice[Any]) -> ChoiceOf[Any]: ...
    def __sub__(self, other: MaybeChoice[Any]) -> ChoiceOf[Any]: ...
    def __rsub__(self, other: MaybeChoice[Any]) -> ChoiceOf[Any]: ...
    def __mul__(self, other: MaybeChoice[Any]) -> ChoiceOf[Any]: ...
    def __rmul__(self, other: MaybeChoice[Any]) -> ChoiceOf[Any]: ...
    def __matmul__(self, other: MaybeChoice[Any]) -> ChoiceOf[Any]: ...
    def __rmatmul__(self, other: MaybeChoice[Any]) -> ChoiceOf[Any]: ...
    def __truediv__(self, other: MaybeChoice[Any]) -> ChoiceOf[Any]: ...
    def __rtruediv__(self, other: MaybeChoice[Any]) -> ChoiceOf[Any]: ...
    def __floordiv__(self, other: MaybeChoice[Any]) -> ChoiceOf[Any]: ...
    def __rfloordiv__(self, other: MaybeChoice[Any]) -> ChoiceOf[Any]: ...
    def __mod__(self, other: MaybeChoice[Any]) -> ChoiceOf[Any]: ...
    def __rmod__(self, other: MaybeChoice[Any]) -> ChoiceOf[Any]: ...
    def __lshift__(self, other: MaybeChoice[Any]) -> ChoiceOf[Any]: ...
    def __rlshift__(self, other: MaybeChoice[Any]) -> ChoiceOf[Any]: ...
    def __rshift__(self, other: MaybeChoice[Any]) -> ChoiceOf[Any]: ...
    def __rrshift__(self, other: MaybeChoice[Any]) -> ChoiceOf[Any]: ...
    def __and__(self, other: MaybeChoice[Any]) -> ChoiceOf[Any]: ...
    def __rand__(self, other: MaybeChoice[Any]) -> ChoiceOf[Any]: ...
    def __xor__(self, other: MaybeChoice[Any]) -> ChoiceOf[Any]: ...
    def __rxor__(self, other: MaybeChoice[Any]) -> ChoiceOf[Any]: ...
    def __or__(self, other: MaybeChoice[Any]) -> ChoiceOf[Any]: ...
    def __ror__(self, other: MaybeChoice[Any]) -> ChoiceOf[Any]: ...
    def __lt__(self, other: MaybeChoice[Any]) -> ChoiceOf[Any]: ...
    def __le__(self, other: MaybeChoice[Any]) -> ChoiceOf[Any]: ...
    def __eq__(self, other: MaybeChoice[Any]) -> ChoiceOf[Any]: ...
    def __ne__(self, other: MaybeChoice[Any]) -> ChoiceOf[Any]: ...
    def __ge__(self, other: MaybeChoice[Any]) -> ChoiceOf[Any]: ...
    def __gt__(self, other: MaybeChoice[Any]) -> ChoiceOf[Any]: ...
    def __pow__(self, other: MaybeChoice[Any], modulo: MaybeChoice[Any] | None = None) -> ChoiceOf[Any]: ...
    def __rpow__(self, other: MaybeChoice[Any], modulo: MaybeChoice[Any] | None = None) -> ChoiceOf[Any]: ...
    def __divmod__(self, other: MaybeChoice[Any]) -> ChoiceOf[Any]: ...
    def __rdivmod__(self, other: MaybeChoice[Any]) -> ChoiceOf[Any]: ...
    def __abs__(self) -> ChoiceOf[Any]: ...
ChoiceOf = ValueChoiceX
MaybeChoice: Incomplete

class ValueChoice(ValueChoiceX[_cand], Mutable):
    """
    ValueChoice is to choose one from ``candidates``. The most common use cases are:

    * Used as input arguments of :class:`~nni.retiarii.basic_unit`
      (i.e., modules in ``nni.retiarii.nn.pytorch`` and user-defined modules decorated with ``@basic_unit``).
    * Used as input arguments of evaluator (*new in v2.7*).

    It can be used in parameters of operators (i.e., a sub-module of the model): ::

        class Net(nn.Module):
            def __init__(self):
                super().__init__()
                self.conv = nn.Conv2d(3, nn.ValueChoice([32, 64]), kernel_size=nn.ValueChoice([3, 5, 7]))

            def forward(self, x):
                return self.conv(x)

    Or evaluator (only if the evaluator is :doc:`traceable </nas/serialization>`, e.g.,
    :class:`FunctionalEvaluator <nni.retiarii.evaluator.FunctionalEvaluator>`): ::

        def train_and_evaluate(model_cls, learning_rate):
            ...

        self.evaluator = FunctionalEvaluator(train_and_evaluate, learning_rate=nn.ValueChoice([1e-3, 1e-2, 1e-1]))

    Value choices supports arithmetic operators, which is particularly useful when searching for a network width multiplier: ::

        # init
        scale = nn.ValueChoice([1.0, 1.5, 2.0])
        self.conv1 = nn.Conv2d(3, round(scale * 16))
        self.conv2 = nn.Conv2d(round(scale * 16), round(scale * 64))
        self.conv3 = nn.Conv2d(round(scale * 64), round(scale * 256))

        # forward
        return self.conv3(self.conv2(self.conv1(x)))

    Or when kernel size and padding are coupled so as to keep the output size constant: ::

        # init
        ks = nn.ValueChoice([3, 5, 7])
        self.conv = nn.Conv2d(3, 16, kernel_size=ks, padding=(ks - 1) // 2)

        # forward
        return self.conv(x)

    Or when several layers are concatenated for a final layer. ::

        # init
        self.linear1 = nn.Linear(3, nn.ValueChoice([1, 2, 3], label='a'))
        self.linear2 = nn.Linear(3, nn.ValueChoice([4, 5, 6], label='b'))
        self.final = nn.Linear(nn.ValueChoice([1, 2, 3], label='a') + nn.ValueChoice([4, 5, 6], label='b'), 2)

        # forward
        return self.final(torch.cat([self.linear1(x), self.linear2(x)], 1))

    Some advanced operators are also provided, such as :meth:`ValueChoice.max` and :meth:`ValueChoice.cond`.

    .. tip::

        All the APIs have an optional argument called ``label``,
        mutations with the same label will share the same choice. A typical example is, ::

            self.net = nn.Sequential(
                nn.Linear(10, nn.ValueChoice([32, 64, 128], label='hidden_dim')),
                nn.Linear(nn.ValueChoice([32, 64, 128], label='hidden_dim'), 3)
            )

        Sharing the same value choice instance has the similar effect. ::

            class Net(nn.Module):
                def __init__(self):
                    super().__init__()
                    hidden_dim = nn.ValueChoice([128, 512])
                    self.fc = nn.Sequential(
                        nn.Linear(64, hidden_dim),
                        nn.Linear(hidden_dim, 10)
                    )

    .. warning::

        It looks as if a specific candidate has been chosen (e.g., how it looks like when you can put ``ValueChoice``
        as a parameter of ``nn.Conv2d``), but in fact it's a syntax sugar as because the basic units and evaluators
        do all the underlying works. That means, you cannot assume that ``ValueChoice`` can be used in the same way
        as its candidates. For example, the following usage will NOT work: ::

            self.blocks = []
            for i in range(nn.ValueChoice([1, 2, 3])):
                self.blocks.append(Block())

            # NOTE: instead you should probably write
            # self.blocks = nn.Repeat(Block(), (1, 3))

    Another use case is to initialize the values to choose from in init and call the module in forward to get the chosen value.
    Usually, this is used to pass a mutable value to a functional API like ``torch.xxx`` or ``nn.functional.xxx```.
    For example, ::

        class Net(nn.Module):
            def __init__(self):
                super().__init__()
                self.dropout_rate = nn.ValueChoice([0., 1.])

            def forward(self, x):
                return F.dropout(x, self.dropout_rate())

    Parameters
    ----------
    candidates : list
        List of values to choose from.
    prior : list of float
        Prior distribution to sample from.
    label : str
        Identifier of the value choice.
    """
    @classmethod
    def create_fixed_module(cls, candidates: List[_cand], *, label: str | None = None, **kwargs): ...
    candidates: Incomplete
    prior: Incomplete
    def __init__(self, candidates: List[_cand], *, prior: List[float] | None = None, label: str | None = None) -> None: ...
    @property
    def label(self): ...
    def forward(self):
        """
        The forward of input choice is simply the first value of ``candidates``.
        It shouldn't be called directly by users in most cases.
        """
    def inner_choices(self) -> Iterable['ValueChoice']: ...
    def dry_run(self) -> _cand: ...
ValueType = TypeVar('ValueType')

class ModelParameterChoice:
    """ModelParameterChoice chooses one hyper-parameter from ``candidates``.

    .. attention::

       This API is internal, and does not guarantee forward-compatibility.

    It's quite similar to :class:`ValueChoice`, but unlike :class:`ValueChoice`,
    it always returns a fixed value, even at the construction of base model.

    This makes it highly flexible (e.g., can be used in for-loop, if-condition, as argument of any function). For example: ::

        self.has_auxiliary_head = ModelParameterChoice([False, True])
        # this will raise error if you use `ValueChoice`
        if self.has_auxiliary_head is True:  # or self.has_auxiliary_head
            self.auxiliary_head = Head()
        else:
            self.auxiliary_head = None
        print(type(self.has_auxiliary_head))  # <class 'bool'>

    The working mechanism of :class:`ModelParameterChoice` is that, it registers itself
    in the ``model_wrapper``, as a hyper-parameter of the model, and then returns the value specified with ``default``.
    At base model construction, the default value will be used (as a mocked hyper-parameter).
    In trial, the hyper-parameter selected by strategy will be used.

    Although flexible, we still recommend using :class:`ValueChoice` in favor of :class:`ModelParameterChoice`,
    because information are lost when using :class:`ModelParameterChoice` in exchange of its flexibility,
    making it incompatible with one-shot strategies and non-python execution engines.

    .. warning::

        :class:`ModelParameterChoice` can NOT be nested.

    .. tip::

        Although called :class:`ModelParameterChoice`, it's meant to tune hyper-parameter of architecture.
        It's NOT used to tune model-training hyper-parameters like ``learning_rate``.
        If you need to tune ``learning_rate``, please use :class:`ValueChoice` on arguments of :class:`nni.retiarii.Evaluator`.

    Parameters
    ----------
    candidates : list of any
        List of values to choose from.
    prior : list of float
        Prior distribution to sample from. Currently has no effect.
    default : Callable[[List[Any]], Any] or Any
        Function that selects one from ``candidates``, or a candidate.
        Use :meth:`ModelParameterChoice.FIRST` or :meth:`ModelParameterChoice.LAST` to take the first or last item.
        Default: :meth:`ModelParameterChoice.FIRST`
    label : str
        Identifier of the value choice.

    Warnings
    --------
    :class:`ModelParameterChoice` is incompatible with one-shot strategies and non-python execution engines.

    Sometimes, the same search space implemented **without** :class:`ModelParameterChoice` can be simpler, and explored
    with more types of search strategies. For example, the following usages are equivalent: ::

        # with ModelParameterChoice
        depth = nn.ModelParameterChoice(list(range(3, 10)))
        blocks = []
        for i in range(depth):
            blocks.append(Block())

        # w/o HyperParmaeterChoice
        blocks = Repeat(Block(), (3, 9))

    Examples
    --------
    Get a dynamic-shaped parameter. Because ``torch.zeros`` is not a basic unit, we can't use :class:`ValueChoice` on it.

    >>> parameter_dim = nn.ModelParameterChoice([64, 128, 256])
    >>> self.token = nn.Parameter(torch.zeros(1, parameter_dim, 32, 32))
    """
    def __new__(cls, candidates: List[ValueType], *, prior: List[float] | None = None, default: Callable[[List[ValueType]], ValueType] | ValueType = None, label: str | None = None) -> ValueType: ...
    @staticmethod
    def create_default(candidates: List[ValueType], default: Callable[[List[ValueType]], ValueType] | ValueType, label: str | None) -> ValueType: ...
    @classmethod
    def create_fixed_module(cls, candidates: List[ValueType], *, label: str | None = None, **kwargs) -> ValueType: ...
    @staticmethod
    def FIRST(sequence: Sequence[ValueType]) -> ValueType:
        """Get the first item of sequence. Useful in ``default`` argument."""
    @staticmethod
    def LAST(sequence: Sequence[ValueType]) -> ValueType:
        """Get the last item of sequence. Useful in ``default`` argument."""

class Placeholder(nn.Module):
    """
    The API that creates an empty module for later mutations.
    For advanced usages only.
    """
    label: Incomplete
    related_info: Incomplete
    def __init__(self, label, **related_info) -> None: ...
    def forward(self, x):
        """
        Forward of placeholder is not meaningful.
        It returns input directly.
        """
