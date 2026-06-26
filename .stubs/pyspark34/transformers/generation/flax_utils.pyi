import jax.numpy as jnp
from ..models.auto import FLAX_MODEL_FOR_CAUSAL_LM_MAPPING as FLAX_MODEL_FOR_CAUSAL_LM_MAPPING, FLAX_MODEL_FOR_SEQ_TO_SEQ_CAUSAL_LM_MAPPING as FLAX_MODEL_FOR_SEQ_TO_SEQ_CAUSAL_LM_MAPPING, FLAX_MODEL_FOR_VISION_2_SEQ_MAPPING as FLAX_MODEL_FOR_VISION_2_SEQ_MAPPING
from ..utils import ModelOutput as ModelOutput, logging as logging
from .configuration_utils import GenerationConfig as GenerationConfig
from .flax_logits_process import FlaxForcedBOSTokenLogitsProcessor as FlaxForcedBOSTokenLogitsProcessor, FlaxForcedEOSTokenLogitsProcessor as FlaxForcedEOSTokenLogitsProcessor, FlaxLogitsProcessorList as FlaxLogitsProcessorList, FlaxMinLengthLogitsProcessor as FlaxMinLengthLogitsProcessor, FlaxTemperatureLogitsWarper as FlaxTemperatureLogitsWarper, FlaxTopKLogitsWarper as FlaxTopKLogitsWarper, FlaxTopPLogitsWarper as FlaxTopPLogitsWarper
from _typeshed import Incomplete
from typing import Dict, Optional

logger: Incomplete

class FlaxGreedySearchOutput(ModelOutput):
    """
    Flax Base class for outputs of decoder-only generation models using greedy search.


    Args:
        sequences (`jnp.ndarray` of shape `(batch_size, max_length)`):
            The generated sequences.
    """
    sequences: jnp.ndarray

class FlaxSampleOutput(ModelOutput):
    """
    Flax Base class for outputs of decoder-only generation models using sampling.


    Args:
        sequences (`jnp.ndarray` of shape `(batch_size, max_length)`):
            The generated sequences.
    """
    sequences: jnp.ndarray

class FlaxBeamSearchOutput(ModelOutput):
    """
    Flax Base class for outputs of decoder-only generation models using greedy search.


    Args:
        sequences (`jnp.ndarray` of shape `(batch_size, max_length)`):
            The generated sequences.
        scores (`jnp.ndarray` of shape `(batch_size,)`):
            The scores (log probabilities) of the generated sequences.
    """
    sequences: jnp.ndarray
    scores: jnp.ndarray

class GreedyState:
    cur_len: jnp.ndarray
    sequences: jnp.ndarray
    running_token: jnp.ndarray
    is_sent_finished: jnp.ndarray
    model_kwargs: Dict[str, jnp.ndarray]

class SampleState:
    cur_len: jnp.ndarray
    sequences: jnp.ndarray
    running_token: jnp.ndarray
    is_sent_finished: jnp.ndarray
    prng_key: jnp.ndarray
    model_kwargs: Dict[str, jnp.ndarray]

class BeamSearchState:
    cur_len: jnp.ndarray
    running_sequences: jnp.ndarray
    running_scores: jnp.ndarray
    sequences: jnp.ndarray
    scores: jnp.ndarray
    is_sent_finished: jnp.ndarray
    model_kwargs: Dict[str, jnp.ndarray]

class FlaxGenerationMixin:
    """
    A class containing all functions for auto-regressive text generation, to be used as a mixin in
    [`FlaxPreTrainedModel`].

    The class exposes [`~generation.FlaxGenerationMixin.generate`], which can be used for:
            - *greedy decoding* by calling [`~generation.FlaxGenerationMixin._greedy_search`] if `num_beams=1` and
              `do_sample=False`
            - *multinomial sampling* by calling [`~generation.FlaxGenerationMixin._sample`] if `num_beams=1` and
              `do_sample=True`
            - *beam-search decoding* by calling [`~generation.FlaxGenerationMixin._beam_search`] if `num_beams>1` and
              `do_sample=False`

    You do not need to call any of the above methods directly. Pass custom parameter values to 'generate' instead. To
    learn more about decoding strategies refer to the [text generation strategies guide](./generation_strategies).
    """
    def prepare_inputs_for_generation(self, *args, **kwargs) -> None: ...
    generation_config: Incomplete
    def generate(self, input_ids: jnp.ndarray, generation_config: Optional[GenerationConfig] = None, prng_key: Optional[jnp.ndarray] = None, trace: bool = True, params: Optional[Dict[str, jnp.ndarray]] = None, **kwargs):
        """
        Generates sequences of token ids for models with a language modeling head.

        Parameters:
            input_ids (`jnp.ndarray` of shape `(batch_size, sequence_length)`):
                The sequence used as a prompt for the generation.
            generation_config (`~generation.GenerationConfig`, *optional*):
                The generation configuration to be used as base parametrization for the generation call. `**kwargs`
                passed to generate matching the attributes of `generation_config` will override them. If
                `generation_config` is not provided, the default will be used, which had the following loading
                priority: 1) from the `generation_config.json` model file, if it exists; 2) from the model
                configuration. Please note that unspecified parameters will inherit [`~generation.GenerationConfig`]'s
                default values, whose documentation should be checked to parameterize generation.
            trace (`bool`, *optional*, defaults to `True`):
                Whether to trace generation. Setting `trace=False` should only be used for debugging and will lead to a
                considerably slower runtime.
            params (`Dict[str, jnp.ndarray]`, *optional*):
                Optionally the model parameters can be passed. Can be useful for parallelized generation.
            kwargs:
                Ad hoc parametrization of `generate_config` and/or additional model-specific kwargs that will be
                forwarded to the `forward` function of the model. If the model is an encoder-decoder model, encoder
                specific kwargs should not be prefixed and decoder specific kwargs should be prefixed with *decoder_*.

        Return:
            [`~utils.ModelOutput`].

        """
