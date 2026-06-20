import torch
from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, Seq2SeqLMOutput as Seq2SeqLMOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...utils import add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from ..auto.configuration_auto import AutoConfig as AutoConfig
from ..auto.modeling_auto import AutoModel as AutoModel, AutoModelForCausalLM as AutoModelForCausalLM
from .configuration_vision_encoder_decoder import VisionEncoderDecoderConfig as VisionEncoderDecoderConfig
from _typeshed import Incomplete
from typing import Optional, Tuple, Union

def shift_tokens_right(input_ids: torch.Tensor, pad_token_id: int, decoder_start_token_id: int):
    """
    Shift input ids one token to the right.
    """

logger: Incomplete
VISION_ENCODER_DECODER_START_DOCSTRING: str
VISION_ENCODER_DECODER_INPUTS_DOCSTRING: str

class VisionEncoderDecoderModel(PreTrainedModel):
    """
    [`VisionEncoderDecoderModel`] is a generic model class that will be instantiated as a transformer architecture with
    one of the base vision model classes of the library as encoder and another one as decoder when created with the
    :meth*~transformers.AutoModel.from_pretrained* class method for the encoder and
    :meth*~transformers.AutoModelForCausalLM.from_pretrained* class method for the decoder.
    """
    config_class = VisionEncoderDecoderConfig
    base_model_prefix: str
    main_input_name: str
    supports_gradient_checkpointing: bool
    encoder: Incomplete
    decoder: Incomplete
    enc_to_dec_proj: Incomplete
    def __init__(self, config: Optional[PretrainedConfig] = None, encoder: Optional[PreTrainedModel] = None, decoder: Optional[PreTrainedModel] = None) -> None: ...
    def get_encoder(self): ...
    def get_decoder(self): ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, new_embeddings): ...
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, **kwargs):
        '''
        Example:

        ```python
        >>> from transformers import VisionEncoderDecoderModel, AutoImageProcessor, AutoTokenizer
        >>> from PIL import Image
        >>> import requests

        >>> image_processor = AutoImageProcessor.from_pretrained("ydshieh/vit-gpt2-coco-en")
        >>> decoder_tokenizer = AutoTokenizer.from_pretrained("ydshieh/vit-gpt2-coco-en")
        >>> model = VisionEncoderDecoderModel.from_pretrained("ydshieh/vit-gpt2-coco-en")

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> img = Image.open(requests.get(url, stream=True).raw)
        >>> pixel_values = image_processor(images=img, return_tensors="pt").pixel_values  # Batch size 1

        >>> output_ids = model.generate(
        ...     pixel_values, max_length=16, num_beams=4, return_dict_in_generate=True
        ... ).sequences

        >>> preds = decoder_tokenizer.batch_decode(output_ids, skip_special_tokens=True)
        >>> preds = [pred.strip() for pred in preds]

        >>> assert preds == ["a cat laying on top of a couch next to another cat"]
        ```'''
    @classmethod
    def from_encoder_decoder_pretrained(cls, encoder_pretrained_model_name_or_path: str = None, decoder_pretrained_model_name_or_path: str = None, *model_args, **kwargs) -> PreTrainedModel:
        '''
        Instantiate an encoder and a decoder from one or two base classes of the library from pretrained model
        checkpoints.


        The model is set in evaluation mode by default using `model.eval()` (Dropout modules are deactivated). To train
        the model, you need to first set it back in training mode with `model.train()`.

        Params:
            encoder_pretrained_model_name_or_path (`str`, *optional*):
                Information necessary to initiate the image encoder. Can be either:

                    - A string, the *model id* of a pretrained model hosted inside a model repo on huggingface.co. An
                      example is `google/vit-base-patch16-224-in21k`.
                    - A path to a *directory* containing model weights saved using
                      [`~PreTrainedModel.save_pretrained`], e.g., `./my_model_directory/`.
                    - A path or url to a *tensorflow index checkpoint file* (e.g, `./tf_model/model.ckpt.index`). In
                      this case, `from_tf` should be set to `True` and a configuration object should be provided as
                      `config` argument. This loading path is slower than converting the TensorFlow checkpoint in a
                      PyTorch model using the provided conversion scripts and loading the PyTorch model afterwards.

            decoder_pretrained_model_name_or_path (`str`, *optional*, defaults to `None`):
                Information necessary to initiate the text decoder. Can be either:

                    - A string, the *model id* of a pretrained model hosted inside a model repo on huggingface.co.
                      Valid model ids can be located at the root-level, like `bert-base-uncased`, or namespaced under a
                      user or organization name, like `dbmdz/bert-base-german-cased`.
                    - A path to a *directory* containing model weights saved using
                      [`~PreTrainedModel.save_pretrained`], e.g., `./my_model_directory/`.
                    - A path or url to a *tensorflow index checkpoint file* (e.g, `./tf_model/model.ckpt.index`). In
                      this case, `from_tf` should be set to `True` and a configuration object should be provided as
                      `config` argument. This loading path is slower than converting the TensorFlow checkpoint in a
                      PyTorch model using the provided conversion scripts and loading the PyTorch model afterwards.

            model_args (remaining positional arguments, *optional*):
                All remaning positional arguments will be passed to the underlying model\'s `__init__` method.

            kwargs (remaining dictionary of keyword arguments, *optional*):
                Can be used to update the configuration object (after it being loaded) and initiate the model (e.g.,
                `output_attentions=True`).

                - To update the encoder configuration, use the prefix *encoder_* for each configuration parameter.
                - To update the decoder configuration, use the prefix *decoder_* for each configuration parameter.
                - To update the parent model configuration, do not use a prefix for each configuration parameter.

                Behaves differently depending on whether a `config` is provided or automatically loaded.

        Example:

        ```python
        >>> from transformers import VisionEncoderDecoderModel

        >>> # initialize a vit-bert from a pretrained ViT and a pretrained BERT model. Note that the cross-attention layers will be randomly initialized
        >>> model = VisionEncoderDecoderModel.from_encoder_decoder_pretrained(
        ...     "google/vit-base-patch16-224-in21k", "bert-base-uncased"
        ... )
        >>> # saving model after fine-tuning
        >>> model.save_pretrained("./vit-bert")
        >>> # load fine-tuned model
        >>> model = VisionEncoderDecoderModel.from_pretrained("./vit-bert")
        ```'''
    def forward(self, pixel_values: Optional[torch.FloatTensor] = None, decoder_input_ids: Optional[torch.LongTensor] = None, decoder_attention_mask: Optional[torch.BoolTensor] = None, encoder_outputs: Optional[Tuple[torch.FloatTensor]] = None, past_key_values: Optional[Tuple[Tuple[torch.FloatTensor]]] = None, decoder_inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, **kwargs) -> Union[Tuple[torch.FloatTensor], Seq2SeqLMOutput]:
        '''
        Returns:

        Examples:

        ```python
        >>> from transformers import AutoProcessor, VisionEncoderDecoderModel
        >>> import requests
        >>> from PIL import Image
        >>> import torch

        >>> processor = AutoProcessor.from_pretrained("microsoft/trocr-base-handwritten")
        >>> model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")

        >>> # load image from the IAM dataset
        >>> url = "https://fki.tic.heia-fr.ch/static/img/a01-122-02.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw).convert("RGB")

        >>> # training
        >>> model.config.decoder_start_token_id = processor.tokenizer.cls_token_id
        >>> model.config.pad_token_id = processor.tokenizer.pad_token_id
        >>> model.config.vocab_size = model.config.decoder.vocab_size

        >>> pixel_values = processor(image, return_tensors="pt").pixel_values
        >>> text = "hello world"
        >>> labels = processor.tokenizer(text, return_tensors="pt").input_ids
        >>> outputs = model(pixel_values=pixel_values, labels=labels)
        >>> loss = outputs.loss

        >>> # inference (generation)
        >>> generated_ids = model.generate(pixel_values)
        >>> generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
        ```'''
    def prepare_decoder_input_ids_from_labels(self, labels: torch.Tensor): ...
    def prepare_inputs_for_generation(self, input_ids, past_key_values: Incomplete | None = None, attention_mask: Incomplete | None = None, use_cache: Incomplete | None = None, encoder_outputs: Incomplete | None = None, **kwargs): ...
    def resize_token_embeddings(self, *args, **kwargs) -> None: ...
