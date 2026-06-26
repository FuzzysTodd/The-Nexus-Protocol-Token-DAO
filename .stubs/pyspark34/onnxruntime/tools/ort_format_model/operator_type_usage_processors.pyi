import abc
import ort_flatbuffers_py.fbs as fbs
import typing
from .types import FbsTypeInfo as FbsTypeInfo, value_name_to_typestr as value_name_to_typestr
from _typeshed import Incomplete
from abc import ABC, abstractmethod

class TypeUsageProcessor(ABC, metaclass=abc.ABCMeta):
    """
    Abstract base class for processors which implement operator specific logic to determine the type or types required.
    """
    domain: Incomplete
    optype: Incomplete
    name: Incomplete
    def __init__(self, domain: str, optype: str) -> None: ...
    @abstractmethod
    def process_node(self, node: fbs.Node, value_name_to_typeinfo: dict): ...
    def is_typed_registration_needed(self, type_in_registration: str, globally_allowed_types: typing.Set[str] | None):
        """
        Given the string from a kernel registration, determine if the registration is required or not.
        :param type_in_registration: Type string from kernel registration
        :param globally_allowed_types: Optional set of globally allowed types. If provided, these types take precedence
                                       in determining the required types.
        :return: True is required. False if not.
        """
    def get_cpp_entry(self):
        """
        Get the C++ code that specifies this operator's required types.
        :return: List with any applicable C++ code for this operator's required types. One line per entry.
        """
    @abstractmethod
    def to_config_entry(self):
        """
        Generate a configuration file entry in JSON format with the required types for the operator.
        :return: JSON string with required type information.
        """
    @abstractmethod
    def from_config_entry(self, entry: str):
        """
        Re-create the types required from a configuration file entry created with to_config_entry.
        NOTE: Any existing type information should be cleared prior to re-creating from a config file entry.
        :param entry: Configuration file entry
        """

class DefaultTypeUsageProcessor(TypeUsageProcessor):
    """
    Operator processor which tracks the types used for selected input/s and/or output/s.
    """
    def __init__(self, domain: str, optype: str, inputs: [int] = [0], outputs: [int] = [], required_input_types: typing.Dict[int, typing.Set[str]] = {}, required_output_types: typing.Dict[int, typing.Set[str]] = {}) -> None:
        """
        Create DefaultTypeUsageProcessor. Types for one or more inputs and/or outputs can be tracked by the processor.
        The default is to track the types required for input 0, as this is the most common use case in ONNX.

        Required input and output types may be specified. These are only applicable to is_typed_registration_needed().
        If a registration type matches a required type, the typed registration is needed.
        There is a separate mechanism for specifying required types from C++ for kernels with untyped registration.

        :param domain: Operator domain.
        :param optype: Operator name.
        :param inputs: Inputs to track. Zero based index. May be empty.
        :param outputs: Outputs to track. Zero based index. May be empty.
        :param required_input_types: Required input types. May be empty.
        :param required_output_types: Required output types. May be empty.
        """
    def is_input_type_enabled(self, reg_type, index, allowed_type_set: Incomplete | None = None):
        """Whether input type is enabled based on required and allowed types."""
    def is_output_type_enabled(self, reg_type, index, allowed_type_set: Incomplete | None = None):
        """Whether output type is enabled based on required and allowed types."""
    def process_node(self, node: fbs.Node, value_name_to_typeinfo: dict): ...
    def is_typed_registration_needed(self, type_in_registration: str, globally_allowed_types: typing.Set[str] | None): ...
    def get_cpp_entry(self): ...
    def to_config_entry(self): ...
    def from_config_entry(self, entry: str): ...

class Input1TypedRegistrationProcessor(DefaultTypeUsageProcessor):
    """
    Processor for operators where the second input type is used in a typed kernel registration.
    """
    def __init__(self, domain: str, optype: str) -> None: ...
    def is_typed_registration_needed(self, type_in_registration: str, globally_allowed_types: typing.Set[str] | None): ...

class Output0TypedRegistrationProcessor(DefaultTypeUsageProcessor):
    """
    Processor for operators where the first output type is used in a typed kernel registration.
    """
    def __init__(self, domain: str, optype: str) -> None: ...
    def is_typed_registration_needed(self, type_in_registration: str, globally_allowed_types: typing.Set[str] | None): ...

class OneHotProcessor(TypeUsageProcessor):
    """
    Processor for the OneHot operator, which requires custom logic as the type registration key is a concatenation of
    the three types involved instead of a single type name.
    """
    def __init__(self) -> None: ...
    def process_node(self, node: fbs.Node, value_name_to_typeinfo: dict): ...
    def is_typed_registration_needed(self, type_in_registration: str, globally_allowed_types: typing.Set[str] | None): ...
    def to_config_entry(self): ...
    def from_config_entry(self, entry: str): ...

class OpTypeImplFilterInterface(ABC, metaclass=abc.ABCMeta):
    """
    Class that filters operator implementations based on type.
    """
    @abstractmethod
    def is_typed_registration_needed(self, domain: str, optype: str, type_registration_str: str):
        """
        Given the string from a kernel registration, determine if the registration is required or not.
        :param domain: Operator domain.
        :param optype: Operator type.
        :param type_registration_str: Type string from kernel registration
        :return: True is required. False if not.
        """
    @abstractmethod
    def get_cpp_entries(self):
        """
        Get the C++ code that specifies the operator types to enable.
        :return: List of strings. One line of C++ code per entry.
        """

class OperatorTypeUsageManager:
    """
    Class to manage the operator type usage processors.
    TODO: Currently the type tracking is not specific to a version of the operator.
    It's unclear how/where version specific logic could/should be added, and it would add significant complexity
    to track types on a per-version basis. Not clear there's enough benefit from doing so either.
    """
    def __init__(self) -> None: ...
    def process_node(self, node: fbs.Node, value_name_to_typeinfo: dict):
        """
        Process a Node and record info on the types used.
        :param node: Node from ORT format model
        :param value_name_to_typeinfo: Map of value names to TypeInfo instances
        """
    def get_config_entry(self, domain: str, optype: str):
        """
        Get the config entry specifying the types for this operator.
        :param domain: Operator domain.
        :param optype: Operator type.
        :return: JSON string with type info if available, else None
        """
    def restore_from_config_entry(self, domain: str, optype: str, config_entry: str):
        """
        Restore the per-operator type information from a configuration file entry.
        :param domain: Operator domain.
        :param optype: Operator type.
        :param config_entry: JSON string with type info as created by get_config_entry
        """
    def debug_dump(self) -> None: ...
    class _OpTypeImplFilter(OpTypeImplFilterInterface):
        def __init__(self, manager) -> None: ...
        def is_typed_registration_needed(self, domain: str, optype: str, type_registration_str: str): ...
        def get_cpp_entries(self): ...
    def make_op_type_impl_filter(self):
        """
        Creates an OpTypeImplFilterInterface instance from this manager.
        Filtering uses the manager's operator type usage processor state.
        """

class GloballyAllowedTypesOpTypeImplFilter(OpTypeImplFilterInterface):
    """
    Operator implementation filter which uses globally allowed types.
    """
    def __init__(self, globally_allowed_types: typing.Set[str]) -> None: ...
    def is_typed_registration_needed(self, domain: str, optype: str, type_registration_str: str): ...
    def get_cpp_entries(self): ...
    def global_type_list(self): ...
