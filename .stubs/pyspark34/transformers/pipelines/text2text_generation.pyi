import enum
from ..models.auto.modeling_auto import MODEL_FOR_SEQ_TO_SEQ_CAUSAL_LM_MAPPING as MODEL_FOR_SEQ_TO_SEQ_CAUSAL_LM_MAPPING
from ..models.auto.modeling_tf_auto import TF_MODEL_FOR_SEQ_TO_SEQ_CAUSAL_LM_MAPPING as TF_MODEL_FOR_SEQ_TO_SEQ_CAUSAL_LM_MAPPING
from ..tokenization_utils import TruncationStrategy as TruncationStrategy
from ..utils import add_end_docstrings as add_end_docstrings, is_tf_available as is_tf_available, is_torch_available as is_torch_available, logging as logging
from .base import PIPELINE_INIT_ARGS as PIPELINE_INIT_ARGS, Pipeline as Pipeline
from _typeshed import Incomplete

logger: Incomplete

class ReturnType(enum.Enum):
    TENSORS: int
    TEXT: int

class Text2TextGenerationPipeline(Pipeline):
    '''
    Pipeline for text to text generation using seq2seq models.

    Example:

    ```python
    >>> from transformers import pipeline

    >>> generator = pipeline(model="mrm8488/t5-base-finetuned-question-generation-ap")
    >>> generator(
    ...     "answer: Manuel context: Manuel has created RuPERTa-base with the support of HF-Transformers and Google"
    ... )
    [{\'generated_text\': \'question: Who created the RuPERTa-base?\'}]
    ```

    Learn more about the basics of using a pipeline in the [pipeline tutorial](../pipeline_tutorial)


    This Text2TextGenerationPipeline pipeline can currently be loaded from [`pipeline`] using the following task
    identifier: `"text2text-generation"`.

    The models that this pipeline can use are models that have been fine-tuned on a translation task. See the
    up-to-date list of available models on
    [huggingface.co/models](https://huggingface.co/models?filter=text2text-generation). For a list of available
    parameters, see the [following
    documentation](https://huggingface.co/docs/transformers/en/main_classes/text_generation#transformers.generation.GenerationMixin.generate)

    Usage:

    ```python
    text2text_generator = pipeline("text2text-generation")
    text2text_generator("question: What is 42 ? context: 42 is the answer to life, the universe and everything")
    ```'''
    return_name: str
    def __init__(self, *args, **kwargs) -> None: ...
    def check_inputs(self, input_length: int, min_length: int, max_length: int):
        """
        Checks whether there might be something wrong with given input with regard to the model.
        """
    def __call__(self, *args, **kwargs):
        """
        Generate the output text(s) using text(s) given as inputs.

        Args:
            args (`str` or `List[str]`):
                Input text for the encoder.
            return_tensors (`bool`, *optional*, defaults to `False`):
                Whether or not to include the tensors of predictions (as token indices) in the outputs.
            return_text (`bool`, *optional*, defaults to `True`):
                Whether or not to include the decoded texts in the outputs.
            clean_up_tokenization_spaces (`bool`, *optional*, defaults to `False`):
                Whether or not to clean up the potential extra spaces in the text output.
            truncation (`TruncationStrategy`, *optional*, defaults to `TruncationStrategy.DO_NOT_TRUNCATE`):
                The truncation strategy for the tokenization within the pipeline. `TruncationStrategy.DO_NOT_TRUNCATE`
                (default) will never truncate, but it is sometimes desirable to truncate the input to fit the model's
                max_length instead of throwing an error down the line.
            generate_kwargs:
                Additional keyword arguments to pass along to the generate method of the model (see the generate method
                corresponding to your framework [here](./model#generative-models)).

        Return:
            A list or a list of list of `dict`: Each result comes as a dictionary with the following keys:

            - **generated_text** (`str`, present when `return_text=True`) -- The generated text.
            - **generated_token_ids** (`torch.Tensor` or `tf.Tensor`, present when `return_tensors=True`) -- The token
              ids of the generated text.
        """
    def preprocess(self, inputs, truncation=..., **kwargs): ...
    def postprocess(self, model_outputs, return_type=..., clean_up_tokenization_spaces: bool = False): ...

class SummarizationPipeline(Text2TextGenerationPipeline):
    '''
    Summarize news articles and other documents.

    This summarizing pipeline can currently be loaded from [`pipeline`] using the following task identifier:
    `"summarization"`.

    The models that this pipeline can use are models that have been fine-tuned on a summarization task, which is
    currently, \'*bart-large-cnn*\', \'*t5-small*\', \'*t5-base*\', \'*t5-large*\', \'*t5-3b*\', \'*t5-11b*\'. See the up-to-date
    list of available models on [huggingface.co/models](https://huggingface.co/models?filter=summarization). For a list
    of available parameters, see the [following
    documentation](https://huggingface.co/docs/transformers/en/main_classes/text_generation#transformers.generation.GenerationMixin.generate)

    Usage:

    ```python
    # use bart in pytorch
    summarizer = pipeline("summarization")
    summarizer("An apple a day, keeps the doctor away", min_length=5, max_length=20)

    # use t5 in tf
    summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base", framework="tf")
    summarizer("An apple a day, keeps the doctor away", min_length=5, max_length=20)
    ```'''
    return_name: str
    def __call__(self, *args, **kwargs):
        """
        Summarize the text(s) given as inputs.

        Args:
            documents (*str* or `List[str]`):
                One or several articles (or one list of articles) to summarize.
            return_text (`bool`, *optional*, defaults to `True`):
                Whether or not to include the decoded texts in the outputs
            return_tensors (`bool`, *optional*, defaults to `False`):
                Whether or not to include the tensors of predictions (as token indices) in the outputs.
            clean_up_tokenization_spaces (`bool`, *optional*, defaults to `False`):
                Whether or not to clean up the potential extra spaces in the text output.
            generate_kwargs:
                Additional keyword arguments to pass along to the generate method of the model (see the generate method
                corresponding to your framework [here](./model#generative-models)).

        Return:
            A list or a list of list of `dict`: Each result comes as a dictionary with the following keys:

            - **summary_text** (`str`, present when `return_text=True`) -- The summary of the corresponding input.
            - **summary_token_ids** (`torch.Tensor` or `tf.Tensor`, present when `return_tensors=True`) -- The token
              ids of the summary.
        """
    def check_inputs(self, input_length: int, min_length: int, max_length: int) -> bool:
        """
        Checks whether there might be something wrong with given input with regard to the model.
        """

class TranslationPipeline(Text2TextGenerationPipeline):
    '''
    Translates from one language to another.

    This translation pipeline can currently be loaded from [`pipeline`] using the following task identifier:
    `"translation_xx_to_yy"`.

    The models that this pipeline can use are models that have been fine-tuned on a translation task. See the
    up-to-date list of available models on [huggingface.co/models](https://huggingface.co/models?filter=translation).
    For a list of available parameters, see the [following
    documentation](https://huggingface.co/docs/transformers/en/main_classes/text_generation#transformers.generation.GenerationMixin.generate)

    Usage:

    ```python
    en_fr_translator = pipeline("translation_en_to_fr")
    en_fr_translator("How old are you?")
    ```'''
    return_name: str
    def check_inputs(self, input_length: int, min_length: int, max_length: int): ...
    def preprocess(self, *args, truncation=..., src_lang: Incomplete | None = None, tgt_lang: Incomplete | None = None): ...
    def __call__(self, *args, **kwargs):
        """
        Translate the text(s) given as inputs.

        Args:
            args (`str` or `List[str]`):
                Texts to be translated.
            return_tensors (`bool`, *optional*, defaults to `False`):
                Whether or not to include the tensors of predictions (as token indices) in the outputs.
            return_text (`bool`, *optional*, defaults to `True`):
                Whether or not to include the decoded texts in the outputs.
            clean_up_tokenization_spaces (`bool`, *optional*, defaults to `False`):
                Whether or not to clean up the potential extra spaces in the text output.
            src_lang (`str`, *optional*):
                The language of the input. Might be required for multilingual models. Will not have any effect for
                single pair translation models
            tgt_lang (`str`, *optional*):
                The language of the desired output. Might be required for multilingual models. Will not have any effect
                for single pair translation models
            generate_kwargs:
                Additional keyword arguments to pass along to the generate method of the model (see the generate method
                corresponding to your framework [here](./model#generative-models)).

        Return:
            A list or a list of list of `dict`: Each result comes as a dictionary with the following keys:

            - **translation_text** (`str`, present when `return_text=True`) -- The translation.
            - **translation_token_ids** (`torch.Tensor` or `tf.Tensor`, present when `return_tensors=True`) -- The
              token ids of the translation.
        """
