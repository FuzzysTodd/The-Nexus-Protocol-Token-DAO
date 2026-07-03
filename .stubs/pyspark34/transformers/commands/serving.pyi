from . import BaseTransformersCLICommand as BaseTransformersCLICommand
from ..pipelines import Pipeline as Pipeline, get_supported_tasks as get_supported_tasks, pipeline as pipeline
from ..utils import logging as logging
from _typeshed import Incomplete
from argparse import ArgumentParser, Namespace
from pydantic import BaseModel
from typing import Any, List, Optional

BaseModel = object
logger: Incomplete

def serve_command_factory(args: Namespace):
    """
    Factory function used to instantiate serving server from provided command line arguments.

    Returns: ServeCommand
    """

class ServeModelInfoResult(BaseModel):
    """
    Expose model information
    """
    infos: dict

class ServeTokenizeResult(BaseModel):
    """
    Tokenize result model
    """
    tokens: List[str]
    tokens_ids: Optional[List[int]]

class ServeDeTokenizeResult(BaseModel):
    """
    DeTokenize result model
    """
    text: str

class ServeForwardResult(BaseModel):
    """
    Forward result model
    """
    output: Any

class ServeCommand(BaseTransformersCLICommand):
    @staticmethod
    def register_subcommand(parser: ArgumentParser):
        """
        Register this command to argparse so it's available for the transformer-cli

        Args:
            parser: Root parser to register command-specific arguments
        """
    host: Incomplete
    port: Incomplete
    workers: Incomplete
    def __init__(self, pipeline: Pipeline, host: str, port: int, workers: int) -> None: ...
    def run(self) -> None: ...
    def model_info(self): ...
    def tokenize(self, text_input: str = ..., return_ids: bool = ...):
        """
        Tokenize the provided input and eventually returns corresponding tokens id: - **text_input**: String to
        tokenize - **return_ids**: Boolean flags indicating if the tokens have to be converted to their integer
        mapping.
        """
    def detokenize(self, tokens_ids: List[int] = ..., skip_special_tokens: bool = ..., cleanup_tokenization_spaces: bool = ...):
        """
        Detokenize the provided tokens ids to readable text: - **tokens_ids**: List of tokens ids -
        **skip_special_tokens**: Flag indicating to not try to decode special tokens - **cleanup_tokenization_spaces**:
        Flag indicating to remove all leading/trailing spaces and intermediate ones.
        """
    async def forward(self, inputs=...):
        """
        **inputs**: **attention_mask**: **tokens_type_ids**:
        """
