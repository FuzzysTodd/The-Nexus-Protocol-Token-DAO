from ..base import TransformerMixin as TransformerMixin
from ..utils import metadata_routing as metadata_routing
from ..utils.validation import check_is_fitted as check_is_fitted
from _typeshed import Incomplete

class AgglomerationTransform(TransformerMixin):
    """
    A class for feature agglomeration via the transform interface.
    """
    def transform(self, X):
        """
        Transform a new matrix using the built clustering.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features) or                 (n_samples, n_samples)
            A M by N array of M observations in N dimensions or a length
            M array of M one-dimensional observations.

        Returns
        -------
        Y : ndarray of shape (n_samples, n_clusters) or (n_clusters,)
            The pooled values for each feature cluster.
        """
    def inverse_transform(self, Xt: Incomplete | None = None, Xred: Incomplete | None = None):
        """
        Inverse the transformation and return a vector of size `n_features`.

        Parameters
        ----------
        Xt : array-like of shape (n_samples, n_clusters) or (n_clusters,)
            The values to be assigned to each cluster of samples.

        Xred : deprecated
            Use `Xt` instead.

            .. deprecated:: 1.3

        Returns
        -------
        X : ndarray of shape (n_samples, n_features) or (n_features,)
            A vector of size `n_samples` with the values of `Xred` assigned to
            each of the cluster of samples.
        """
