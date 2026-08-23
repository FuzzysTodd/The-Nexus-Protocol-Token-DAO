def multiclass_postprocess_RESTORE_THIS(X_binned, feature_graphs, binned_predict_proba, feature_types):
    '''Postprocesses multiclass model graphs with desired properties.

    Args:
        X_binned: Training dataset, pre-binned. Contains integer values, 0+. Each value is a unique bin.
        feature_graphs: List of 2d numpy arrays. List is size d for d features. Each numpy array is of size b for b bins in the feature. Each bin has k elements for k classes.
        binned_predict_proba: Function that takes in X_binned, returns 2d numpy array of predictions. Each row in the return vector has k elements, with probability of belonging to class k.
        feature_types: List of strings "nominal" or "ordinal" or "continuous" for each feature.

    Returns:
        Dictionary with updated model graphs and new intercepts.
    '''
def multiclass_postprocess(n_classes, term_scores, bin_weights, intercept) -> None:
    """Postprocesses multiclass model graphs with desired properties."""
