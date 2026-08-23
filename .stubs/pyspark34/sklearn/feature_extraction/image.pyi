from ..base import BaseEstimator, TransformerMixin
from _typeshed import Incomplete

__all__ = ['PatchExtractor', 'extract_patches_2d', 'grid_to_graph', 'img_to_graph', 'reconstruct_from_patches_2d']

def img_to_graph(img, *, mask: Incomplete | None = None, return_as=..., dtype: Incomplete | None = None):
    """Graph of the pixel-to-pixel gradient connections.

    Edges are weighted with the gradient values.

    Read more in the :ref:`User Guide <image_feature_extraction>`.

    Parameters
    ----------
    img : array-like of shape (height, width) or (height, width, channel)
        2D or 3D image.
    mask : ndarray of shape (height, width) or             (height, width, channel), dtype=bool, default=None
        An optional mask of the image, to consider only part of the
        pixels.
    return_as : np.ndarray or a sparse matrix class,             default=sparse.coo_matrix
        The class to use to build the returned adjacency matrix.
    dtype : dtype, default=None
        The data of the returned sparse matrix. By default it is the
        dtype of img.

    Returns
    -------
    graph : ndarray or a sparse matrix class
        The computed adjacency matrix.

    Notes
    -----
    For scikit-learn versions 0.14.1 and prior, return_as=np.ndarray was
    handled by returning a dense np.matrix instance.  Going forward, np.ndarray
    returns an np.ndarray, as expected.

    For compatibility, user code relying on this method should wrap its
    calls in ``np.asarray`` to avoid type issues.
    """
def grid_to_graph(n_x, n_y, n_z: int = 1, *, mask: Incomplete | None = None, return_as=..., dtype=...):
    """Graph of the pixel-to-pixel connections.

    Edges exist if 2 voxels are connected.

    Parameters
    ----------
    n_x : int
        Dimension in x axis.
    n_y : int
        Dimension in y axis.
    n_z : int, default=1
        Dimension in z axis.
    mask : ndarray of shape (n_x, n_y, n_z), dtype=bool, default=None
        An optional mask of the image, to consider only part of the
        pixels.
    return_as : np.ndarray or a sparse matrix class,             default=sparse.coo_matrix
        The class to use to build the returned adjacency matrix.
    dtype : dtype, default=int
        The data of the returned sparse matrix. By default it is int.

    Returns
    -------
    graph : np.ndarray or a sparse matrix class
        The computed adjacency matrix.

    Notes
    -----
    For scikit-learn versions 0.14.1 and prior, return_as=np.ndarray was
    handled by returning a dense np.matrix instance.  Going forward, np.ndarray
    returns an np.ndarray, as expected.

    For compatibility, user code relying on this method should wrap its
    calls in ``np.asarray`` to avoid type issues.
    """
def extract_patches_2d(image, patch_size, *, max_patches: Incomplete | None = None, random_state: Incomplete | None = None):
    '''Reshape a 2D image into a collection of patches.

    The resulting patches are allocated in a dedicated array.

    Read more in the :ref:`User Guide <image_feature_extraction>`.

    Parameters
    ----------
    image : ndarray of shape (image_height, image_width) or         (image_height, image_width, n_channels)
        The original image data. For color images, the last dimension specifies
        the channel: a RGB image would have `n_channels=3`.

    patch_size : tuple of int (patch_height, patch_width)
        The dimensions of one patch.

    max_patches : int or float, default=None
        The maximum number of patches to extract. If `max_patches` is a float
        between 0 and 1, it is taken to be a proportion of the total number
        of patches. If `max_patches` is None it corresponds to the total number
        of patches that can be extracted.

    random_state : int, RandomState instance, default=None
        Determines the random number generator used for random sampling when
        `max_patches` is not None. Use an int to make the randomness
        deterministic.
        See :term:`Glossary <random_state>`.

    Returns
    -------
    patches : array of shape (n_patches, patch_height, patch_width) or         (n_patches, patch_height, patch_width, n_channels)
        The collection of patches extracted from the image, where `n_patches`
        is either `max_patches` or the total number of patches that can be
        extracted.

    Examples
    --------
    >>> from sklearn.datasets import load_sample_image
    >>> from sklearn.feature_extraction import image
    >>> # Use the array data from the first image in this dataset:
    >>> one_image = load_sample_image("china.jpg")
    >>> print(\'Image shape: {}\'.format(one_image.shape))
    Image shape: (427, 640, 3)
    >>> patches = image.extract_patches_2d(one_image, (2, 2))
    >>> print(\'Patches shape: {}\'.format(patches.shape))
    Patches shape: (272214, 2, 2, 3)
    >>> # Here are just two of these patches:
    >>> print(patches[1])
    [[[174 201 231]
      [174 201 231]]
     [[173 200 230]
      [173 200 230]]]
    >>> print(patches[800])
    [[[187 214 243]
      [188 215 244]]
     [[187 214 243]
      [188 215 244]]]
    '''
def reconstruct_from_patches_2d(patches, image_size):
    """Reconstruct the image from all of its patches.

    Patches are assumed to overlap and the image is constructed by filling in
    the patches from left to right, top to bottom, averaging the overlapping
    regions.

    Read more in the :ref:`User Guide <image_feature_extraction>`.

    Parameters
    ----------
    patches : ndarray of shape (n_patches, patch_height, patch_width) or         (n_patches, patch_height, patch_width, n_channels)
        The complete set of patches. If the patches contain colour information,
        channels are indexed along the last dimension: RGB patches would
        have `n_channels=3`.

    image_size : tuple of int (image_height, image_width) or         (image_height, image_width, n_channels)
        The size of the image that will be reconstructed.

    Returns
    -------
    image : ndarray of shape image_size
        The reconstructed image.
    """

class PatchExtractor(TransformerMixin, BaseEstimator):
    '''Extracts patches from a collection of images.

    Read more in the :ref:`User Guide <image_feature_extraction>`.

    .. versionadded:: 0.9

    Parameters
    ----------
    patch_size : tuple of int (patch_height, patch_width), default=None
        The dimensions of one patch. If set to None, the patch size will be
        automatically set to `(img_height // 10, img_width // 10)`, where
        `img_height` and `img_width` are the dimensions of the input images.

    max_patches : int or float, default=None
        The maximum number of patches per image to extract. If `max_patches` is
        a float in (0, 1), it is taken to mean a proportion of the total number
        of patches. If set to None, extract all possible patches.

    random_state : int, RandomState instance, default=None
        Determines the random number generator used for random sampling when
        `max_patches is not None`. Use an int to make the randomness
        deterministic.
        See :term:`Glossary <random_state>`.

    See Also
    --------
    reconstruct_from_patches_2d : Reconstruct image from all of its patches.

    Notes
    -----
    This estimator is stateless and does not need to be fitted. However, we
    recommend to call :meth:`fit_transform` instead of :meth:`transform`, as
    parameter validation is only performed in :meth:`fit`.

    Examples
    --------
    >>> from sklearn.datasets import load_sample_images
    >>> from sklearn.feature_extraction import image
    >>> # Use the array data from the second image in this dataset:
    >>> X = load_sample_images().images[1]
    >>> X = X[None, ...]
    >>> print(f"Image shape: {X.shape}")
    Image shape: (1, 427, 640, 3)
    >>> pe = image.PatchExtractor(patch_size=(10, 10))
    >>> pe_trans = pe.transform(X)
    >>> print(f"Patches shape: {pe_trans.shape}")
    Patches shape: (263758, 10, 10, 3)
    >>> X_reconstructed = image.reconstruct_from_patches_2d(pe_trans, X.shape[1:])
    >>> print(f"Reconstructed shape: {X_reconstructed.shape}")
    Reconstructed shape: (427, 640, 3)
    '''
    patch_size: Incomplete
    max_patches: Incomplete
    random_state: Incomplete
    def __init__(self, *, patch_size: Incomplete | None = None, max_patches: Incomplete | None = None, random_state: Incomplete | None = None) -> None: ...
    def fit(self, X, y: Incomplete | None = None):
        """Only validate the parameters of the estimator.

        This method allows to: (i) validate the parameters of the estimator  and
        (ii) be consistent with the scikit-learn transformer API.

        Parameters
        ----------
        X : ndarray of shape (n_samples, image_height, image_width) or                 (n_samples, image_height, image_width, n_channels)
            Array of images from which to extract patches. For color images,
            the last dimension specifies the channel: a RGB image would have
            `n_channels=3`.

        y : Ignored
            Not used, present for API consistency by convention.

        Returns
        -------
        self : object
            Returns the instance itself.
        """
    def transform(self, X):
        """Transform the image samples in `X` into a matrix of patch data.

        Parameters
        ----------
        X : ndarray of shape (n_samples, image_height, image_width) or                 (n_samples, image_height, image_width, n_channels)
            Array of images from which to extract patches. For color images,
            the last dimension specifies the channel: a RGB image would have
            `n_channels=3`.

        Returns
        -------
        patches : array of shape (n_patches, patch_height, patch_width) or                 (n_patches, patch_height, patch_width, n_channels)
            The collection of patches extracted from the images, where
            `n_patches` is either `n_samples * max_patches` or the total
            number of patches that can be extracted.
        """
