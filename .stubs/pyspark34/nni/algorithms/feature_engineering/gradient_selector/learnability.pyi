import torch
import torch.nn as nn
from . import constants as constants, syssettings as syssettings
from .fginitialize import ChunkDataLoader as ChunkDataLoader
from _typeshed import Incomplete

sparsetensor: Incomplete

def def_train_opt(p):
    """
    Return the default optimizer.
    """
def revcumsum(U):
    """
    Reverse cumulative sum for faster performance.
    """
def triudr(X, r): ...
def triudl(X, l): ...

class ramp(torch.autograd.Function):
    """
    Ensures input is between 0 and 1
    """
    @staticmethod
    def forward(ctx, input_data): ...
    @staticmethod
    def backward(ctx, grad_output): ...

class safesqrt(torch.autograd.Function):
    """
    Square root without dividing by 0.
    """
    @staticmethod
    def forward(ctx, input_data): ...
    @staticmethod
    def backward(ctx, grad_output): ...

class LearnabilityMB(nn.Module):
    '''
    Calculates the learnability of a set of features.
    mini-batch version w/ "left" and "right" multiplies
    '''
    order: Incomplete
    a: Incomplete
    binary: Incomplete
    def __init__(self, Nminibatch, D, coeff, groups: Incomplete | None = None, binary: bool = False, device=...) -> None: ...
    def ret_val(self, z):
        """
        Get the return value based on z.
        """
    def forward(self, s, X, y): ...

class Solver(nn.Module):
    """
    Class that performs the main optimization.
    Keeps track of the current x and iterates through data to learn x given the penalty and order.
    """
    groups: Incomplete
    soft_D: Incomplete
    soft_groups: Incomplete
    Nminibatch: Incomplete
    accum_steps: Incomplete
    ftransform: Incomplete
    x: Incomplete
    max_norm: Incomplete
    device: Incomplete
    verbose: Incomplete
    multiclass: Incomplete
    n_classes: Incomplete
    balanced: Incomplete
    ordinal: Incomplete
    ds_train: Incomplete
    f_train: Incomplete
    opt_train: Incomplete
    it: int
    iters_per_epoch: Incomplete
    w: Incomplete
    def __init__(self, PreparedData, order, Nminibatch: Incomplete | None = None, groups: Incomplete | None = None, soft_groups: Incomplete | None = None, x0: Incomplete | None = None, C: int = 1, ftransform=..., get_train_opt=..., accum_steps: int = 1, rng=..., max_norm_clip: float = 1.0, shuffle: bool = True, device=..., verbose: int = 1) -> None:
        """

        Parameters
        ----------
        PreparedData : Dataset of PrepareData class
        order : int
            What order of interactions to include. Higher orders
            may be more accurate but increase the run time. 12 is the maximum allowed order.
        Nminibatch : int
            Number of rows in a mini batch
        groups : array-like
            Optional, shape = [n_features]
            Groups of columns that must be selected as a unit
            e.g. [0, 0, 1, 2] specifies the first two columns are part of a group.
        soft_groups : array-like
            optional, shape = [n_features]
            Groups of columns come from the same source
            Used to encourage sparsity of number of sources selected
            e.g. [0, 0, 1, 2] specifies the first two columns are part of a group.
        x0 : torch.tensor
            Optional, initialization of x.
        C : float
            Penalty parameter.
        get_train_opt : function
            Function that returns a pytorch optimizer, Adam is the default
        accum_steps : int
            Number of steps
        rng : random state
        max_norm_clip : float
            Maximum allowable size of the gradient
        shuffle : bool
            Whether or not to shuffle data within the dataloader
        order : int
            What order of interactions to include. Higher orders
            may be more accurate but increase the run time. 12 is the maximum allowed order.
        penalty : int
            Constant that multiplies the regularization term.
        ftransform : function
            Function to transform the x. sigmoid is the default.
        device : str
            'cpu' to run on CPU and 'cuda' to run on GPU. Runs much faster on GPU
        verbose : int
            Controls the verbosity when fitting. Set to 0 for no printing
            1 or higher for printing every verbose number of gradient steps.
        """
    def penalty(self, s):
        """
        Calculate L1 Penalty.
        """
    def forward_and_backward(self, s, xsub, ysub, retain_graph: bool = False):
        """
        Completes the forward operation and computes gradients for learnability and penalty.
        """
    def combine_gradient(self, g1, g2):
        """
        Combine gradients from learnability and penalty

        Parameters
        ----------
        g1 : array-like
            gradient from learnability
        g2 : array-like
            gradient from penalty
        """
    def combine_loss(self, f_train, pen):
        """
        Combine the learnability and L1 penalty.
        """
    def transform_y_into_binary(self, ysub, target_class):
        """
        Transforms multiclass classification problems into a binary classification problem.
        """
    def train(self, f_callback: Incomplete | None = None, f_stop: Incomplete | None = None) -> None:
        """
        Trains the estimator to determine which features to include.

        Parameters
        ----------
        f_callback : function
            Function that performs a callback
        f_stop: function
            Function that tells you when to stop
        """
