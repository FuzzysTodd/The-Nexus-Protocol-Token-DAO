from .operator_type_usage_processors import OperatorTypeUsageManager as OperatorTypeUsageManager

class OrtFormatModelProcessor:
    """Class to process an ORT format model and determine required operators and types."""
    def __init__(self, model_path: str, required_ops: dict, processors: OperatorTypeUsageManager) -> None:
        """
        Initialize ORT format model processor
        :param model_path: Path to model to load
        :param required_ops: Dictionary required operator information will be added to.
        :param processors: Operator type usage processors which will be called for each matching Node.
        """
    def process(self) -> None: ...
