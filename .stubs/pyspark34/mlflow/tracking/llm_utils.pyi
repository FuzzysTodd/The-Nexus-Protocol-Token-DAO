from mlflow.tracking.client import MlflowClient as MlflowClient
from mlflow.utils.annotations import experimental as experimental
from typing import Dict, List

def log_predictions(inputs: List[str | Dict[str, str]], outputs: List[str], prompts: List[str | Dict[str, str]]) -> None:
    '''
    Log a batch of inputs, outputs and prompts for the current evaluation run.
    If no run is active, this method will create a new active run.

    :param inputs: Union of either List of input strings or List of input dictionary
    :param outputs: List of output strings
    :param prompts: Union of either List of prompt strings or List of prompt dictionary
    :returns: None

    .. test-code-block:: python
        :caption: Example

        import mlflow

        inputs = [
            {
                "question": "How do I create a Databricks cluster with UC access?",
                "context": "Databricks clusters are ...",
            },
        ]

        outputs = [
            "<Instructions for cluster creation with UC enabled>",
        ]

        prompts = [
            "Get Databricks documentation to answer all the questions: {input}",
        ]


        with mlflow.start_run():
            # Log llm predictions
            mlflow.llm.log_predictions(inputs, outputs, prompts)
    '''
