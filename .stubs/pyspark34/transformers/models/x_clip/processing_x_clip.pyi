from ...processing_utils import ProcessorMixin as ProcessorMixin
from ...tokenization_utils_base import BatchEncoding as BatchEncoding
from _typeshed import Incomplete

class XCLIPProcessor(ProcessorMixin):
    """
    Constructs an X-CLIP processor which wraps a VideoMAE image processor and a CLIP tokenizer into a single processor.

    [`XCLIPProcessor`] offers all the functionalities of [`VideoMAEImageProcessor`] and [`CLIPTokenizerFast`]. See the
    [`~XCLIPProcessor.__call__`] and [`~XCLIPProcessor.decode`] for more information.

    Args:
        image_processor ([`VideoMAEImageProcessor`]):
            The image processor is a required input.
        tokenizer ([`CLIPTokenizerFast`]):
            The tokenizer is a required input.
    """
    attributes: Incomplete
    image_processor_class: str
    tokenizer_class: Incomplete
    current_processor: Incomplete
    def __init__(self, image_processor: Incomplete | None = None, tokenizer: Incomplete | None = None, **kwargs) -> None: ...
    def __call__(self, text: Incomplete | None = None, videos: Incomplete | None = None, return_tensors: Incomplete | None = None, **kwargs):
        '''
        Main method to prepare for the model one or several sequences(s) and image(s). This method forwards the `text`
        and `kwargs` arguments to CLIPTokenizerFast\'s [`~CLIPTokenizerFast.__call__`] if `text` is not `None` to encode
        the text. To prepare the image(s), this method forwards the `videos` and `kwargs` arguments to
        VideoMAEImageProcessor\'s [`~VideoMAEImageProcessor.__call__`] if `videos` is not `None`. Please refer to the
        doctsring of the above two methods for more information.

        Args:
            text (`str`, `List[str]`, `List[List[str]]`):
                The sequence or batch of sequences to be encoded. Each sequence can be a string or a list of strings
                (pretokenized string). If the sequences are provided as list of strings (pretokenized), you must set
                `is_split_into_words=True` (to lift the ambiguity with a batch of sequences).
            videos (`List[PIL.Image.Image]`, `List[np.ndarray]`, `List[torch.Tensor]`, `List[List[PIL.Image.Image]]`, `List[List[np.ndarrray]]`,:
                `List[List[torch.Tensor]]`): The video or batch of videos to be prepared. Each video should be a list
                of frames, which can be either PIL images or NumPy arrays. In case of NumPy arrays/PyTorch tensors,
                each frame should be of shape (H, W, C), where H and W are frame height and width, and C is a number of
                channels.

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
            - **pixel_values** -- Pixel values to be fed to a model. Returned when `videos` is not `None`.
        '''
    def batch_decode(self, *args, **kwargs):
        """
        This method forwards all its arguments to CLIPTokenizerFast's [`~PreTrainedTokenizer.batch_decode`]. Please
        refer to the docstring of this method for more information.
        """
    def decode(self, *args, **kwargs):
        """
        This method forwards all its arguments to CLIPTokenizerFast's [`~PreTrainedTokenizer.decode`]. Please refer to
        the docstring of this method for more information.
        """
    @property
    def model_input_names(self): ...
    @property
    def feature_extractor_class(self): ...
    @property
    def feature_extractor(self): ...
