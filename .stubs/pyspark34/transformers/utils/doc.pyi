from _typeshed import Incomplete

def add_start_docstrings(*docstr): ...
def add_start_docstrings_to_model_forward(*docstr): ...
def add_end_docstrings(*docstr): ...

PT_RETURN_INTRODUCTION: str
TF_RETURN_INTRODUCTION: str
FAKE_MODEL_DISCLAIMER: str
PT_TOKEN_CLASSIFICATION_SAMPLE: str
PT_QUESTION_ANSWERING_SAMPLE: str
PT_SEQUENCE_CLASSIFICATION_SAMPLE: str
PT_MASKED_LM_SAMPLE: str
PT_BASE_MODEL_SAMPLE: str
PT_MULTIPLE_CHOICE_SAMPLE: str
PT_CAUSAL_LM_SAMPLE: str
PT_SPEECH_BASE_MODEL_SAMPLE: str
PT_SPEECH_CTC_SAMPLE: str
PT_SPEECH_SEQ_CLASS_SAMPLE: str
PT_SPEECH_FRAME_CLASS_SAMPLE: str
PT_SPEECH_XVECTOR_SAMPLE: str
PT_VISION_BASE_MODEL_SAMPLE: str
PT_VISION_SEQ_CLASS_SAMPLE: str
PT_SAMPLE_DOCSTRINGS: Incomplete
TF_TOKEN_CLASSIFICATION_SAMPLE: str
TF_QUESTION_ANSWERING_SAMPLE: str
TF_SEQUENCE_CLASSIFICATION_SAMPLE: str
TF_MASKED_LM_SAMPLE: str
TF_BASE_MODEL_SAMPLE: str
TF_MULTIPLE_CHOICE_SAMPLE: str
TF_CAUSAL_LM_SAMPLE: str
TF_SPEECH_BASE_MODEL_SAMPLE: str
TF_SPEECH_CTC_SAMPLE: str
TF_VISION_BASE_MODEL_SAMPLE: str
TF_VISION_SEQ_CLASS_SAMPLE: str
TF_SAMPLE_DOCSTRINGS: Incomplete
FLAX_TOKEN_CLASSIFICATION_SAMPLE: str
FLAX_QUESTION_ANSWERING_SAMPLE: str
FLAX_SEQUENCE_CLASSIFICATION_SAMPLE: str
FLAX_MASKED_LM_SAMPLE: str
FLAX_BASE_MODEL_SAMPLE: str
FLAX_MULTIPLE_CHOICE_SAMPLE: str
FLAX_CAUSAL_LM_SAMPLE: str
FLAX_SAMPLE_DOCSTRINGS: Incomplete

def filter_outputs_from_example(docstring, **kwargs):
    """
    Removes the lines testing an output with the doctest syntax in a code sample when it's set to `None`.
    """
def add_code_sample_docstrings(*docstr, processor_class: Incomplete | None = None, checkpoint: Incomplete | None = None, output_type: Incomplete | None = None, config_class: Incomplete | None = None, mask: str = '[MASK]', qa_target_start_index: int = 14, qa_target_end_index: int = 15, model_cls: Incomplete | None = None, modality: Incomplete | None = None, expected_output: Incomplete | None = None, expected_loss: Incomplete | None = None, real_checkpoint: Incomplete | None = None): ...
def replace_return_docstrings(output_type: Incomplete | None = None, config_class: Incomplete | None = None): ...
def copy_func(f):
    """Returns a copy of a function f."""
