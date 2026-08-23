from _typeshed import Incomplete
from sentence_transformers import SentenceTransformer as SentenceTransformer
from torch import Tensor as Tensor, nn
from typing import Dict, Iterable

logger: Incomplete

class DenoisingAutoEncoderLoss(nn.Module):
    """
        This loss expects as input a batch consisting of damaged sentences and the corresponding original ones.
        The data generation process has already been implemented in readers/DenoisingAutoEncoderReader.py
        During training, the decoder reconstructs the original sentences from the encoded sentence embeddings.
        Here the argument 'decoder_name_or_path' indicates the pretrained model (supported by Huggingface) to be used as the decoder.
        Since decoding process is included, here the decoder should have a class called XXXLMHead (in the context of Huggingface's Transformers).
        Flag 'tie_encoder_decoder' indicates whether to tie the trainable parameters of encoder and decoder,
        which is shown beneficial to model performance while limiting the amount of required memory.
        Only when the encoder and decoder are from the same architecture, can the flag 'tie_encoder_decoder' works.
        For more information, please refer to the TSDAE paper.
    """
    encoder: Incomplete
    tokenizer_encoder: Incomplete
    tokenizer_decoder: Incomplete
    need_retokenization: Incomplete
    decoder: Incomplete
    def __init__(self, model: SentenceTransformer, decoder_name_or_path: str = None, tie_encoder_decoder: bool = True) -> None:
        """
        :param model: SentenceTransformer model
        :param decoder_name_or_path: Model name or path for initializing a decoder (compatible with Huggingface's Transformers)
        :param tie_encoder_decoder: whether to tie the trainable parameters of encoder and decoder
        """
    def retokenize(self, sentence_features): ...
    def forward(self, sentence_features: Iterable[Dict[str, Tensor]], labels: Tensor): ...
