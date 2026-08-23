import os
from .dynamic_module_utils import custom_object_save as custom_object_save
from .feature_extraction_utils import BatchFeature as BaseBatchFeature
from .utils import IMAGE_PROCESSOR_NAME as IMAGE_PROCESSOR_NAME, PushToHubMixin as PushToHubMixin, cached_file as cached_file, copy_func as copy_func, download_url as download_url, is_offline_mode as is_offline_mode, is_remote_url as is_remote_url, logging as logging
from _typeshed import Incomplete
from typing import Any, Dict, Iterable, Optional, Tuple, Union

logger: Incomplete

class BatchFeature(BaseBatchFeature):
    """
    Holds the output of the image processor specific `__call__` methods.

    This class is derived from a python dictionary and can be used as a dictionary.

    Args:
        data (`dict`):
            Dictionary of lists/arrays/tensors returned by the __call__ method ('pixel_values', etc.).
        tensor_type (`Union[None, str, TensorType]`, *optional*):
            You can give a tensor_type here to convert the lists of integers in PyTorch/TensorFlow/Numpy Tensors at
            initialization.
    """

class ImageProcessingMixin(PushToHubMixin):
    """
    This is an image processor mixin used to provide saving/loading functionality for sequential and image feature
    extractors.
    """
    def __init__(self, **kwargs) -> None:
        """Set elements of `kwargs` as attributes."""
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path: Union[str, os.PathLike], **kwargs):
        '''
        Instantiate a type of [`~image_processing_utils.ImageProcessingMixin`] from an image processor.

        Args:
            pretrained_model_name_or_path (`str` or `os.PathLike`):
                This can be either:

                - a string, the *model id* of a pretrained image_processor hosted inside a model repo on
                  huggingface.co. Valid model ids can be located at the root-level, like `bert-base-uncased`, or
                  namespaced under a user or organization name, like `dbmdz/bert-base-german-cased`.
                - a path to a *directory* containing a image processor file saved using the
                  [`~image_processing_utils.ImageProcessingMixin.save_pretrained`] method, e.g.,
                  `./my_model_directory/`.
                - a path or url to a saved image processor JSON *file*, e.g.,
                  `./my_model_directory/preprocessor_config.json`.
            cache_dir (`str` or `os.PathLike`, *optional*):
                Path to a directory in which a downloaded pretrained model image processor should be cached if the
                standard cache should not be used.
            force_download (`bool`, *optional*, defaults to `False`):
                Whether or not to force to (re-)download the image processor files and override the cached versions if
                they exist.
            resume_download (`bool`, *optional*, defaults to `False`):
                Whether or not to delete incompletely received file. Attempts to resume the download if such a file
                exists.
            proxies (`Dict[str, str]`, *optional*):
                A dictionary of proxy servers to use by protocol or endpoint, e.g., `{\'http\': \'foo.bar:3128\',
                \'http://hostname\': \'foo.bar:4012\'}.` The proxies are used on each request.
            use_auth_token (`str` or `bool`, *optional*):
                The token to use as HTTP bearer authorization for remote files. If `True`, or not specified, will use
                the token generated when running `huggingface-cli login` (stored in `~/.huggingface`).
            revision (`str`, *optional*, defaults to `"main"`):
                The specific model version to use. It can be a branch name, a tag name, or a commit id, since we use a
                git-based system for storing models and other artifacts on huggingface.co, so `revision` can be any
                identifier allowed by git.


                <Tip>

                To test a pull request you made on the Hub, you can pass `revision="refs/pr/<pr_number>".

                </Tip>

            return_unused_kwargs (`bool`, *optional*, defaults to `False`):
                If `False`, then this function returns just the final image processor object. If `True`, then this
                functions returns a `Tuple(image_processor, unused_kwargs)` where *unused_kwargs* is a dictionary
                consisting of the key/value pairs whose keys are not image processor attributes: i.e., the part of
                `kwargs` which has not been used to update `image_processor` and is otherwise ignored.
            kwargs (`Dict[str, Any]`, *optional*):
                The values in kwargs of any keys which are image processor attributes will be used to override the
                loaded values. Behavior concerning key/value pairs whose keys are *not* image processor attributes is
                controlled by the `return_unused_kwargs` keyword parameter.

        Returns:
            A image processor of type [`~image_processing_utils.ImageProcessingMixin`].

        Examples:

        ```python
        # We can\'t instantiate directly the base class *ImageProcessingMixin* so let\'s show the examples on a
        # derived class: *CLIPImageProcessor*
        image_processor = CLIPImageProcessor.from_pretrained(
            "openai/clip-vit-base-patch32"
        )  # Download image_processing_config from huggingface.co and cache.
        image_processor = CLIPImageProcessor.from_pretrained(
            "./test/saved_model/"
        )  # E.g. image processor (or model) was saved using *save_pretrained(\'./test/saved_model/\')*
        image_processor = CLIPImageProcessor.from_pretrained("./test/saved_model/preprocessor_config.json")
        image_processor = CLIPImageProcessor.from_pretrained(
            "openai/clip-vit-base-patch32", do_normalize=False, foo=False
        )
        assert image_processor.do_normalize is False
        image_processor, unused_kwargs = CLIPImageProcessor.from_pretrained(
            "openai/clip-vit-base-patch32", do_normalize=False, foo=False, return_unused_kwargs=True
        )
        assert image_processor.do_normalize is False
        assert unused_kwargs == {"foo": False}
        ```'''
    def save_pretrained(self, save_directory: Union[str, os.PathLike], push_to_hub: bool = False, **kwargs):
        """
        Save an image processor object to the directory `save_directory`, so that it can be re-loaded using the
        [`~image_processing_utils.ImageProcessingMixin.from_pretrained`] class method.

        Args:
            save_directory (`str` or `os.PathLike`):
                Directory where the image processor JSON file will be saved (will be created if it does not exist).
            push_to_hub (`bool`, *optional*, defaults to `False`):
                Whether or not to push your model to the Hugging Face model hub after saving it. You can specify the
                repository you want to push to with `repo_id` (will default to the name of `save_directory` in your
                namespace).
            kwargs:
                Additional key word arguments passed along to the [`~utils.PushToHubMixin.push_to_hub`] method.
        """
    @classmethod
    def get_image_processor_dict(cls, pretrained_model_name_or_path: Union[str, os.PathLike], **kwargs) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """
        From a `pretrained_model_name_or_path`, resolve to a dictionary of parameters, to be used for instantiating a
        image processor of type [`~image_processor_utils.ImageProcessingMixin`] using `from_dict`.

        Parameters:
            pretrained_model_name_or_path (`str` or `os.PathLike`):
                The identifier of the pre-trained checkpoint from which we want the dictionary of parameters.

        Returns:
            `Tuple[Dict, Dict]`: The dictionary(ies) that will be used to instantiate the image processor object.
        """
    @classmethod
    def from_dict(cls, image_processor_dict: Dict[str, Any], **kwargs):
        """
        Instantiates a type of [`~image_processing_utils.ImageProcessingMixin`] from a Python dictionary of parameters.

        Args:
            image_processor_dict (`Dict[str, Any]`):
                Dictionary that will be used to instantiate the image processor object. Such a dictionary can be
                retrieved from a pretrained checkpoint by leveraging the
                [`~image_processing_utils.ImageProcessingMixin.to_dict`] method.
            kwargs (`Dict[str, Any]`):
                Additional parameters from which to initialize the image processor object.

        Returns:
            [`~image_processing_utils.ImageProcessingMixin`]: The image processor object instantiated from those
            parameters.
        """
    def to_dict(self) -> Dict[str, Any]:
        """
        Serializes this instance to a Python dictionary.

        Returns:
            `Dict[str, Any]`: Dictionary of all the attributes that make up this image processor instance.
        """
    @classmethod
    def from_json_file(cls, json_file: Union[str, os.PathLike]):
        """
        Instantiates a image processor of type [`~image_processing_utils.ImageProcessingMixin`] from the path to a JSON
        file of parameters.

        Args:
            json_file (`str` or `os.PathLike`):
                Path to the JSON file containing the parameters.

        Returns:
            A image processor of type [`~image_processing_utils.ImageProcessingMixin`]: The image_processor object
            instantiated from that JSON file.
        """
    def to_json_string(self) -> str:
        """
        Serializes this instance to a JSON string.

        Returns:
            `str`: String containing all the attributes that make up this feature_extractor instance in JSON format.
        """
    def to_json_file(self, json_file_path: Union[str, os.PathLike]):
        """
        Save this instance to a JSON file.

        Args:
            json_file_path (`str` or `os.PathLike`):
                Path to the JSON file in which this image_processor instance's parameters will be saved.
        """
    @classmethod
    def register_for_auto_class(cls, auto_class: str = 'AutoImageProcessor') -> None:
        '''
        Register this class with a given auto class. This should only be used for custom image processors as the ones
        in the library are already mapped with `AutoImageProcessor `.

        <Tip warning={true}>

        This API is experimental and may have some slight breaking changes in the next releases.

        </Tip>

        Args:
            auto_class (`str` or `type`, *optional*, defaults to `"AutoImageProcessor "`):
                The auto class to register this new image processor with.
        '''

class BaseImageProcessor(ImageProcessingMixin):
    def __init__(self, **kwargs) -> None: ...
    def __call__(self, images, **kwargs) -> BatchFeature:
        """Preprocess an image or a batch of images."""
    def preprocess(self, images, **kwargs) -> BatchFeature: ...

VALID_SIZE_DICT_KEYS: Incomplete

def is_valid_size_dict(size_dict): ...
def convert_to_size_dict(size, max_size: Optional[int] = None, default_to_square: bool = True, height_width_order: bool = True): ...
def get_size_dict(size: Union[int, Iterable[int], Dict[str, int]] = None, max_size: Optional[int] = None, height_width_order: bool = True, default_to_square: bool = True, param_name: str = 'size') -> dict:
    '''
    Converts the old size parameter in the config into the new dict expected in the config. This is to ensure backwards
    compatibility with the old image processor configs and removes ambiguity over whether the tuple is in (height,
    width) or (width, height) format.

    - If `size` is tuple, it is converted to `{"height": size[0], "width": size[1]}` or `{"height": size[1], "width":
    size[0]}` if `height_width_order` is `False`.
    - If `size` is an int, and `default_to_square` is `True`, it is converted to `{"height": size, "width": size}`.
    - If `size` is an int and `default_to_square` is False, it is converted to `{"shortest_edge": size}`. If `max_size`
      is set, it is added to the dict as `{"longest_edge": max_size}`.

    Args:
        size (`Union[int, Iterable[int], Dict[str, int]]`, *optional*):
            The `size` parameter to be cast into a size dictionary.
        max_size (`Optional[int]`, *optional*):
            The `max_size` parameter to be cast into a size dictionary.
        height_width_order (`bool`, *optional*, defaults to `True`):
            If `size` is a tuple, whether it\'s in (height, width) or (width, height) order.
        default_to_square (`bool`, *optional*, defaults to `True`):
            If `size` is an int, whether to default to a square image or not.
    '''
