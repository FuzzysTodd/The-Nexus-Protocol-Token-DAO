from _typeshed import Incomplete
from dataclasses import dataclass
from flaml.automl.task.task import MULTICHOICECLASSIFICATION as MULTICHOICECLASSIFICATION, SEQCLASSIFICATION as SEQCLASSIFICATION, SEQREGRESSION as SEQREGRESSION, SUMMARIZATION as SUMMARIZATION, TOKENCLASSIFICATION as TOKENCLASSIFICATION
from transformers.data.data_collator import DataCollatorWithPadding

@dataclass
class DataCollatorForMultipleChoiceClassification(DataCollatorWithPadding):
    def __call__(self, features): ...

task_to_datacollator_class: Incomplete
