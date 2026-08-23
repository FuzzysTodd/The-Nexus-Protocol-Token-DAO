from ...processing_utils import ProcessorMixin as ProcessorMixin
from ...tokenization_utils_base import BatchEncoding as BatchEncoding
from _typeshed import Incomplete

class VisionTextDualEncoderProcessor(ProcessorMixin):
    """
    Constructs a VisionTextDualEncoder processor which wraps an image processor and a tokenizer into a single
    processor.

    [`VisionTextDualEncoderProcessor`] offers all the functionalities of [`AutoImageProcessor`] and [`AutoTokenizer`].
    See the [`~VisionTextDualEncoderProcessor.__call__`] and [`~VisionTextDualEncoderProcessor.decode`] for more
    information.

    Args:
        image_processor ([`AutoImageProcessor`]):
            The image processor is a required input.
        tokenizer ([`PreTrainedTokenizer`]):
            The tokenizer is a required input.
    """
    attributes: Incomplete
    image_processor_class: str
    tokenizer_class: str
    current_processor: Incomplete
    def __init__(self, image_processor: Incomplete | None = None, tokenizer: Incomplete | None = None, **kwargs) -> None: ...
    def __call__(self, text: Incomplete | None = None, images: Incomplete | None = None, return_tensors: Incomplete | None = None, **kwargs):
        '''
        Main method to prepare for the model one or several sequences(s) and image(s). This method forwards the `text`
        and `kwargs` arguments to VisionTextDualEncoderTokenizer\'s [`~PreTrainedTokenizer.__call__`] if `text` is not
        `None` to encode the text. To prepare the image(s), this method forwards the `images` and `kwrags` arguments to
        AutoImageProcessor\'s [`~AutoImageProcessor.__call__`] if `images` is not `None`. Please refer to the doctsring
        of the above two methods for more information.

        Args:
            text (`str`, `List[str]`, `List[List[str]]`):
                The sequence or batch of sequences to be encoded. Each sequence can be a string or a list of strings
                (pretokenized string). If the sequences are provided as list of strings (pretokenized), you must set
                `is_split_into_words=True` (to lift the ambiguity with a batch of sequences).
            images (`PIL.Image.Image`, `np.ndarray`, `torch.Tensor`, `List[PIL.Image.Image]`, `List[np.ndarray]`, `List[torch.Tensor]`):
                The image or batch of images to be prepared. Each image can be a PIL image, NumPy array or PyTorch
                tensor. In case of a NumPy array/PyTorch tensor, each image should be of shape (C, H, W), where C is a
                number of channels, H and W are image height and width.

            return_tensors (`str` or [`~utils.TensorType`], *optional*):
                If set, will return tensors of a particular framework. Acceptable values are:

                - `\'tf\'`: Return TensorFlow `tf.constant` objects.
                - `\'pt\'`: Return PyTorch `torch.Tensor` objects.
                - `\'np\'`: Return NumPy `np.ndarray` objects.
                - `\'jax\'`: Return JAX `jnp.ndarray` objects.

        Returns:
            [`BatchEncoding`]: A [`BatchEncoding`] with the following fields:

            - **input_ids** -- List of token ids to be fed to a model. Returned when `text` is not `None`.
            - **attention_mask** -- List of indices specifying which tokens should be attended to by the model (when
              `return_attention_mask=True` or if *"attention_mask"* is in `self.model_input_names` and if `text` is not
              `None`).
            - **pixel_values** -- Pixel values to be fed to a model. Returned when `images` is not `None`.
        '''
    def batch_decode(self, *args, **kwargs):
        """
        This method forwards all its arguments to VisionTextDualEncoderTokenizer's
        [`~PreTrainedTokenizer.batch_decode`]. Please refer to the docstring of this method for more information.
        """
    def decode(self, *args, **kwargs):
        """
        This method forwards all its arguments to VisionTextDualEncoderTokenizer's [`~PreTrainedTokenizer.decode`].
        Please refer to the docstring of this method for more information.
        """
    @property
    def model_input_names(self): ...
    @property
    def feature_extractor_class(self): ...
    @property
    def feature_extractor(self): ...
