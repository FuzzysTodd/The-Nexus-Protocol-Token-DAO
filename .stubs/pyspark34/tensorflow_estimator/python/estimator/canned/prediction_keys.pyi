class PredictionKeys:
    """Enum for canonical model prediction keys.

  The following values are defined:
  PREDICTIONS: Used by models that predict values, such as regressor models.
  """
    CLASSES: str
    CLASS_IDS: str
    ALL_CLASSES: str
    ALL_CLASS_IDS: str
    LOGISTIC: str
    LOGITS: str
    PREDICTIONS: str
    PROBABILITIES: str
    TOP_K: str
