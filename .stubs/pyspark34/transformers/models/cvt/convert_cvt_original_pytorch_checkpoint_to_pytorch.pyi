from transformers import AutoFeatureExtractor as AutoFeatureExtractor, CvtConfig as CvtConfig, CvtForImageClassification as CvtForImageClassification

def embeddings(idx):
    """
    The function helps in renaming embedding layer weights.

    Args:
        idx: stage number in original model
    """
def attention(idx, cnt):
    """
    The function helps in renaming attention block layers weights.

    Args:
        idx: stage number in original model
        cnt: count of blocks in each stage
    """
def cls_token(idx):
    """
    Function helps in renaming cls_token weights
    """
def final():
    """
    Function helps in renaming final classification layer
    """
def convert_cvt_checkpoint(cvt_model, image_size, cvt_file_name, pytorch_dump_folder) -> None:
    """
    Fucntion to convert the microsoft cvt checkpoint to huggingface checkpoint
    """
