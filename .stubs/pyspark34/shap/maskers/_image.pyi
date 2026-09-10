from .._serializable import Deserializer as Deserializer, Serializer as Serializer
from ..utils import assert_import as assert_import, record_import_error as record_import_error, safe_isinstance as safe_isinstance
from ..utils._exceptions import DimensionError as DimensionError
from ._masker import Masker as Masker
from _typeshed import Incomplete

class Image(Masker):
    """ This masks out image regions with blurring or inpainting.
    """
    input_shape: Incomplete
    input_mask_value: Incomplete
    shape: Incomplete
    image_data: bool
    blur_kernel: Incomplete
    mask_value: Incomplete
    fixed_background: Incomplete
    last_xid: Incomplete
    immutable_outputs: bool
    def __init__(self, mask_value, shape: Incomplete | None = None) -> None:
        ''' Build a new Image masker with the given masking value.
        Parameters
        ----------
        mask_value : np.array, "blur(kernel_xsize, kernel_xsize)", "inpaint_telea", or "inpaint_ns"
            The value used to mask hidden regions of the image.
        shape : None or tuple
            If the mask_value is an auto-generated masker instead of a dataset then the input
            image shape needs to be provided.
        '''
    def __call__(self, mask, x): ...
    def inpaint(self, x, mask, method):
        """ Fill in the masked parts of the image through inpainting.
        """
    clustering: Incomplete
    def build_partition_tree(self) -> None:
        """ This partitions an image into a herarchical clustering based on axis-aligned splits.
        """
    def save(self, out_file) -> None:
        """ Write a Image masker to a file stream.
        """
    @classmethod
    def load(cls, in_file, instantiate: bool = True):
        """ Load a Image masker from a file stream.
        """
