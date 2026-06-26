from _typeshed import Incomplete
from pathlib import Path
from torch import Tensor as Tensor
from torch.nn import Module as Module
from typing import Dict, List, Tuple

class Task:
    task_id: Incomplete
    model_path: Incomplete
    masks_path: Incomplete
    config_list_path: Incomplete
    speedup: Incomplete
    finetune: Incomplete
    evaluate: Incomplete
    status: str
    score: Incomplete
    state: Incomplete
    def __init__(self, task_id: int, model_path: str | Path, masks_path: str | Path, config_list_path: str | Path, speedup: bool | None = True, finetune: bool | None = True, evaluate: bool | None = True) -> None:
        """
        Parameters
        ----------
        task_id
            The unique id of task.
        model_path
            The path of the unwrapped pytorch model that will be pruned in this task.
        masks_path
            The path of the masks that applied on the model before pruning.
        config_list_path
            The path of the config list that used in this task.
        speedup
            Control if this task needs speedup, True means use scheduler default value, False means no speedup.
        finetune
            Control if this task needs finetune, True means use scheduler default value, False means no finetune.
        evaluate
            Control if this task needs evaluate, True means use scheduler default value, False means no evaluate.
        """
    def to_dict(self) -> Dict: ...
    def load_data(self) -> Tuple[Module, Dict[str, Dict[str, Tensor]], List[Dict]]:
        """
        Returns
        -------
        Tuple[Module, Dict[str, Dict[str, Tensor]], List[Dict]]
            Return the model pruning in this task, the masks of the model before pruning,
            the config list used in this task.
        """
    def referenced_paths(self) -> List[str | Path]:
        """
        Return the path list that need to count reference in this task.
        """
    def clean_up(self) -> None:
        """
        Counter of referenced file paths subtract 1. If the counter reach 0, then delete the file.
        """

class TaskResult:
    task_id: Incomplete
    compact_model: Incomplete
    compact_model_masks: Incomplete
    pruner_generated_masks: Incomplete
    score: Incomplete
    def __init__(self, task_id: int | str, compact_model: Module, compact_model_masks: Dict[str, Dict[str, Tensor]], pruner_generated_masks: Dict[str, Dict[str, Tensor]], score: float | None) -> None:
        """
        Parameters
        ----------
        task_id
            The unique id of task.
        compact_model
            The unwrapped compact pytorch model after pruning. If the compact model has been speeduped during the pruning process,
            it will have a smaller structure compare with the model before pruning.
            If the compact model has not been speeduped, it will have the same structure with the model before pruning.
        compact_model_masks
            The masks on the compact model. If the compact model has been speeduped during the pruning process,
            the `compact_model_masks` is always an empty dict. If the compact model has not been speeduped,
            the `compact_model_masks` is same as `pruner_generated_masks`.
        pruner_generated_masks
            The masks that can apply on the before pruning model. It is always the output of `pruner.compress()`.
            TODO: If the compact model has been speeduped, the auto infer masks maybe also need.
        score
            The score of the pruning effect. i.e., the accuracy or latency after pruning.
        """

class BasePruningScheduler:
    def generate_task(self) -> Task | None:
        """
        Returns
        -------
        Optional[Task]
            Return the next pruning task.
        """
    def record_task_result(self, task_result: TaskResult):
        """
        Parameters
        ----------
        task_result
            The result of the task
        """
    def pruning_one_step(self, task: Task) -> TaskResult:
        """
        Pruning the model defined in task.

        Parameters
        ----------
        task
            The pruning task in this step.

        Returns
        -------
        TaskResult
            Return the result of the task in this step.
        """
    def get_best_result(self) -> Tuple[int, Module, Dict[str, Dict[str, Tensor]], float, List[Dict]]:
        """
        Returns
        -------
        Tuple[int, Module, Dict[str, Dict[str, Tensor]], float, List[Dict]]
            Return the task result that has the best performance,
            inculde task id, the compact model, the masks on the compact model, score and config list used in this task.
        """
    def compress(self) -> None:
        """
        The pruning schedule main loop.
        """
