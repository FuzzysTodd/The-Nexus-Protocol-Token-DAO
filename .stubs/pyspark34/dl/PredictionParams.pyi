from _typeshed import Incomplete
from pyspark.ml.param import Params

class HasLabelColParam(Params):
    label_col: Incomplete
    def __init__(self) -> None: ...
    def setLabelCol(self, value):
        """
        Sets the value of :py:attr:`label_col`.
        """
    def getLabelCol(self):
        """
        Gets the value of label_col or its default value.
        """

class HasImageColParam(Params):
    image_col: Incomplete
    def __init__(self) -> None: ...
    def setImageCol(self, value):
        """
        Sets the value of :py:attr:`image_col`.
        """
    def getImageCol(self):
        """
        Gets the value of image_col or its default value.
        """

class HasTextColParam(Params):
    text_col: Incomplete
    def __init__(self) -> None: ...
    def setTextCol(self, value):
        """
        Sets the value of :py:attr:`text_col`.
        """
    def getTextCol(self):
        """
        Gets the value of text_col or its default value.
        """

class HasPredictionColParam(Params):
    prediction_col: Incomplete
    def __init__(self) -> None: ...
    def setPredictionCol(self, value):
        """
        Sets the value of :py:attr:`prediction_col`.
        """
    def getPredictionCol(self):
        """
        Gets the value of prediction_col or its default value.
        """

class VisionPredictionParams(HasLabelColParam, HasImageColParam, HasPredictionColParam):
    def __init__(self) -> None: ...

class TextPredictionParams(HasLabelColParam, HasTextColParam, HasPredictionColParam):
    def __init__(self) -> None: ...
