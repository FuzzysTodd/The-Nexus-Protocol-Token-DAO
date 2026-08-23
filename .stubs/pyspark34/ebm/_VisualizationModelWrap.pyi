from _typeshed import Incomplete
from typing import List

DATAFRAME_UPPER_LIMIT: int

class _VisualizationModelWrap:
    def __init__(self, inner_model) -> None: ...
    @property
    def num_features(self) -> int: ...
    @property
    def feature_names(self) -> List[str]: ...
    @property
    def feature_importances(self) -> List[float]: ...
    @property
    def offset(self) -> float: ...
    def explain_global(self, name: Incomplete | None = None):
        """ Provides global explanation for model.

        Args:
            name: User-defined explanation name.

        Returns:
            An explanation object,
            visualizing feature-value pairs as horizontal bar chart.
        """
    def explain_local(self, df, name: Incomplete | None = None):
        ''' Provides a local explanation for the `DataFrame`.

        To create a local explanation the column `featureScoresCol` should be set in the
        model and added to the `DataFrame`, e.g.:

            model.setFeatureScoresCol("feature_scores")
            transformed_df = model.transform(df)
            wrapper = model.getVizWrapper()
            local_explanation = wrapper.explain_local(transformed_df)

        Args:
            df: Spark Dataframe containing the `featureScoresCol`
            name: User-defined explanation name.

        Returns:
            An explanation object, visualizing feature-value pairs
            for each sample as horizontal bar charts.
        '''

class _RegressionWrap(_VisualizationModelWrap):
    def __init__(self, inner_model) -> None: ...

class _ClassificationWrap(_VisualizationModelWrap):
    def __init__(self, inner_model) -> None: ...
    @property
    def classes(self) -> List[int]: ...
