from ..models.auto.modeling_auto import MODEL_FOR_VIDEO_CLASSIFICATION_MAPPING as MODEL_FOR_VIDEO_CLASSIFICATION_MAPPING
from ..utils import add_end_docstrings as add_end_docstrings, is_decord_available as is_decord_available, is_torch_available as is_torch_available, logging as logging, requires_backends as requires_backends
from .base import PIPELINE_INIT_ARGS as PIPELINE_INIT_ARGS, Pipeline as Pipeline
from _typeshed import Incomplete
from typing import List, Union

logger: Incomplete

class VideoClassificationPipeline(Pipeline):
    '''
    Video classification pipeline using any `AutoModelForVideoClassification`. This pipeline predicts the class of a
    video.

    This video classification pipeline can currently be loaded from [`pipeline`] using the following task identifier:
    `"video-classification"`.

    See the list of available models on
    [huggingface.co/models](https://huggingface.co/models?filter=video-classification).
    '''
    def __init__(self, *args, **kwargs) -> None: ...
    def __call__(self, videos: Union[str, List[str]], **kwargs):
        """
        Assign labels to the video(s) passed as inputs.

        Args:
            videos (`str`, `List[str]`):
                The pipeline handles three types of videos:

                - A string containing a http link pointing to a video
                - A string containing a local path to a video

                The pipeline accepts either a single video or a batch of videos, which must then be passed as a string.
                Videos in a batch must all be in the same format: all as http links or all as local paths.
            top_k (`int`, *optional*, defaults to 5):
                The number of top labels that will be returned by the pipeline. If the provided number is higher than
                the number of labels available in the model configuration, it will default to the number of labels.
            num_frames (`int`, *optional*, defaults to `self.model.config.num_frames`):
                The number of frames sampled from the video to run the classification on. If not provided, will default
                to the number of frames specified in the model configuration.
            frame_sampling_rate (`int`, *optional*, defaults to 1):
                The sampling rate used to select frames from the video. If not provided, will default to 1, i.e. every
                frame will be used.

        Return:
            A dictionary or a list of dictionaries containing result. If the input is a single video, will return a
            dictionary, if the input is a list of several videos, will return a list of dictionaries corresponding to
            the videos.

            The dictionaries contain the following keys:

            - **label** (`str`) -- The label identified by the model.
            - **score** (`int`) -- The score attributed by the model for that label.
        """
    def preprocess(self, video, num_frames: Incomplete | None = None, frame_sampling_rate: int = 1): ...
    def postprocess(self, model_outputs, top_k: int = 5): ...
