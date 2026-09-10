import abc
import torch
from ..utils import add_start_docstrings as add_start_docstrings
from .beam_constraints import Constraint as Constraint, ConstraintListState as ConstraintListState
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from typing import List, Optional, Tuple, Union

PROCESS_INPUTS_DOCSTRING: str
FINALIZE_INPUTS_DOCSTRING: str

class BeamScorer(ABC, metaclass=abc.ABCMeta):
    """
    Abstract base class for all beam scorers that are used for [`~PreTrainedModel.beam_search`] and
    [`~PreTrainedModel.beam_sample`].
    """
    @abstractmethod
    def process(self, input_ids: torch.LongTensor, next_scores: torch.FloatTensor, next_tokens: torch.LongTensor, next_indices: torch.LongTensor, **kwargs) -> Tuple[torch.Tensor]: ...
    @abstractmethod
    def finalize(self, input_ids: torch.LongTensor, next_scores: torch.FloatTensor, next_tokens: torch.LongTensor, next_indices: torch.LongTensor, max_length: int, **kwargs) -> torch.LongTensor: ...

class BeamSearchScorer(BeamScorer):
    '''
    [`BeamScorer`] implementing standard beam search decoding.

    Adapted in part from [Facebook\'s XLM beam search
    code](https://github.com/facebookresearch/XLM/blob/9e6f6814d17be4fe5b15f2e6c43eb2b2d76daeb4/src/model/transformer.py#L529).

    Reference for the diverse beam search algorithm and implementation [Ashwin Kalyan\'s DBS
    implementation](https://github.com/ashwinkalyan/dbs/blob/master/dbs/beam_utils.lua)

    Args:
        batch_size (`int`):
            Batch Size of `input_ids` for which standard beam search decoding is run in parallel.
        max_length (`int`):
            The maximum length of the sequence to be generated.
        num_beams (`int`):
            Number of beams for beam search.
        device (`torch.device`):
            Defines the device type (*e.g.*, `"cpu"` or `"cuda"`) on which this instance of `BeamSearchScorer` will be
            allocated.
        length_penalty (`float`, *optional*, defaults to 1.0):
            Exponential penalty to the length that is used with beam-based generation. It is applied as an exponent to
            the sequence length, which in turn is used to divide the score of the sequence. Since the score is the log
            likelihood of the sequence (i.e. negative), `length_penalty` > 0.0 promotes longer sequences, while
            `length_penalty` < 0.0 encourages shorter sequences.
        do_early_stopping (`bool`, *optional*, defaults to `False`):
            Whether to stop the beam search when at least `num_beams` sentences are finished per batch or not.
        num_beam_hyps_to_keep (`int`, *optional*, defaults to 1):
            The number of beam hypotheses that shall be returned upon calling
            [`~transformer.BeamSearchScorer.finalize`].
        num_beam_groups (`int`):
            Number of groups to divide `num_beams` into in order to ensure diversity among different groups of beams.
            See [this paper](https://arxiv.org/pdf/1610.02424.pdf) for more details.
    '''
    num_beams: Incomplete
    device: Incomplete
    length_penalty: Incomplete
    do_early_stopping: Incomplete
    num_beam_hyps_to_keep: Incomplete
    num_beam_groups: Incomplete
    group_size: Incomplete
    def __init__(self, batch_size: int, num_beams: int, device: torch.device, length_penalty: Optional[float] = 1.0, do_early_stopping: Optional[bool] = False, num_beam_hyps_to_keep: Optional[int] = 1, num_beam_groups: Optional[int] = 1, **kwargs) -> None: ...
    @property
    def is_done(self) -> bool: ...
    def process(self, input_ids: torch.LongTensor, next_scores: torch.FloatTensor, next_tokens: torch.LongTensor, next_indices: torch.LongTensor, pad_token_id: Optional[int] = None, eos_token_id: Optional[Union[int, List[int]]] = None, beam_indices: Optional[torch.LongTensor] = None) -> Tuple[torch.Tensor]: ...
    def finalize(self, input_ids: torch.LongTensor, final_beam_scores: torch.FloatTensor, final_beam_tokens: torch.LongTensor, final_beam_indices: torch.LongTensor, max_length: int, pad_token_id: Optional[int] = None, eos_token_id: Optional[Union[int, List[int]]] = None, beam_indices: Optional[torch.LongTensor] = None) -> Tuple[torch.LongTensor]: ...

class ConstrainedBeamSearchScorer(BeamScorer):
    '''
    [`BeamScorer`] implementing constrained beam search decoding.


    Args:
        batch_size (`int`):
            Batch Size of `input_ids` for which standard beam search decoding is run in parallel.
        max_length (`int`):
            The maximum length of the sequence to be generated.
        num_beams (`int`):
            Number of beams for beam search.
        constraints (`List[Constraint]`):
            A list of positive constraints represented as `Constraint` objects that must be fulfilled in the generation
            output. For more information, the documentation of [`Constraint`] should be read.
        device (`torch.device`):
            Defines the device type (*e.g.*, `"cpu"` or `"cuda"`) on which this instance of `BeamSearchScorer` will be
            allocated.
        length_penalty (`float`, *optional*, defaults to 1.0):
            Exponential penalty to the length that is used with beam-based generation. It is applied as an exponent to
            the sequence length, which in turn is used to divide the score of the sequence. Since the score is the log
            likelihood of the sequence (i.e. negative), `length_penalty` > 0.0 promotes longer sequences, while
            `length_penalty` < 0.0 encourages shorter sequences.
        do_early_stopping (`bool`, *optional*, defaults to `False`):
            Whether to stop the beam search when at least `num_beams` sentences are finished per batch or not.
        num_beam_hyps_to_keep (`int`, *optional*, defaults to 1):
            The number of beam hypotheses that shall be returned upon calling
            [`~transformer.BeamSearchScorer.finalize`].
        num_beam_groups (`int`):
            Number of groups to divide `num_beams` into in order to ensure diversity among different groups of beams.
            See [this paper](https://arxiv.org/pdf/1610.02424.pdf) for more details.
    '''
    num_beams: Incomplete
    device: Incomplete
    length_penalty: Incomplete
    do_early_stopping: Incomplete
    num_beam_hyps_to_keep: Incomplete
    num_beam_groups: Incomplete
    group_size: Incomplete
    constraints: Incomplete
    def __init__(self, batch_size: int, num_beams: int, constraints: List[Constraint], device: torch.device, length_penalty: Optional[float] = 1.0, do_early_stopping: Optional[bool] = False, num_beam_hyps_to_keep: Optional[int] = 1, num_beam_groups: Optional[int] = 1, **kwargs) -> None: ...
    @property
    def is_done(self) -> bool: ...
    def make_constraint_states(self, n): ...
    def check_completes_constraints(self, sequence): ...
    def process(self, input_ids: torch.LongTensor, next_scores: torch.FloatTensor, next_tokens: torch.LongTensor, next_indices: torch.LongTensor, scores_for_all_vocab: torch.FloatTensor, pad_token_id: Optional[int] = None, eos_token_id: Optional[Union[int, List[int]]] = None) -> Tuple[torch.Tensor]:
        """
        Args:
            input_ids (`torch.LongTensor` of shape `(batch_size * num_beams, sequence_length)`):
                Indices of input sequence tokens in the vocabulary.

                Indices can be obtained using any class inheriting from [`PreTrainedTokenizer`]. See
                [`PreTrainedTokenizer.encode`] and [`PreTrainedTokenizer.__call__`] for details.

                [What are input IDs?](../glossary#input-ids)
            next_scores (`torch.FloatTensor` of shape `(batch_size, 2 * num_beams)`):
                Current scores of the top `2 * num_beams` non-finished beam hypotheses.
            next_tokens (`torch.LongTensor` of shape `(batch_size, 2 * num_beams)`):
                `input_ids` of the tokens corresponding to the top `2 * num_beams` non-finished beam hypotheses.
            next_indices (`torch.LongTensor` of shape `(batch_size, 2 * num_beams)`):
                Beam indices indicating to which beam hypothesis the `next_tokens` correspond.
            scores_for_all_vocab (`torch.FloatTensor` of shape `(batch_size * num_beams, sequence_length)`):
                The scores of all tokens in the vocabulary for each of the beam hypotheses.
            pad_token_id (`int`, *optional*):
                The id of the *padding* token.
            eos_token_id (`Union[int, List[int]]`, *optional*):
                The id of the *end-of-sequence* token. Optionally, use a list to set multiple *end-of-sequence* tokens.

        Return:
            `UserDict`: A dictionary composed of the fields as defined above:

                - **next_beam_scores** (`torch.FloatTensor` of shape `(batch_size * num_beams)`) -- Updated scores of
                  all
                non-finished beams.

                - **next_beam_tokens** (`torch.FloatTensor` of shape `(batch_size * num_beams)`) -- Next tokens to be
                  added
                to the non-finished beam_hypotheses.
                - **next_beam_indices** (`torch.FloatTensor` of shape `(batch_size * num_beams)`) -- Beam indices
                indicating to which beam the next tokens shall be added.
        """
    def step_sentence_constraint(self, batch_idx: int, input_ids: torch.LongTensor, vocab_scores: torch.FloatTensor, sent_beam_scores: torch.FloatTensor, sent_beam_tokens: torch.LongTensor, sent_beam_indices: torch.LongTensor, push_progress: bool = False): ...
    def finalize(self, input_ids: torch.LongTensor, final_beam_scores: torch.FloatTensor, final_beam_tokens: torch.LongTensor, final_beam_indices: torch.LongTensor, max_length: int, pad_token_id: Optional[int] = None, eos_token_id: Optional[Union[int, List[int]]] = None) -> Tuple[torch.LongTensor]: ...

class BeamHypotheses:
    length_penalty: Incomplete
    early_stopping: Incomplete
    num_beams: Incomplete
    beams: Incomplete
    worst_score: float
    def __init__(self, num_beams: int, length_penalty: float, early_stopping: bool) -> None:
        """
        Initialize n-best list of hypotheses.
        """
    def __len__(self) -> int:
        """
        Number of hypotheses in the list.
        """
    def add(self, hyp: torch.LongTensor, sum_logprobs: float, beam_indices: Optional[torch.LongTensor] = None):
        """
        Add a new hypothesis to the list.
        """
    def is_done(self, best_sum_logprobs: float, cur_len: int) -> bool:
        """
        If there are enough hypotheses and that none of the hypotheses being generated can become better than the worst
        one in the heap, then we are done with this sentence.
        """
