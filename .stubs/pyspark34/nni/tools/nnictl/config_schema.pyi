from .common_utils import get_yml_content as get_yml_content, print_warning as print_warning
from .constants import SCHEMA_PATH_ERROR as SCHEMA_PATH_ERROR, SCHEMA_RANGE_ERROR as SCHEMA_RANGE_ERROR, SCHEMA_TYPE_ERROR as SCHEMA_TYPE_ERROR
from _typeshed import Incomplete
from nni.tools.package_utils.tuner_factory import create_validator_instance as create_validator_instance

def setType(key, valueType):
    """check key type"""
def setChoice(key, *args):
    """check choice"""
def setNumberRange(key, keyType, start, end):
    """check number range"""
def setPathCheck(key):
    """check if path exist"""

class AlgoSchema:
    """
    This class is the schema of 'tuner', 'assessor' and 'advisor' sections of experiment configuraion file.
    For example:
    AlgoSchema('tuner') creates the schema of tuner section.
    """
    algo_type: Incomplete
    algo_schema: Incomplete
    builtin_keys: Incomplete
    builtin_name_schema: Incomplete
    customized_keys: Incomplete
    def __init__(self, algo_type) -> None:
        """
        Parameters:
        -----------
        algo_type: str
            One of ['tuner', 'assessor', 'advisor'].
            'tuner': This AlgoSchema class create the schema of tuner section.
            'assessor': This AlgoSchema class create the schema of assessor section.
            'advisor': This AlgoSchema class create the schema of advisor section.
        """
    def validate_class_args(self, class_args, algo_type, builtin_name) -> None: ...
    def missing_customized_keys(self, data): ...
    def validate_extras(self, data, algo_type) -> None: ...
    def validate(self, data) -> None: ...

common_schema: Incomplete
common_trial_schema: Incomplete
pai_yarn_trial_schema: Incomplete
pai_trial_schema: Incomplete
pai_config_schema: Incomplete
dlts_trial_schema: Incomplete
dlts_config_schema: Incomplete
aml_trial_schema: Incomplete
aml_config_schema: Incomplete
hybrid_trial_schema: Incomplete
hybrid_config_schema: Incomplete
adl_trial_schema: Incomplete
kubeflow_trial_schema: Incomplete
kubeflow_config_schema: Incomplete
frameworkcontroller_trial_schema: Incomplete
frameworkcontroller_config_schema: Incomplete
remote_config_schema: Incomplete
machine_list_schema: Incomplete
training_service_schema_dict: Incomplete

class NNIConfigSchema:
    def validate(self, data) -> None: ...
    def validate_extras(self, experiment_config) -> None: ...
    def validate_tuner_adivosr_assessor(self, experiment_config) -> None: ...
    def validate_search_space_content(self, experiment_config) -> None:
        """Validate searchspace content,
        if the searchspace file is not json format or its values does not contain _type and _value which must be specified,
        it will not be a valid searchspace file"""
    def validate_kubeflow_operators(self, experiment_config) -> None:
        """Validate whether the kubeflow operators are valid"""
    def validate_annotation_content(self, experiment_config, spec_key, builtin_name) -> None:
        """
        Valid whether useAnnotation and searchSpacePath is coexist
        spec_key: 'advisor' or 'tuner'
        builtin_name: 'builtinAdvisorName' or 'builtinTunerName'
        """
    def validate_pai_config_path(self, experiment_config) -> None:
        """validate paiConfigPath field"""
    def validate_pai_trial_conifg(self, experiment_config) -> None:
        """validate the trial config in pai platform"""
    def validate_hybrid_platforms(self, experiment_config) -> None: ...
    def validate_frameworkcontroller_trial_config(self, experiment_config) -> None: ...
