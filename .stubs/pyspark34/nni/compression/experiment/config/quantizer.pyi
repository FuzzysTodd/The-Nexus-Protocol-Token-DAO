from dataclasses import dataclass
from nni.experiment.config.base import ConfigBase as ConfigBase

@dataclass
class QuantizerConfig(ConfigBase):
    """
    A placeholder for quantizer config.
    Use to config the initialization parameters of a quantizer used in the compression experiment.
    """
