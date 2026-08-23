from .ort_format_model import GloballyAllowedTypesOpTypeImplFilter as GloballyAllowedTypesOpTypeImplFilter, OperatorTypeUsageManager as OperatorTypeUsageManager

have_flatbuffers: bool

def parse_config(config_file: str, enable_type_reduction: bool = False):
    '''
    Parse the configuration file and return the required operators dictionary and an
    OpTypeImplFilterInterface instance.

    Configuration file lines can do the following:
    1. specify required operators
    2. specify globally allowed types for all operators
    3. specify what it means for no required operators to be specified

    1. Specifying required operators

    The basic format for specifying required operators is `domain;opset1,opset2;op1,op2...`
    e.g. `ai.onnx;11;Add,Cast,Clip,... for a single opset
         `ai.onnx;11,12;Add,Cast,Clip,... for multiple opsets

         note: Configuration information is accrued as the file is parsed. If an operator requires support from multiple
         opsets that can be done with one entry for each opset, or one entry with multiple opsets in it.

    If the configuration file is generated from ORT format models it may optionally contain JSON for per-operator
    type reduction. The required types are generally listed per input and/or output of the operator.
    The type information is in a map, with \'inputs\' and \'outputs\' keys. The value for \'inputs\' or \'outputs\' is a map
    between the index number of the input/output and the required list of types.

    For example, both the input and output types are relevant to ai.onnx:Cast.
    Type information for input 0 and output 0 could look like this:
        `{"inputs": {"0": ["float", "int32_t"]}, "outputs": {"0": ["float", "int64_t"]}}`

    which is added directly after the operator name in the configuration file.
    e.g.
        `ai.onnx;12;Add,Cast{"inputs": {"0": ["float", "int32_t"]}, "outputs": {"0": ["float", "int64_t"]}},Concat`

    If for example the types of inputs 0 and 1 were important, the entry may look like this (e.g. ai.onnx:Gather):
        `{"inputs": {"0": ["float", "int32_t"], "1": ["int32_t"]}}`

    Finally some operators do non-standard things and store their type information under a \'custom\' key.
    ai.onnx.OneHot is an example of this, where the three input types are combined into a triple.
        `{"custom": [["float", "int64_t", "int64_t"], ["int64_t", "std::string", "int64_t"]]}`

    2. Specifying globally allowed types for all operators

    The format for specifying globally allowed types for all operators is:
        `!globally_allowed_types;T0,T1,...`

    Ti should be a C++ scalar type supported by ONNX and ORT.
    At most one globally allowed types specification is allowed.

    Specifying per-operator type information and specifying globally allowed types are mutually exclusive - it is an
    error to specify both.

    3. Specify what it means for no required operators to be specified

    By default, if no required operators are specified, NO operators are required.

    With the following line, if no required operators are specified, ALL operators are required:
        `!no_ops_specified_means_all_ops_are_required`

    :param config_file: Configuration file to parse
    :param enable_type_reduction: Set to True to use the type information in the config.
                                  If False the type information will be ignored.
                                  If the flatbuffers module is unavailable type information will be ignored as the
                                  type-based filtering has a dependency on the ORT flatbuffers schema.
    :return: required_ops: Dictionary of domain:opset:[ops] for required operators. If None, all operators are
                           required.
             op_type_impl_filter: OpTypeImplFilterInterface instance if type reduction is enabled, the flatbuffers
                                  module is available, and type reduction information is present. None otherwise.
    '''
