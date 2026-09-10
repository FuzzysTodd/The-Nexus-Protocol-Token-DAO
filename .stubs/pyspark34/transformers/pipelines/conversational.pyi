import uuid
from ..utils import add_end_docstrings as add_end_docstrings, is_tf_available as is_tf_available, is_torch_available as is_torch_available, logging as logging
from .base import PIPELINE_INIT_ARGS as PIPELINE_INIT_ARGS, Pipeline as Pipeline
from _typeshed import Incomplete
from collections.abc import Generator
from typing import Any, Dict, List, Union

logger: Incomplete

class Conversation:
    '''
    Utility class containing a conversation and its history. This class is meant to be used as an input to the
    [`ConversationalPipeline`]. The conversation contains a number of utility function to manage the addition of new
    user input and generated model responses. A conversation needs to contain an unprocessed user input before being
    passed to the [`ConversationalPipeline`]. This user input is either created when the class is instantiated, or by
    calling `conversational_pipeline.append_response("input")` after a conversation turn.

    Arguments:
        text (`str`, *optional*):
            The initial user input to start the conversation. If not provided, a user input needs to be provided
            manually using the [`~Conversation.add_user_input`] method before the conversation can begin.
        conversation_id (`uuid.UUID`, *optional*):
            Unique identifier for the conversation. If not provided, a random UUID4 id will be assigned to the
            conversation.
        past_user_inputs (`List[str]`, *optional*):
            Eventual past history of the conversation of the user. You don\'t need to pass it manually if you use the
            pipeline interactively but if you want to recreate history you need to set both `past_user_inputs` and
            `generated_responses` with equal length lists of strings
        generated_responses (`List[str]`, *optional*):
            Eventual past history of the conversation of the model. You don\'t need to pass it manually if you use the
            pipeline interactively but if you want to recreate history you need to set both `past_user_inputs` and
            `generated_responses` with equal length lists of strings

    Usage:

    ```python
    conversation = Conversation("Going to the movies tonight - any suggestions?")

    # Steps usually performed by the model when generating a response:
    # 1. Mark the user input as processed (moved to the history)
    conversation.mark_processed()
    # 2. Append a mode response
    conversation.append_response("The Big lebowski.")

    conversation.add_user_input("Is it good?")
    ```'''
    uuid: Incomplete
    past_user_inputs: Incomplete
    generated_responses: Incomplete
    new_user_input: Incomplete
    def __init__(self, text: str = None, conversation_id: uuid.UUID = None, past_user_inputs: Incomplete | None = None, generated_responses: Incomplete | None = None) -> None: ...
    def __eq__(self, other): ...
    def add_user_input(self, text: str, overwrite: bool = False):
        """
        Add a user input to the conversation for the next round. This populates the internal `new_user_input` field.

        Args:
            text (`str`): The user input for the next conversation round.
            overwrite (`bool`, *optional*, defaults to `False`):
                Whether or not existing and unprocessed user input should be overwritten when this function is called.
        """
    def mark_processed(self) -> None:
        """
        Mark the conversation as processed (moves the content of `new_user_input` to `past_user_inputs`) and empties
        the `new_user_input` field.
        """
    def append_response(self, response: str):
        """
        Append a response to the list of generated responses.

        Args:
            response (`str`): The model generated response.
        """
    def iter_texts(self) -> Generator[Incomplete, None, None]:
        """
        Iterates over all blobs of the conversation.

        Returns: Iterator of (is_user, text_chunk) in chronological order of the conversation. `is_user` is a `bool`,
        `text_chunks` is a `str`.
        """

class ConversationalPipeline(Pipeline):
    '''
    Multi-turn conversational pipeline.

    Example:

    ```python
    >>> from transformers import pipeline, Conversation

    >>> chatbot = pipeline(model="microsoft/DialoGPT-medium")
    >>> conversation = Conversation("Going to the movies tonight - any suggestions?")
    >>> conversation = chatbot(conversation)
    >>> conversation.generated_responses[-1]
    \'The Big Lebowski\'

    >>> conversation.add_user_input("Is it an action movie?")
    >>> conversation = chatbot(conversation)
    >>> conversation.generated_responses[-1]
    "It\'s a comedy."
    ```

    Learn more about the basics of using a pipeline in the [pipeline tutorial](../pipeline_tutorial)

    This conversational pipeline can currently be loaded from [`pipeline`] using the following task identifier:
    `"conversational"`.

    The models that this pipeline can use are models that have been fine-tuned on a multi-turn conversational task,
    currently: *\'microsoft/DialoGPT-small\'*, *\'microsoft/DialoGPT-medium\'*, *\'microsoft/DialoGPT-large\'*. See the
    up-to-date list of available models on
    [huggingface.co/models](https://huggingface.co/models?filter=conversational).
    '''
    def __init__(self, *args, **kwargs) -> None: ...
    def __call__(self, conversations: Union[Conversation, List[Conversation]], num_workers: int = 0, **kwargs):
        """
        Generate responses for the conversation(s) given as inputs.

        Args:
            conversations (a [`Conversation`] or a list of [`Conversation`]):
                Conversations to generate responses for.
            clean_up_tokenization_spaces (`bool`, *optional*, defaults to `False`):
                Whether or not to clean up the potential extra spaces in the text output.
            generate_kwargs:
                Additional keyword arguments to pass along to the generate method of the model (see the generate method
                corresponding to your framework [here](./model#generative-models)).

        Returns:
            [`Conversation`] or a list of [`Conversation`]: Conversation(s) with updated generated responses for those
            containing a new user input.
        """
    def preprocess(self, conversation: Conversation, min_length_for_response: int = 32) -> Dict[str, Any]: ...
    def postprocess(self, model_outputs, clean_up_tokenization_spaces: bool = True): ...
