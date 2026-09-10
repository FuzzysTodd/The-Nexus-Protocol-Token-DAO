from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from _typeshed import Incomplete

logger: Incomplete
LXMERT_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class LxmertConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`LxmertModel`] or a [`TFLxmertModel`]. It is used
    to instantiate a LXMERT model according to the specified arguments, defining the model architecture. Instantiating
    a configuration with the defaults will yield a similar configuration to that of the Lxmert
    [unc-nlp/lxmert-base-uncased](https://huggingface.co/unc-nlp/lxmert-base-uncased) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
        vocab_size (`int`, *optional*, defaults to 30522):
            Vocabulary size of the LXMERT model. Defines the number of different tokens that can be represented by the
            `inputs_ids` passed when calling [`LxmertModel`] or [`TFLxmertModel`].
        hidden_size (`int`, *optional*, defaults to 768):
            Dimensionality of the encoder layers and the pooler layer.
        r_layers (`int`, *optional*, defaults to 5):
            Number of hidden layers in the Transformer visual encoder.
        l_layers (`int`, *optional*, defaults to 9):
            Number of hidden layers in the Transformer language encoder.
        x_layers (`int`, *optional*, defaults to 5):
            Number of hidden layers in the Transformer cross modality encoder.
        num_attention_heads (`int`, *optional*, defaults to 5):
            Number of attention heads for each attention layer in the Transformer encoder.
        intermediate_size (`int`, *optional*, defaults to 3072):
            Dimensionality of the "intermediate" (often named feed-forward) layer in the Transformer encoder.
        hidden_act (`str` or `Callable`, *optional*, defaults to `"gelu"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"silu"` and `"gelu_new"` are supported.
        hidden_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        attention_probs_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout ratio for the attention probabilities.
        max_position_embeddings (`int`, *optional*, defaults to 512):
            The maximum sequence length that this model might ever be used with. Typically set this to something large
            just in case (e.g., 512 or 1024 or 2048).
        type_vocab_size (`int`, *optional*, defaults to 2):
            The vocabulary size of the *token_type_ids* passed into [`BertModel`].
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-12):
            The epsilon used by the layer normalization layers.
        visual_feat_dim (`int`, *optional*, defaults to 2048):
            This represents the last dimension of the pooled-object features used as input for the model, representing
            the size of each object feature itself.
        visual_pos_dim (`int`, *optional*, defaults to 4):
            This represents the number of spacial features that are mixed into the visual features. The default is set
            to 4 because most commonly this will represent the location of a bounding box. i.e., (x, y, width, height)
        visual_loss_normalizer (`float`, *optional*, defaults to 1/15):
            This represents the scaling factor in which each visual loss is multiplied by if during pretraining, one
            decided to train with multiple vision-based loss objectives.
        num_qa_labels (`int`, *optional*, defaults to 9500):
            This represents the total number of different question answering (QA) labels there are. If using more than
            one dataset with QA, the user will need to account for the total number of labels that all of the datasets
            have in total.
        num_object_labels (`int`, *optional*, defaults to 1600):
            This represents the total number of semantically unique objects that lxmert will be able to classify a
            pooled-object feature as belonging too.
        num_attr_labels (`int`, *optional*, defaults to 400):
            This represents the total number of semantically unique attributes that lxmert will be able to classify a
            pooled-object feature as possessing.
        task_matched (`bool`, *optional*, defaults to `True`):
            This task is used for sentence-image matching. If the sentence correctly describes the image the label will
            be 1. If the sentence does not correctly describe the image, the label will be 0.
        task_mask_lm (`bool`, *optional*, defaults to `True`):
            Whether or not to add masked language modeling (as used in pretraining models such as BERT) to the loss
            objective.
        task_obj_predict (`bool`, *optional*, defaults to `True`):
            Whether or not to add object prediction, attribute prediction and feature regression to the loss objective.
        task_qa (`bool`, *optional*, defaults to `True`):
            Whether or not to add the question-answering loss to the objective
        visual_obj_loss (`bool`, *optional*, defaults to `True`):
            Whether or not to calculate the object-prediction loss objective
        visual_attr_loss (`bool`, *optional*, defaults to `True`):
            Whether or not to calculate the attribute-prediction loss objective
        visual_feat_loss (`bool`, *optional*, defaults to `True`):
            Whether or not to calculate the feature-regression loss objective
        output_attentions (`bool`, *optional*, defaults to `False`):
            Whether or not the model should return the attentions from the vision, language, and cross-modality layers
            should be returned.
        output_hidden_states (`bool`, *optional*, defaults to `False`):
            Whether or not the model should return the hidden states from the vision, language, and cross-modality
            layers should be returned.
    '''
    model_type: str
    attribute_map: Incomplete
    vocab_size: Incomplete
    hidden_size: Incomplete
    num_attention_heads: Incomplete
    hidden_act: Incomplete
    intermediate_size: Incomplete
    hidden_dropout_prob: Incomplete
    attention_probs_dropout_prob: Incomplete
    max_position_embeddings: Incomplete
    type_vocab_size: Incomplete
    initializer_range: Incomplete
    layer_norm_eps: Incomplete
    num_qa_labels: Incomplete
    num_object_labels: Incomplete
    num_attr_labels: Incomplete
    l_layers: Incomplete
    x_layers: Incomplete
    r_layers: Incomplete
    visual_feat_dim: Incomplete
    visual_pos_dim: Incomplete
    visual_loss_normalizer: Incomplete
    task_matched: Incomplete
    task_mask_lm: Incomplete
    task_obj_predict: Incomplete
    task_qa: Incomplete
    visual_obj_loss: Incomplete
    visual_attr_loss: Incomplete
    visual_feat_loss: Incomplete
    num_hidden_layers: Incomplete
    def __init__(self, vocab_size: int = 30522, hidden_size: int = 768, num_attention_heads: int = 12, num_qa_labels: int = 9500, num_object_labels: int = 1600, num_attr_labels: int = 400, intermediate_size: int = 3072, hidden_act: str = 'gelu', hidden_dropout_prob: float = 0.1, attention_probs_dropout_prob: float = 0.1, max_position_embeddings: int = 512, type_vocab_size: int = 2, initializer_range: float = 0.02, layer_norm_eps: float = 1e-12, l_layers: int = 9, x_layers: int = 5, r_layers: int = 5, visual_feat_dim: int = 2048, visual_pos_dim: int = 4, visual_loss_normalizer: float = 6.67, task_matched: bool = True, task_mask_lm: bool = True, task_obj_predict: bool = True, task_qa: bool = True, visual_obj_loss: bool = True, visual_attr_loss: bool = True, visual_feat_loss: bool = True, **kwargs) -> None: ...
