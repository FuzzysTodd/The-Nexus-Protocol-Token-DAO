import numpy as np
from ..tf_utils import stable_softmax as stable_softmax
from ..utils import add_end_docstrings as add_end_docstrings, is_tf_available as is_tf_available, is_torch_available as is_torch_available, logging as logging
from .base import GenericTensor as GenericTensor, PIPELINE_INIT_ARGS as PIPELINE_INIT_ARGS, Pipeline as Pipeline, PipelineException as PipelineException
from _typeshed import Incomplete
from typing import Dict

logger: Incomplete

class FillMaskPipeline(Pipeline):
    '''
    Masked language modeling prediction pipeline using any `ModelWithLMHead`. See the [masked language modeling
    examples](../task_summary#masked-language-modeling) for more information.

    Example:

    ```python
    >>> from transformers import pipeline

    >>> fill_masker = pipeline(model="bert-base-uncased")
    >>> fill_masker("This is a simple [MASK].")
    [{\'score\': 0.042, \'token\': 3291, \'token_str\': \'problem\', \'sequence\': \'this is a simple problem.\'}, {\'score\': 0.031, \'token\': 3160, \'token_str\': \'question\', \'sequence\': \'this is a simple question.\'}, {\'score\': 0.03, \'token\': 8522, \'token_str\': \'equation\', \'sequence\': \'this is a simple equation.\'}, {\'score\': 0.027, \'token\': 2028, \'token_str\': \'one\', \'sequence\': \'this is a simple one.\'}, {\'score\': 0.024, \'token\': 3627, \'token_str\': \'rule\', \'sequence\': \'this is a simple rule.\'}]
    ```

    Learn more about the basics of using a pipeline in the [pipeline tutorial](../pipeline_tutorial)

    This mask filling pipeline can currently be loaded from [`pipeline`] using the following task identifier:
    `"fill-mask"`.

    The models that this pipeline can use are models that have been trained with a masked language modeling objective,
    which includes the bi-directional models in the library. See the up-to-date list of available models on
    [huggingface.co/models](https://huggingface.co/models?filter=fill-mask).

    <Tip>

    This pipeline only works for inputs with exactly one token masked. Experimental: We added support for multiple
    masks. The returned values are raw model output, and correspond to disjoint probabilities where one might expect
    joint probabilities (See [discussion](https://github.com/huggingface/transformers/pull/10222)).

    </Tip>'''
    def get_masked_index(self, input_ids: GenericTensor) -> np.ndarray: ...
    def ensure_exactly_one_mask_token(self, model_inputs: GenericTensor): ...
    def preprocess(self, inputs, return_tensors: Incomplete | None = None, **preprocess_parameters) -> Dict[str, GenericTensor]: ...
    def postprocess(self, model_outputs, top_k: int = 5, target_ids: Incomplete | None = None): ...
    def get_target_ids(self, targets, top_k: Incomplete | None = None): ...
    def __call__(self, inputs, *args, **kwargs):
        """
        Fill the masked token in the text(s) given as inputs.

        Args:
            args (`str` or `List[str]`):
                One or several texts (or one list of prompts) with masked tokens.
            targets (`str` or `List[str]`, *optional*):
                When passed, the model will limit the scores to the passed targets instead of looking up in the whole
                vocab. If the provided targets are not in the model vocab, they will be tokenized and the first
                resulting token will be used (with a warning, and that might be slower).
            top_k (`int`, *optional*):
                When passed, overrides the number of predictions to return.

        Return:
            A list or a list of list of `dict`: Each result comes as list of dictionaries with the following keys:

            - **sequence** (`str`) -- The corresponding input with the mask token prediction.
            - **score** (`float`) -- The corresponding probability.
            - **token** (`int`) -- The predicted token id (to replace the masked one).
            - **token** (`str`) -- The predicted token (to replace the masked one).
        """
