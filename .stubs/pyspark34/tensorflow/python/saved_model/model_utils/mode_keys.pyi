from tensorflow.python.util.compat import collections_abc as collections_abc

class KerasModeKeys:
    """Standard names for model modes.

  The following standard keys are defined:

  * `TRAIN`: training/fitting mode.
  * `TEST`: testing/evaluation mode.
  * `PREDICT`: prediction/inference mode.
  """
    TRAIN: str
    TEST: str
    PREDICT: str

class EstimatorModeKeys:
    """Standard names for Estimator model modes.

  The following standard keys are defined:

  * `TRAIN`: training/fitting mode.
  * `EVAL`: testing/evaluation mode.
  * `PREDICT`: predication/inference mode.
  """
    TRAIN: str
    EVAL: str
    PREDICT: str

def is_predict(mode): ...
def is_eval(mode): ...
def is_train(mode): ...

class ModeKeyMap(collections_abc.Mapping):
    '''Map using ModeKeys as keys.

  This class creates an immutable mapping from modes to values. For example,
  SavedModel export of Keras and Estimator models use this to map modes to their
  corresponding MetaGraph tags/SignatureDef keys.

  Since this class uses modes, rather than strings, as keys, both "predict"
  (Keras\'s PREDICT ModeKey) and "infer" (Estimator\'s PREDICT ModeKey) map to the
  same value.
  '''
    def __init__(self, **kwargs) -> None: ...
    def __getitem__(self, key): ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
