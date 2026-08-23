from _typeshed import Incomplete
from torch import nn

class ProjectedAdaptiveLogSoftmax(nn.Module):
    n_token: Incomplete
    d_embed: Incomplete
    d_proj: Incomplete
    cutoffs: Incomplete
    cutoff_ends: Incomplete
    div_val: Incomplete
    shortlist_size: Incomplete
    n_clusters: Incomplete
    head_size: Incomplete
    cluster_weight: Incomplete
    cluster_bias: Incomplete
    out_layers: Incomplete
    out_projs: Incomplete
    keep_order: Incomplete
    def __init__(self, n_token, d_embed, d_proj, cutoffs, div_val: int = 1, keep_order: bool = False) -> None: ...
    def forward(self, hidden, labels: Incomplete | None = None, keep_order: bool = False):
        """
        Params:
            hidden :: [len*bsz x d_proj]
            labels :: [len*bsz

        Return:
            if labels is None: out :: [len*bsz x n_tokens] log probabilities of tokens over the vocabulary else: out ::
            [(len-1)*bsz] Negative log likelihood. We could replace this implementation by the native PyTorch one if
            theirs had an option to set bias on all clusters in the native one. here:
            https://github.com/pytorch/pytorch/blob/dbe6a7a9ff1a364a8706bf5df58a1ca96d2fd9da/torch/nn/modules/adaptive.py#L138
        """
    def log_prob(self, hidden):
        """
        Computes log probabilities for all \\\\(n\\_classes\\\\) From:
        https://github.com/pytorch/pytorch/blob/master/torch/nn/modules/adaptive.p

        Args:
            hidden (Tensor): a minibatch of example

        Returns:
            log-probabilities of for each class \\\\(c\\\\) in range \\\\(0 <= c <= n\\_classes\\\\), where \\\\(n\\_classes\\\\) is
            a parameter passed to `AdaptiveLogSoftmaxWithLoss` constructor. Shape:

            - Input: \\\\((N, in\\_features)\\\\)
            - Output: \\\\((N, n\\_classes)\\\\)
        """
