def remove_retrain(nmask, X_train, y_train, X_test, y_test, attr_test, model_generator, metric, trained_model, random_state):
    """ The model is retrained for each test sample with the important features set to a constant.

    If you want to know how important a set of features is you can ask how the model would be
    different if those features had never existed. To determine this we can mask those features
    across the entire training and test datasets, then retrain the model. If we apply compare the
    output of this retrained model to the original model we can see the effect produced by knowning
    the features we masked. Since for individualized explanation methods each test sample has a
    different set of most important features we need to retrain the model for every test sample
    to get the change in model performance when a specified fraction of the most important features
    are withheld.
    """
def remove_mask(nmask, X_train, y_train, X_test, y_test, attr_test, model_generator, metric, trained_model, random_state):
    """ Each test sample is masked by setting the important features to a constant.
    """
def remove_impute(nmask, X_train, y_train, X_test, y_test, attr_test, model_generator, metric, trained_model, random_state):
    """ The model is revaluated for each test sample with the important features set to an imputed value.

    Note that the imputation is done using a multivariate normality assumption on the dataset. This depends on
    being able to estimate the full data covariance matrix (and inverse) accuractly. So X_train.shape[0] should
    be significantly bigger than X_train.shape[1].
    """
def remove_resample(nmask, X_train, y_train, X_test, y_test, attr_test, model_generator, metric, trained_model, random_state):
    """ The model is revaluated for each test sample with the important features set to resample background values.
    """
def batch_remove_retrain(nmask_train, nmask_test, X_train, y_train, X_test, y_test, attr_train, attr_test, model_generator, metric):
    """ An approximation of holdout that only retraines the model once.

    This is alse called ROAR (RemOve And Retrain) in work by Google. It is much more computationally
    efficient that the holdout method because it masks the most important features in every sample
    and then retrains the model once, instead of retraining the model for every test sample like
    the holdout metric.
    """
def keep_retrain(nkeep, X_train, y_train, X_test, y_test, attr_test, model_generator, metric, trained_model, random_state):
    """ The model is retrained for each test sample with the non-important features set to a constant.

    If you want to know how important a set of features is you can ask how the model would be
    different if only those features had existed. To determine this we can mask the other features
    across the entire training and test datasets, then retrain the model. If we apply compare the
    output of this retrained model to the original model we can see the effect produced by only
    knowning the important features. Since for individualized explanation methods each test sample
    has a different set of most important features we need to retrain the model for every test sample
    to get the change in model performance when a specified fraction of the most important features
    are retained.
    """
def keep_mask(nkeep, X_train, y_train, X_test, y_test, attr_test, model_generator, metric, trained_model, random_state):
    """ The model is revaluated for each test sample with the non-important features set to their mean.
    """
def keep_impute(nkeep, X_train, y_train, X_test, y_test, attr_test, model_generator, metric, trained_model, random_state):
    """ The model is revaluated for each test sample with the non-important features set to an imputed value.

    Note that the imputation is done using a multivariate normality assumption on the dataset. This depends on
    being able to estimate the full data covariance matrix (and inverse) accuractly. So X_train.shape[0] should
    be significantly bigger than X_train.shape[1].
    """
def keep_resample(nkeep, X_train, y_train, X_test, y_test, attr_test, model_generator, metric, trained_model, random_state):
    """ The model is revaluated for each test sample with the non-important features set to resample background values.
    """
def batch_keep_retrain(nkeep_train, nkeep_test, X_train, y_train, X_test, y_test, attr_train, attr_test, model_generator, metric):
    """ An approximation of keep that only retraines the model once.

    This is alse called KAR (Keep And Retrain) in work by Google. It is much more computationally
    efficient that the keep method because it masks the unimportant features in every sample
    and then retrains the model once, instead of retraining the model for every test sample like
    the keep metric.
    """
def local_accuracy(X_train, y_train, X_test, y_test, attr_test, model_generator, metric, trained_model):
    """ The how well do the features plus a constant base rate sum up to the model output.
    """
def to_array(*args): ...
def const_rand(size, seed: int = 23980):
    """ Generate a random array with a fixed seed.
    """
def const_shuffle(arr, seed: int = 23980) -> None:
    """ Shuffle an array in-place with a fixed seed.
    """
def strip_list(attrs):
    """ This assumes that if you have a list of outputs you just want the second one (the second class is the '1' class).
    """
