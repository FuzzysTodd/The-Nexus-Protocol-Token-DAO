from ...processing_utils import ProcessorMixin as ProcessorMixin
from _typeshed import Incomplete
from transformers.utils import is_torch_available as is_torch_available

class OneFormerProcessor(ProcessorMixin):
    """
    Constructs an OneFormer processor which wraps [`OneFormerImageProcessor`] and
    [`CLIPTokenizer`]/[`CLIPTokenizerFast`] into a single processor that inherits both the image processor and
    tokenizer functionalities.

    Args:
        image_processor ([`OneFormerImageProcessor`]):
            The image processor is a required input.
        tokenizer ([`CLIPTokenizer`, `CLIPTokenizerFast`]):
            The tokenizer is a required input.
        max_seq_len (`int`, *optional*, defaults to 77)):
            Sequence length for input text list.
        task_seq_len (`int`, *optional*, defaults to 77):
            Sequence length for input task token.
    """
    attributes: Incomplete
    image_processor_class: str
    tokenizer_class: Incomplete
    max_seq_length: Incomplete
    task_seq_length: Incomplete
    def __init__(self, image_processor: Incomplete | None = None, tokenizer: Incomplete | None = None, max_seq_length: int = 77, task_seq_length: int = 77, **kwargs) -> None: ...
    def __call__(self, images: Incomplete | None = None, task_inputs: Incomplete | None = None, segmentation_maps: Incomplete | None = None, **kwargs):
        '''
        Main method to prepare for the model one or several task input(s) and image(s). This method forwards the
        `task_inputs` and `kwargs` arguments to CLIPTokenizer\'s [`~CLIPTokenizer.__call__`] if `task_inputs` is not
        `None` to encode. To prepare the image(s), this method forwards the `images` and `kwargs` arguments to
        OneFormerImageProcessor\'s [`~OneFormerImageProcessor.__call__`] if `images` is not `None`. Please refer to the
        doctsring of the above two methods for more information.

        Args:
            task_inputs (`str`, `List[str]`):
                The sequence or batch of task_inputs sequences to be encoded. Each sequence can be a string or a list
                of strings of the template "the task is {task}".
            images (`PIL.Image.Image`, `np.ndarray`, `torch.Tensor`, `List[PIL.Image.Image]`, `List[np.ndarray]`,
            `List[torch.Tensor]`):
                The image or batch of images to be prepared. Each image can be a PIL image, NumPy array or PyTorch
                tensor. In case of a NumPy array/PyTorch tensor, each image should be of shape (C, H, W), where C is a
                number of channels, H and W are image height and width.
            segmentation_maps (`ImageInput`, *optional*):
                The corresponding semantic segmentation maps with the pixel-wise annotations.

             (`bool`, *optional*, defaults to `True`):
                Whether or not to pad images up to the largest image in a batch and create a pixel mask.

                If left to the default, will return a pixel mask that is:

                - 1 for pixels that are real (i.e. **not masked**),
                - 0 for pixels that are padding (i.e. **masked**).
        Returns:
            [`BatchFeature`]: A [`BatchFeature`] with the following fields:
            - **task_inputs** -- List of token ids to be fed to a model. Returned when `text` is not `None`.
            - **pixel_values** -- Pixel values to be fed to a model. Returned when `images` is not `None`.
        '''
    def encode_inputs(self, images: Incomplete | None = None, task_inputs: Incomplete | None = None, segmentation_maps: Incomplete | None = None, **kwargs):
        """
        This method forwards all its arguments to [`OneFormerImageProcessor.encode_inputs`] and then tokenizes the
        task_inputs. Please refer to the docstring of this method for more information.
        """
    def post_process_semantic_segmentation(self, *args, **kwargs):
        """
        This method forwards all its arguments to [`OneFormerImageProcessor.post_process_semantic_segmentation`].
        Please refer to the docstring of this method for more information.
        """
    def post_process_instance_segmentation(self, *args, **kwargs):
        """
        This method forwards all its arguments to [`OneFormerImageProcessor.post_process_instance_segmentation`].
        Please refer to the docstring of this method for more information.
        """
    def post_process_panoptic_segmentation(self, *args, **kwargs):
        """
        This method forwards all its arguments to [`OneFormerImageProcessor.post_process_panoptic_segmentation`].
        Please refer to the docstring of this method for more information.
        """
