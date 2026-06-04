import lightgbm as lgb
from typing import Any

class LGBMModel(lgb.LGBMModel):
    """Proxy of lightgbm.LGBMModel.

    See: `pydoc lightgbm.LGBMModel`
    """
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class LGBMClassifier(lgb.LGBMClassifier):
    """Proxy of lightgbm.LGBMClassifier.

    See: `pydoc lightgbm.LGBMClassifier`
    """
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class LGBMRegressor(lgb.LGBMRegressor):
    """Proxy of LGBMRegressor.

    See: `pydoc lightgbm.LGBMRegressor`
    """
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
