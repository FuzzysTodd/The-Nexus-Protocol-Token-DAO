import dataclasses
from _typeshed import Incomplete
from torch.onnx._internal.diagnostics import infra as infra
from typing import Tuple

class _NodeMissingOnnxShapeInference(infra.Rule):
    """Node is missing ONNX shape inference."""
    def format_message(self, op_name) -> str:
        """Returns the formatted default message of this Rule.

        Message template: 'The shape inference of {op_name} type is missing, so it may result in wrong shape inference for the exported graph. Please consider adding it in symbolic function.'
        """
    def format(self, level: infra.Level, op_name) -> Tuple[infra.Rule, infra.Level, str]:
        """Returns a tuple of (Rule, Level, message) for this Rule.

        Message template: 'The shape inference of {op_name} type is missing, so it may result in wrong shape inference for the exported graph. Please consider adding it in symbolic function.'
        """

class _MissingCustomSymbolicFunction(infra.Rule):
    """Missing symbolic function for custom PyTorch operator, cannot translate node to ONNX."""
    def format_message(self, op_name) -> str:
        """Returns the formatted default message of this Rule.

        Message template: 'ONNX export failed on an operator with unrecognized namespace {op_name}. If you are trying to export a custom operator, make sure you registered it with the right domain and version.'
        """
    def format(self, level: infra.Level, op_name) -> Tuple[infra.Rule, infra.Level, str]:
        """Returns a tuple of (Rule, Level, message) for this Rule.

        Message template: 'ONNX export failed on an operator with unrecognized namespace {op_name}. If you are trying to export a custom operator, make sure you registered it with the right domain and version.'
        """

class _MissingStandardSymbolicFunction(infra.Rule):
    """Missing symbolic function for standard PyTorch operator, cannot translate node to ONNX."""
    def format_message(self, op_name, opset_version, issue_url) -> str:
        '''Returns the formatted default message of this Rule.

        Message template: "Exporting the operator \'{op_name}\' to ONNX opset version {opset_version} is not supported. Please feel free to request support or submit a pull request on PyTorch GitHub: {issue_url}."
        '''
    def format(self, level: infra.Level, op_name, opset_version, issue_url) -> Tuple[infra.Rule, infra.Level, str]:
        '''Returns a tuple of (Rule, Level, message) for this Rule.

        Message template: "Exporting the operator \'{op_name}\' to ONNX opset version {opset_version} is not supported. Please feel free to request support or submit a pull request on PyTorch GitHub: {issue_url}."
        '''

class _OperatorSupportedInNewerOpsetVersion(infra.Rule):
    """Operator is supported in newer opset version."""
    def format_message(self, op_name, opset_version, supported_opset_version) -> str:
        '''Returns the formatted default message of this Rule.

        Message template: "Exporting the operator \'{op_name}\' to ONNX opset version {opset_version} is not supported. Support for this operator was added in version {supported_opset_version}, try exporting with this version."
        '''
    def format(self, level: infra.Level, op_name, opset_version, supported_opset_version) -> Tuple[infra.Rule, infra.Level, str]:
        '''Returns a tuple of (Rule, Level, message) for this Rule.

        Message template: "Exporting the operator \'{op_name}\' to ONNX opset version {opset_version} is not supported. Support for this operator was added in version {supported_opset_version}, try exporting with this version."
        '''

class _FxTracerSuccess(infra.Rule):
    """FX Tracer succeeded."""
    def format_message(self, fn_name, tracer_name) -> str:
        '''Returns the formatted default message of this Rule.

        Message template: "The callable \'{fn_name}\' is successfully traced as a \'torch.fx.GraphModule\' by \'{tracer_name}\'."
        '''
    def format(self, level: infra.Level, fn_name, tracer_name) -> Tuple[infra.Rule, infra.Level, str]:
        '''Returns a tuple of (Rule, Level, message) for this Rule.

        Message template: "The callable \'{fn_name}\' is successfully traced as a \'torch.fx.GraphModule\' by \'{tracer_name}\'."
        '''

class _FxTracerFailure(infra.Rule):
    """FX Tracer failed."""
    def format_message(self, fn_name, tracer_name, explanation) -> str:
        '''Returns the formatted default message of this Rule.

        Message template: "The callable \'{fn_name}\' is not successfully traced as a \'torch.fx.GraphModule\' by \'{tracer_name}\'.
{explanation}"
        '''
    def format(self, level: infra.Level, fn_name, tracer_name, explanation) -> Tuple[infra.Rule, infra.Level, str]:
        '''Returns a tuple of (Rule, Level, message) for this Rule.

        Message template: "The callable \'{fn_name}\' is not successfully traced as a \'torch.fx.GraphModule\' by \'{tracer_name}\'.
{explanation}"
        '''

class _FxFrontendAotautograd(infra.Rule):
    """FX Tracer succeeded."""
    def format_message(self, fn_name, tracer_name) -> str:
        '''Returns the formatted default message of this Rule.

        Message template: "The callable \'{fn_name}\' is successfully traced as a \'torch.fx.GraphModule\' by \'{tracer_name}\'."
        '''
    def format(self, level: infra.Level, fn_name, tracer_name) -> Tuple[infra.Rule, infra.Level, str]:
        '''Returns a tuple of (Rule, Level, message) for this Rule.

        Message template: "The callable \'{fn_name}\' is successfully traced as a \'torch.fx.GraphModule\' by \'{tracer_name}\'."
        '''

class _FxPassConvertNegToSigmoid(infra.Rule):
    """FX pass converting torch.neg to torch.sigmoid."""
    def format_message(self) -> str:
        '''Returns the formatted default message of this Rule.

        Message template: "Running \'convert-neg-to-sigmoid\' pass on \'torch.fx.GraphModule\'."
        '''
    def format(self, level: infra.Level) -> Tuple[infra.Rule, infra.Level, str]:
        '''Returns a tuple of (Rule, Level, message) for this Rule.

        Message template: "Running \'convert-neg-to-sigmoid\' pass on \'torch.fx.GraphModule\'."
        '''

class _FxIrAddNode(infra.Rule):
    """ToDo, experimenting diagnostics, placeholder text."""
    def format_message(self) -> str:
        """Returns the formatted default message of this Rule.

        Message template: 'ToDo, experimenting diagnostics, placeholder text.'
        """
    def format(self, level: infra.Level) -> Tuple[infra.Rule, infra.Level, str]:
        """Returns a tuple of (Rule, Level, message) for this Rule.

        Message template: 'ToDo, experimenting diagnostics, placeholder text.'
        """

class _AtenlibSymbolicFunction(infra.Rule):
    """Op level tracking. ToDo, experimenting diagnostics, placeholder text."""
    def format_message(self) -> str:
        """Returns the formatted default message of this Rule.

        Message template: 'ToDo, experimenting diagnostics, placeholder text.'
        """
    def format(self, level: infra.Level) -> Tuple[infra.Rule, infra.Level, str]:
        """Returns a tuple of (Rule, Level, message) for this Rule.

        Message template: 'ToDo, experimenting diagnostics, placeholder text.'
        """

class _AtenlibFxToOnnx(infra.Rule):
    """Graph level tracking. Each op is a step. ToDo, experimenting diagnostics, placeholder text."""
    def format_message(self) -> str:
        """Returns the formatted default message of this Rule.

        Message template: 'ToDo, experimenting diagnostics, placeholder text.'
        """
    def format(self, level: infra.Level) -> Tuple[infra.Rule, infra.Level, str]:
        """Returns a tuple of (Rule, Level, message) for this Rule.

        Message template: 'ToDo, experimenting diagnostics, placeholder text.'
        """

class _FxNodeToOnnx(infra.Rule):
    """Node level tracking. ToDo, experimenting diagnostics, placeholder text."""
    def format_message(self) -> str:
        """Returns the formatted default message of this Rule.

        Message template: 'ToDo, experimenting diagnostics, placeholder text.'
        """
    def format(self, level: infra.Level) -> Tuple[infra.Rule, infra.Level, str]:
        """Returns a tuple of (Rule, Level, message) for this Rule.

        Message template: 'ToDo, experimenting diagnostics, placeholder text.'
        """

class _FxFrontendDynamoMakeFx(infra.Rule):
    """The make_fx + decomposition pass on fx graph produced from Dynamo, before ONNX export."""
    def format_message(self) -> str:
        """Returns the formatted default message of this Rule.

        Message template: 'ToDo, experimenting diagnostics, placeholder text.'
        """
    def format(self, level: infra.Level) -> Tuple[infra.Rule, infra.Level, str]:
        """Returns a tuple of (Rule, Level, message) for this Rule.

        Message template: 'ToDo, experimenting diagnostics, placeholder text.'
        """

class _ArgFormatTooVerbose(infra.Rule):
    """The formatted str for argument to display is too verbose."""
    def format_message(self, length, length_limit, argument_type, formatter_type) -> str:
        """Returns the formatted default message of this Rule.

        Message template: 'Too verbose ({length} > {length_limit}). Argument type {argument_type} for formatter {formatter_type}.'
        """
    def format(self, level: infra.Level, length, length_limit, argument_type, formatter_type) -> Tuple[infra.Rule, infra.Level, str]:
        """Returns a tuple of (Rule, Level, message) for this Rule.

        Message template: 'Too verbose ({length} > {length_limit}). Argument type {argument_type} for formatter {formatter_type}.'
        """

@dataclasses.dataclass
class _POERules(infra.RuleCollection):
    node_missing_onnx_shape_inference: _NodeMissingOnnxShapeInference = ...
    missing_custom_symbolic_function: _MissingCustomSymbolicFunction = ...
    missing_standard_symbolic_function: _MissingStandardSymbolicFunction = ...
    operator_supported_in_newer_opset_version: _OperatorSupportedInNewerOpsetVersion = ...
    fx_tracer_success: _FxTracerSuccess = ...
    fx_tracer_failure: _FxTracerFailure = ...
    fx_frontend_aotautograd: _FxFrontendAotautograd = ...
    fx_pass_convert_neg_to_sigmoid: _FxPassConvertNegToSigmoid = ...
    fx_ir_add_node: _FxIrAddNode = ...
    atenlib_symbolic_function: _AtenlibSymbolicFunction = ...
    atenlib_fx_to_onnx: _AtenlibFxToOnnx = ...
    fx_node_to_onnx: _FxNodeToOnnx = ...
    fx_frontend_dynamo_make_fx: _FxFrontendDynamoMakeFx = ...
    arg_format_too_verbose: _ArgFormatTooVerbose = ...
    def __init__(self) -> None: ...

rules: Incomplete
