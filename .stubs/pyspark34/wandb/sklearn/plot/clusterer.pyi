from _typeshed import Incomplete
from wandb.sklearn import calculate as calculate, utils as utils

def clusterer(model, X_train, cluster_labels, labels: Incomplete | None = None, model_name: str = 'Clusterer') -> None:
    '''Generates all sklearn clusterer plots supported by W&B.

    The following plots are generated:
        elbow curve, silhouette plot.

    Should only be called with a fitted clusterer (otherwise an error is thrown).

    Arguments:
        model: (clusterer) Takes in a fitted clusterer.
        X_train: (arr) Training set features.
        cluster_labels: (list) Names for cluster labels. Makes plots easier to read
                            by replacing cluster indexes with corresponding names.
        labels: (list) Named labels for target varible (y). Makes plots easier to
                        read by replacing target values with corresponding index.
                        For example if `labels=[\'dog\', \'cat\', \'owl\']` all 0s are
                        replaced by dog, 1s by cat.
        model_name: (str) Model name. Defaults to \'Clusterer\'

    Returns:
        None: To see plots, go to your W&B run page then expand the \'media\' tab
              under \'auto visualizations\'.

    Example:
    ```python
    wandb.sklearn.plot_clusterer(kmeans, X, cluster_labels, labels, "KMeans")
    ```
    '''
def elbow_curve(clusterer: Incomplete | None = None, X: Incomplete | None = None, cluster_ranges: Incomplete | None = None, n_jobs: int = 1, show_cluster_time: bool = True) -> None:
    """Measures and plots variance explained as a function of the number of clusters.

    Useful in picking the optimal number of clusters.

    Should only be called with a fitted clusterer (otherwise an error is thrown).

    Please note this function fits the model on the training set when called.

    Arguments:
        model: (clusterer) Takes in a fitted clusterer.
        X: (arr) Training set features.

    Returns:
        None: To see plots, go to your W&B run page then expand the 'media' tab
              under 'auto visualizations'.

    Example:
    ```python
    wandb.sklearn.plot_elbow_curve(model, X_train)
    ```
    """
def silhouette(clusterer: Incomplete | None = None, X: Incomplete | None = None, cluster_labels: Incomplete | None = None, labels: Incomplete | None = None, metric: str = 'euclidean', kmeans: bool = True) -> None:
    '''Measures & plots silhouette coefficients.

    Silhouette coefficients near +1 indicate that the sample is far away from
    the neighboring clusters. A value near 0 indicates that the sample is on or
    very close to the decision boundary between two neighboring clusters and
    negative values indicate that the samples might have been assigned to the wrong cluster.

    Should only be called with a fitted clusterer (otherwise an error is thrown).

    Please note this function fits the model on the training set when called.

    Arguments:
        model: (clusterer) Takes in a fitted clusterer.
        X: (arr) Training set features.
        cluster_labels: (list) Names for cluster labels. Makes plots easier to read
                               by replacing cluster indexes with corresponding names.

    Returns:
        None: To see plots, go to your W&B run page then expand the \'media\' tab
              under \'auto visualizations\'.

    Example:
    ```python
    wandb.sklearn.plot_silhouette(model, X_train, ["spam", "not spam"])
    ```
    '''
