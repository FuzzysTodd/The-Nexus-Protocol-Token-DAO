import abc
import torch
import torch.nn as nn
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from torch.ao.quantization.fake_quantize import FakeQuantize as FakeQuantize
from torch.ao.quantization.fx._equalize import EqualizationQConfig as EqualizationQConfig, default_equalization_qconfig as default_equalization_qconfig
from torch.ao.quantization.fx._model_report.model_report_observer import ModelReportObserver as ModelReportObserver
from torch.ao.quantization.fx.graph_module import GraphModule as GraphModule
from torch.ao.quantization.observer import ObserverBase as ObserverBase, default_dynamic_quant_observer as default_dynamic_quant_observer, default_observer as default_observer, default_per_channel_weight_observer as default_per_channel_weight_observer, default_weight_observer as default_weight_observer
from torch.ao.quantization.qconfig import QConfig as QConfig, default_qconfig as default_qconfig
from typing import Any, Callable, Dict, Set, Tuple

DETECTOR_TARGET_NODE_KEY: str
DETECTOR_OBS_TO_INSERT_KEY: str
DETECTOR_IS_POST_OBS_KEY: str
DETECTOR_OBS_ARGS_KEY: str

class DetectorQConfigInfo:
    """
    This class contains the QConfig information for a single module.
    The list of variables / values this contains can grow depending on the
    extensibility of the qconfig mapping feature set but this currently includes:
    - if activation observer is dynamic
    - if weight observer is per channel


    Args:
        module_fqn (str): The fully qualified name (fqn) of the module that this
            information contains info relevant to qconfig for
    """
    module_fqn: Incomplete
    is_activation_dynamic: bool
    is_weight_per_channel: bool
    is_equalization_recommended: bool
    def __init__(self, module_fqn: str) -> None: ...
    def generate_quantization_qconfig(self, module: torch.nn.Module) -> QConfig:
        """
        Args:
            module (torch.nn.Module) The module we are generating
            the qconfig for

        Returns the generated quantization QConfig according to what a valid configuration is
        """
    def generate_equalization_qconfig(self) -> EqualizationQConfig:
        """
        This returns the equalization configuration for a module.

        For now, it just returns the default, but as more equalization options become
        possible, this method can get more fleshed out with more nuanced granularity.


        Returns the generated equalization QConfig according to what a valid configuration is
        """

class DetectorBase(ABC, metaclass=abc.ABCMeta):
    """ Base Detector Module
    Any detector class should derive from this class.

    Concrete detectors should follow the same general API, which includes:
    - A method to calculate and return observer insertion points
        - Should return both the fqns and the Observer class to insert
    - A method to return a report based on the the detector
        - Should return a str-based report and dict info in Tuple[str,Dict] format
    """
    detector_config_info: Incomplete
    def __init__(self) -> None: ...
    @abstractmethod
    def determine_observer_insert_points(self, model) -> Dict:
        """
        Args
            model (nn.Module or subclass): model to find observer insertion points

        Returns a Dict mapping from unique observer fqns (where we want to insert them) to a Dict.
            This dict maps string keys to detector specific information
        """
    @abstractmethod
    def get_detector_name(self) -> str:
        """ Returns the name of the current detector """
    @abstractmethod
    def get_qconfig_info(self, model) -> Dict[str, DetectorQConfigInfo]:
        """ Returns the DetectorQConfigInfo for each module_fqn relavent
        Args
            model (nn.Module or subclass): model to find observer insertion points

        Returns a Dict mapping from unique observer fqns (where we want to insert them) to:
            A DetectorQConfigInfo with the information to generate a QConfig for a specific module
        """
    @abstractmethod
    def generate_detector_report(self, model) -> Tuple[str, Dict[str, Any]]:
        """
        Args
            model (nn.Module or subclass): model to find observer insertion points

        Returns a Tuple of two elements:
            Str: string report of the suggested improvements
            Dict: contains useful data collected by the observer pertinent to this report
        """

class PerChannelDetector(DetectorBase):
    """ This class is used to detect if any Linear or Conv layers in a model utilize per_channel quantization.
        Only Linear and Conv layers can use per_channel as of now so only these two are currently checked.

        per_channel quantization can lead to major benefits in the form of accuracy.
        Therefore, if the backend used by the user supports it, it is recommended to use

        Args:
            backend (str, optional): the backend the user wishes to use in production
                Default value is current torch.backends.quantized.engine
    """
    BACKEND_KEY: str
    PER_CHAN_SUPPORTED_KEY: str
    PER_CHAN_USED_KEY: str
    DEFAULT_BACKEND_PER_CHANNEL_SUPPORTED_MODULES: Dict[str, Set[Any]]
    backend_chosen: Incomplete
    supported_modules: Incomplete
    def __init__(self, backend: str = ...) -> None: ...
    def get_detector_name(self) -> str:
        """ returns the string name of this detector"""
    def get_qconfig_info(self, model) -> Dict[str, DetectorQConfigInfo]:
        """ Returns the DetectorQConfigInfo for each module_fqn relavent
        Args
            model (nn.Module or subclass): model to find observer insertion points

        Returns a Dict mapping from unique observer fqns (where we want to insert them) to:
            A DetectorQConfigInfo with the information to generate a QConfig for a specific module
        """
    def determine_observer_insert_points(self, model: nn.Module) -> Dict:
        """
        There is no observers inserted for the PerChannelDetector.

        Returns an empty dictionary since no observers are added or needed
        """
    def generate_detector_report(self, model: nn.Module) -> Tuple[str, Dict[str, Any]]:
        """Checks if any Linear or Conv layers in the model utilize per_channel quantization.
        Only Linear and Conv layers can use per_channel as of now so only these two are currently checked.

        Looks at q_config format and backend to determine if per_channel can be utilized.
        Uses the DEFAULT_BACKEND_PER_CHANNEL_SUPPORTED_MODULES structure to determine support

        Args:
            model: The prepared and calibrated model we want to check if using per_channel

        Returns a tuple with two elements:
            String report of potential actions to improve model (if per_channel quantization is available in backend)
            Dictionary mapping per_channel quantizable elements to:
                whether per_channel quantization is supported by the backend
                if it is being utilized in the current model
        """

class DynamicStaticDetector(DetectorBase):
    """
    Determines whether dynamic or static quantization is more appropriate for a given module.

    Takes advantage of the ModelReportObserver that records range information.
    Stationary distribution of data are strictly above tolerance level for the comparison statistic:

        S = average_batch_activation_range/epoch_activation_range

    Nonstationary distributions are below or at the tolerance level for this metric.

    If the distribution of data right after the module is non-stationary, recommend dynamic quantization
        Otherwise recommend static quantization

    Args:
        tolerance (float, optional): The threshold where S metric is stationary above and non-stationary otherwise. Default: 0.5
    """
    DEFAULT_PRE_OBSERVER_NAME: str
    DEFAULT_POST_OBSERVER_NAME: str
    STATIONARY_STR: str
    NON_STATIONARY_STR: str
    INPUT_ACTIVATION_PREFIX: str
    OUTPUT_ACTIVATION_PREFIX: str
    TOLERANCE_KEY: str
    DEFAULT_DYNAMIC_REC_KEY: str
    PRE_OBS_COMP_STAT_KEY: Incomplete
    POST_OBS_COMP_STAT_KEY: Incomplete
    PRE_OBS_DATA_DIST_KEY: Incomplete
    POST_OBS_DATA_DIST_KEY: Incomplete
    IS_CURRENTLY_SUPPORTED_KEY: str
    DEFAULT_DYNAMIC_STATIC_CHECK_SUPPORTED: Incomplete
    DEFAULT_DYNAMIC_STATIC_FUTURE_SUPPORTED: Incomplete
    tolerance: Incomplete
    useful_observer_fqns: Incomplete
    def __init__(self, tolerance: float = 0.5) -> None: ...
    def determine_observer_insert_points(self, prepared_fx_model: GraphModule) -> Dict[str, Dict[str, Any]]:
        '''
        Determines where observers need to be inserted for the Dynamic vs Static detector.
        For this detector, we want to place observers on either side of linear layers in the model.

        Currently inserts observers for:
            linear layers

        Args:
            prepared_fx_model (GraphModule):  The prepared Fx GraphModule

        Returns a Dict mapping from unique observer fqns (where we want to insert them) to a Dict with:
            key "target_node" -> the node we are trying to observe with this observer (torch.fx.node.Node)
            key "observer_to_insert" -> the observer we wish to insert (ObserverBase)
            key "is_post_observer" -> True if this is meant to be a post-observer for target_node, False if pre-observer
            key "observer_args" -> The arguments that are meant to be passed into the observer
        '''
    def get_detector_name(self) -> str:
        """ returns the string name of this detector"""
    def get_qconfig_info(self, model) -> Dict[str, DetectorQConfigInfo]:
        """ Returns the DetectorQConfigInfo for each module_fqn relavent
        Args
            model (nn.Module or subclass): model to find observer insertion points

        Returns a Dict mapping from unique observer fqns (where we want to insert them) to:
            A DetectorQConfigInfo with the information to generate a QConfig for a specific module
        """
    def generate_detector_report(self, model: GraphModule) -> Tuple[str, Dict[str, Any]]:
        """
        Determines whether dynamic or static quantization is more appropriate for a given module.

        Takes advantage of the ModelReportObserver that records range information.
        Stationary distribution of data are strictly above tolerance level for the comparison statistic:

            S = average_batch_activation_range/epoch_activation_range

        Nonstationary distributions are below or at the tolerance level for this metric.

        If the distribution of data right after the module is non-stationary, recommend dynamic quantization
            Otherwise recommend static quantization

        This will then generate suggestions for dynamic vs static quantization focused around Linear.

        Args:
            model (GraphModule): The prepared and calibrated GraphModule with inserted ModelReportObservers

        Returns a tuple with two elements:
            String report of of whether dynamic or static quantization is recommended for certain modules
            Dictionary mapping modules with ModelReportObservers around them to:
                whether dynamic quantization is recommended
                their S metric of input to module
                whether input to module is stationary or non-stationary
                their S metric of output of module
                whether output of module is stationary or non-stationary
                the tolerance level to decided whether input/output is stationary or non-stationary
                whether it is currently supported or planned for the future
        """

class InputWeightEqualizationDetector(DetectorBase):
    """
    Determines whether input-weight equalization can help improve quantization for certain modules.

    Specifically, this list of modules includes:
        linear
        conv

    Determines whether input-weight equalization is recommended based on the comp stat:
        s_c = sqrt(w_c/W)/sqrt(i_c/I)
        where:
            w_c is range of weight for channel c, W is range of weight over all channels
            i_c is range of input for channel c, I is range of input over all channels

        if s_c >= threshold or <= 1 / threshold, recommends input-weight equalization

    Args:
        ratio_threshold (float): The threshold for s_c to determine if input-weight equalization is sugggested
            Should be between 0 and 1 (both non-inclusive)
        ch_axis (int, optional): The channel axis being observed to determine input weight equalization
            Default: 1

    * :attr:`ratio_threshold`: The threshold for s_c to determine if input-weight equalization is sugggested
        Should be between 0 and 1

    * :attr:`ch_axis`: The channel axis being observed to determine input weight equalization

    * :attr:`SUPPORTED_MODULES`: This specifies the modules that are supported for input-weight equalization

    * :attr:`DEFAULT_PRE_OBSERVER_NAME`: The name of the pre-observer to be inserted for this detector
    """
    SUPPORTED_MODULES: Set[Callable]
    DEFAULT_PRE_OBSERVER_NAME: str
    WEIGHT_PREFIX: str
    ACTIVATION_PREFIX: str
    PER_CHANNEL_MAX_KEY: str
    PER_CHANNEL_MIN_KEY: str
    GLOBAL_MAX_KEY: str
    GLOBAL_MIN_KEY: str
    RECOMMENDED_KEY: str
    COMP_METRIC_KEY: str
    THRESHOLD_KEY: str
    CHANNEL_KEY: str
    WEIGHT_STR: str
    INPUT_STR: str
    DEFAULT_RECOMMEND_INPUT_WEIGHT_CHANNEL_RATIO: float
    ratio_threshold: Incomplete
    ch_axis: Incomplete
    def __init__(self, ratio_threshold: float, ch_axis: int = 1) -> None: ...
    def get_qconfig_info(self, model) -> Dict[str, DetectorQConfigInfo]:
        """ Returns the DetectorQConfigInfo for each module_fqn relavent
        Args
            model (nn.Module or subclass): model to find observer insertion points

        Returns a Dict mapping from unique observer fqns (where we want to insert them) to:
            A DetectorQConfigInfo with the information to generate a QConfig for a specific module
        """
    def determine_observer_insert_points(self, prepared_fx_model: GraphModule) -> Dict[str, Dict[str, Any]]:
        '''Determines where observers need to be inserted for the Input Weight Equalization Detector.
        For this detector, we want to place observers in front of supported layers.

        Currently inserts observers for:
            linear layers
            conv layers

        Args:
            prepared_fx_model (GraphModule):  The prepared Fx GraphModule

        Returns a Dict mapping from unique observer fqns (where we want to insert them) to a Dict with:
            key "target_node" -> the node we are trying to observe with this observer (torch.fx.node.Node)
            key "observer_to_insert" -> the observer we wish to insert (ObserverBase)
            key "is_post_observer" -> True if this is meant to be a post-observer for target_node, False if pre-observer
            key "observer_args" -> The arguments that are meant to be passed into the observer
        '''
    def get_detector_name(self) -> str:
        """Returns the name of this detector"""
    def generate_detector_report(self, model: GraphModule) -> Tuple[str, Dict[str, Any]]:
        """
        Determines whether input weight equalization is appropriate for a given module.

        Takes advantage of the ModelReport Observer which records per channel information of input range
        It then uses the passed in weight info inconjunction to compute the desired ratio
        Finally, it gives suggestions based on this information for each module of interest

        Args:
            model (GraphModule): The prepared and calibrated GraphModule with inserted ModelReportObservers

        Returns a tuple with two elements:
            String report of of whether input weight equalization is recommended for certain modules
            Dictionary mapping modules of interest to:
                whether input weight equalization is recommended
                their s_c metric compared to the threshold
                the threshold used to make the recommendation
                the channel used for recording data
                the input channel range info
                the weight channel range info
        """

class OutlierDetector(DetectorBase):
    '''
    Determines whether there are significant outliers in activation data around a certain layer.

    This is ideally used in conjunction with information on stationary vs. non-stationary distribution:
        If the data is stationary, and there are significant outliers, then we want to flag them
        We want to do this on a per channel basis for detecting outliers

    Determines whether activation data is flagged as outlier based on if data is stationary and:
        p_r = avg(100th percentile / "reference_percentile"th percentile)
        where:
            p_r is average percentile ratio across all batches in the epoch
            reference_percentile is a percentile values between 0 and 100 exclusive

        if p_r is above some threshold, then we consider the activations to have significant outliers

    Args:
        ratio_threshold (float, optional): The threshold for p_r to determine if there are outliers in activations
            Should be >= 1
            Default: 3.5
        reference_percentile (float, optional): The denominator to find the relative scale of the 100th percentile
            Should be between 0 and 1
            Default: 0.975
        fraction_batches_used_threshold (float, optional): Threshold of fraction of batches per channel to determine outlier
            If fraction is below this, we deem number of samples used to calculate outliers as insignificant and alert user
            regardless of whether we detected outliers or not in channel to take a closer look at channel results
            Should be between 0 and 1
            Default: 0.95
        ch_axis (int, optional): The channel axis being observed to determine input weight equalization
            Default: 1

    * :attr:`ratio_threshold`: The threshold for p_r to determine if there are outliers in activations
        The p_r value (average ratio of 100th percentile/reference_percentile) is compared to ratio_threshold
        If it is significantly greater, then we consider it an outlier
        This threshold was calculated based on the ratio of the percentiles in a normal distribution
        The calculations behind value choice: https://drive.google.com/file/d/1N2wdtXWI-kOH8S7HH4-PYB_NmqzZil4p/view?usp=sharing

    * :attr:`reference_percentile`: The denominator of the top fraction to find the relative scale of the 100th percentile
        Should be between 0 and 1
        The calculations behind value choice: https://drive.google.com/file/d/1N2wdtXWI-kOH8S7HH4-PYB_NmqzZil4p/view?usp=sharing

    * :attr:`fraction_batches_used_threshold`: The fraction of batches to determine outliers for each channel should be above this
        Some batches may not be used because of 0-based errors, so this is to ensure a good amount of the total batches are used
        Should be between 0 and 1

    * :attr:`ch_axis`: The channel axis being observed to determine outliers

    * :attr:`DEFAULT_PRE_OBSERVER_NAME`: The name of the pre-observer to be inserted for this detector
    '''
    DEFAULT_PRE_OBSERVER_NAME: str
    INPUT_ACTIVATION_PREFIX: str
    OUTLIER_KEY: str
    NUM_BATCHES_KEY: str
    IS_SUFFICIENT_BATCHES_KEY: str
    COMP_METRIC_KEY: str
    RATIO_THRES_KEY: str
    REF_PERCENTILE_KEY: str
    CHANNEL_AXIS_KEY: str
    MAX_VALS_KEY: Incomplete
    CONSTANT_COUNTS_KEY: str
    ratio_threshold: Incomplete
    reference_percentile: Incomplete
    fraction_batches_used_threshold: Incomplete
    ch_axis: Incomplete
    def __init__(self, ratio_threshold: float = 3.5, reference_percentile: float = 0.975, fraction_batches_used_threshold: float = 0.95, ch_axis: int = 1) -> None: ...
    def get_detector_name(self) -> str:
        """Returns the name of this detector"""
    def get_qconfig_info(self, model) -> Dict[str, DetectorQConfigInfo]:
        """ Returns the DetectorQConfigInfo for each module_fqn relavent
        Args
            model (nn.Module or subclass): model to find observer insertion points

        Returns a Dict mapping from unique observer fqns (where we want to insert them) to:
            A DetectorQConfigInfo with the information to generate a QConfig for a specific module
        """
    def determine_observer_insert_points(self, prepared_fx_model: GraphModule) -> Dict[str, Dict[str, Any]]:
        ''' Determines where observers need to be inserted for the Outlier Detector.

        For this detector, we want to place observers in front of supported layers.

        Currently inserts observers for:
            all layers that do not have children (leaf level layers)

        Args:
            prepared_fx_model (GraphModule):  The prepared Fx GraphModule

        Returns a Dict mapping from unique observer fqns (where we want to insert them) to a Dict with:
            key "target_node" -> the node we are trying to observe with this observer (torch.fx.node.Node)
            key "observer_to_insert" -> the observer we wish to insert (ObserverBase)
            key "is_post_observer" -> True if this is meant to be a post-observer for target_node, False if pre-observer
            key "observer_args" -> The arguments that are meant to be passed into the observer
        '''
    def generate_detector_report(self, model: GraphModule) -> Tuple[str, Dict[str, Any]]:
        """
        Determines whether input weight equalization is appropriate for a given module.

        Takes advantage of the ModelReport Observer which records the relavent percentile information

        Args:
            model (GraphModule): The prepared and calibrated GraphModule with inserted ModelReportObservers

        Returns a tuple with two elements:
            String report of of whether there are outliers in the activations around certain modules
            Dictionary mapping modules of interest to:
                whether there were outliers found in activation before
                the number of batches used for each channel
                whether fraction of applicable batches used is above fraction_batches_used_threshold
                their p_r metric compared to the threshold
                the threshold used to make the recommendation
                the reference_percentile used to make the recommendation
                the channel axis used to determine individual channels
                the constant batch counts per channel
                the per channel max values
        """
