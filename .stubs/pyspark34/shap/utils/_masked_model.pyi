from .. import links as links
from _typeshed import Incomplete

class MaskedModel:
    """ This is a utility class that combines a model, a masker object, and a current input.

    The combination of a model, a masker object, and a current input produces a binary set
    function that can be called to mask out any set of inputs. This class attempts to be smart
    about only evaluating the model for background samples when the inputs changed (note this
    requires the masker object to have a .invariants method).
    """
    delta_mask_noop_value: int
    model: Incomplete
    masker: Incomplete
    link: Incomplete
    linearize_link: Incomplete
    args: Incomplete
    def __init__(self, model, masker, link, linearize_link, *args) -> None: ...
    def __call__(self, masks, zero_index: Incomplete | None = None, batch_size: Incomplete | None = None): ...
    @property
    def mask_shapes(self): ...
    def __len__(self) -> int:
        """ How many binary inputs there are to toggle.

        By default we just match what the masker tells us. But if the masker doesn't help us
        out by giving a length then we assume is the number of data inputs.
        """
    def varying_inputs(self): ...
    def main_effects(self, inds: Incomplete | None = None, batch_size: Incomplete | None = None):
        """ Compute the main effects for this model.
        """

def make_masks(cluster_matrix):
    """ Builds a sparse CSR mask matrix from the given clustering.

    This function is optimized since trees for images can be very large.
    """
def link_reweighting(p, link):
    """ Returns a weighting that makes mean(weights*link(p)) == link(mean(p)).

    This is based on a linearization of the link function. When the link function is monotonic then we
    can find a set of positive weights that adjust for the non-linear influence changes on the
    expected value. Note that there are many possible reweightings that can satisfy the above
    property. This function returns the one that has the lowest L2 norm.
    """
