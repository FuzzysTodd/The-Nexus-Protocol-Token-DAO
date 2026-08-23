import torch
from .conv_utils import conv_args_and_kwargs as conv_args_and_kwargs, conv_backward as conv_backward, conv_input_for_string_padding as conv_input_for_string_padding, conv_picker as conv_picker
from .expanded_weights_impl import ExpandedWeight as ExpandedWeight, implements_per_sample_grads as implements_per_sample_grads
from .expanded_weights_utils import forward_helper as forward_helper

class ConvPerSampleGrad(torch.autograd.Function):
    @staticmethod
    def forward(ctx, kwarg_names, conv_fn, *expanded_args_and_kwargs): ...
    @staticmethod
    def backward(ctx, grad_output): ...
