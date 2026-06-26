from .. import PretrainedConfig as PretrainedConfig, is_tf_available as is_tf_available, is_torch_available as is_torch_available
from ..utils import TF2_WEIGHTS_NAME as TF2_WEIGHTS_NAME, WEIGHTS_NAME as WEIGHTS_NAME, logging as logging
from .config import OnnxConfig as OnnxConfig
from _typeshed import Incomplete
from transformers import PreTrainedModel as PreTrainedModel, TFPreTrainedModel as TFPreTrainedModel
from transformers.models.auto import AutoModel as AutoModel, AutoModelForCausalLM as AutoModelForCausalLM, AutoModelForImageClassification as AutoModelForImageClassification, AutoModelForImageSegmentation as AutoModelForImageSegmentation, AutoModelForMaskedImageModeling as AutoModelForMaskedImageModeling, AutoModelForMaskedLM as AutoModelForMaskedLM, AutoModelForMultipleChoice as AutoModelForMultipleChoice, AutoModelForObjectDetection as AutoModelForObjectDetection, AutoModelForQuestionAnswering as AutoModelForQuestionAnswering, AutoModelForSemanticSegmentation as AutoModelForSemanticSegmentation, AutoModelForSeq2SeqLM as AutoModelForSeq2SeqLM, AutoModelForSequenceClassification as AutoModelForSequenceClassification, AutoModelForSpeechSeq2Seq as AutoModelForSpeechSeq2Seq, AutoModelForTokenClassification as AutoModelForTokenClassification, AutoModelForVision2Seq as AutoModelForVision2Seq, TFAutoModel as TFAutoModel, TFAutoModelForCausalLM as TFAutoModelForCausalLM, TFAutoModelForMaskedLM as TFAutoModelForMaskedLM, TFAutoModelForMultipleChoice as TFAutoModelForMultipleChoice, TFAutoModelForQuestionAnswering as TFAutoModelForQuestionAnswering, TFAutoModelForSemanticSegmentation as TFAutoModelForSemanticSegmentation, TFAutoModelForSeq2SeqLM as TFAutoModelForSeq2SeqLM, TFAutoModelForSequenceClassification as TFAutoModelForSequenceClassification, TFAutoModelForTokenClassification as TFAutoModelForTokenClassification
from typing import Callable, Dict, Optional, Tuple, Type, Union

logger: Incomplete

def supported_features_mapping(*supported_features: str, onnx_config_cls: str = None) -> Dict[str, Callable[[PretrainedConfig], OnnxConfig]]:
    """
    Generate the mapping between supported the features and their corresponding OnnxConfig for a given model.

    Args:
        *supported_features: The names of the supported features.
        onnx_config_cls: The OnnxConfig full name corresponding to the model.

    Returns:
        The dictionary mapping a feature to an OnnxConfig constructor.
    """

class FeaturesManager:
    AVAILABLE_FEATURES: Incomplete
    @staticmethod
    def get_supported_features_for_model_type(model_type: str, model_name: Optional[str] = None) -> Dict[str, Callable[[PretrainedConfig], OnnxConfig]]:
        """
        Tries to retrieve the feature -> OnnxConfig constructor map from the model type.

        Args:
            model_type (`str`):
                The model type to retrieve the supported features for.
            model_name (`str`, *optional*):
                The name attribute of the model object, only used for the exception message.

        Returns:
            The dictionary mapping each feature to a corresponding OnnxConfig constructor.
        """
    @staticmethod
    def feature_to_task(feature: str) -> str: ...
    @staticmethod
    def get_model_class_for_feature(feature: str, framework: str = 'pt') -> Type:
        '''
        Attempts to retrieve an AutoModel class from a feature name.

        Args:
            feature (`str`):
                The feature required.
            framework (`str`, *optional*, defaults to `"pt"`):
                The framework to use for the export.

        Returns:
            The AutoModel class corresponding to the feature.
        '''
    @staticmethod
    def determine_framework(model: str, framework: str = None) -> str:
        """
        Determines the framework to use for the export.

        The priority is in the following order:
            1. User input via `framework`.
            2. If local checkpoint is provided, use the same framework as the checkpoint.
            3. Available framework in environment, with priority given to PyTorch

        Args:
            model (`str`):
                The name of the model to export.
            framework (`str`, *optional*, defaults to `None`):
                The framework to use for the export. See above for priority if none provided.

        Returns:
            The framework to use for the export.

        """
    @staticmethod
    def get_model_from_feature(feature: str, model: str, framework: str = None, cache_dir: str = None) -> Union['PreTrainedModel', 'TFPreTrainedModel']:
        """
        Attempts to retrieve a model from a model's name and the feature to be enabled.

        Args:
            feature (`str`):
                The feature required.
            model (`str`):
                The name of the model to export.
            framework (`str`, *optional*, defaults to `None`):
                The framework to use for the export. See `FeaturesManager.determine_framework` for the priority should
                none be provided.

        Returns:
            The instance of the model.

        """
    @staticmethod
    def check_supported_model_or_raise(model: Union['PreTrainedModel', 'TFPreTrainedModel'], feature: str = 'default') -> Tuple[str, Callable]:
        """
        Check whether or not the model has the requested features.

        Args:
            model: The model to export.
            feature: The name of the feature to check if it is available.

        Returns:
            (str) The type of the model (OnnxConfig) The OnnxConfig instance holding the model export properties.

        """
    def get_config(model_type: str, feature: str) -> OnnxConfig:
        """
        Gets the OnnxConfig for a model_type and feature combination.

        Args:
            model_type (`str`):
                The model type to retrieve the config for.
            feature (`str`):
                The feature to retrieve the config for.

        Returns:
            `OnnxConfig`: config for the combination
        """
