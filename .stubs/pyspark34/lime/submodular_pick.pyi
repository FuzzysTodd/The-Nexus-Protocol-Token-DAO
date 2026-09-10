from _typeshed import Incomplete

class SubmodularPick:
    """Class for submodular pick

    Saves a representative sample of explanation objects using SP-LIME,
    as well as saving all generated explanations

    First, a collection of candidate explanations are generated
    (see explain_instance). From these candidates, num_exps_desired are
    chosen using submodular pick. (see marcotcr et al paper)."""
    explanations: Incomplete
    sp_explanations: Incomplete
    V: Incomplete
    def __init__(self, explainer, data, predict_fn, method: str = 'sample', sample_size: int = 1000, num_exps_desired: int = 5, num_features: int = 10, **kwargs) -> None:
        """
        Args:
            data: a numpy array where each row is a single input into predict_fn
            predict_fn: prediction function. For classifiers, this should be a
                    function that takes a numpy array and outputs prediction
                    probabilities. For regressors, this takes a numpy array and
                    returns the predictions. For ScikitClassifiers, this is
                    `classifier.predict_proba()`. For ScikitRegressors, this
                    is `regressor.predict()`. The prediction function needs to work
                    on multiple feature vectors (the vectors randomly perturbed
                    from the data_row).
            method: The method to use to generate candidate explanations
                    method == 'sample' will sample the data uniformly at
                    random. The sample size is given by sample_size. Otherwise
                    if method == 'full' then explanations will be generated for the
                    entire data. l
            sample_size: The number of instances to explain if method == 'sample'
            num_exps_desired: The number of explanation objects returned
            num_features: maximum number of features present in explanation


        Sets value:
            sp_explanations: A list of explanation objects that has a high coverage
            explanations: All the candidate explanations saved for potential future use.
              """
