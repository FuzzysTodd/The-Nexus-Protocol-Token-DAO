from _typeshed import Incomplete
from transformers.models.marian.convert_marian_to_pytorch import FRONT_MATTER_TEMPLATE as FRONT_MATTER_TEMPLATE, convert as convert, convert_opus_name_to_hf_name as convert_opus_name_to_hf_name, download_and_unzip as download_and_unzip, get_system_metadata as get_system_metadata
from typing import Tuple

DEFAULT_REPO: str
DEFAULT_MODEL_DIR: Incomplete
LANG_CODE_URL: str
ISO_URL: str
ISO_PATH: str
LANG_CODE_PATH: str
TATOEBA_MODELS_URL: str

class TatoebaConverter:
    """
    Convert Tatoeba-Challenge models to huggingface format.

    Steps:

        1. Convert numpy state dict to hf format (same code as OPUS-MT-Train conversion).
        2. Rename opus model to huggingface format. This means replace each alpha3 code with an alpha2 code if a unique
           one exists. e.g. aav-eng -> aav-en, heb-eng -> he-en
        3. Select the best model for a particular pair, parse the yml for it and write a model card. By default the
           best model is the one listed first in released-model-results, but it's also possible to specify the most
           recent one.
    """
    model_results: Incomplete
    alpha3_to_alpha2: Incomplete
    model_card_dir: Incomplete
    tag2name: Incomplete
    def __init__(self, save_dir: str = 'marian_converted') -> None: ...
    def convert_models(self, tatoeba_ids, dry_run: bool = False) -> None: ...
    def expand_group_to_two_letter_codes(self, grp_name): ...
    def is_group(self, code, name): ...
    def get_tags(self, code, name): ...
    def resolve_lang_code(self, src, tgt) -> Tuple[str, str]: ...
    @staticmethod
    def model_type_info_from_model_name(name): ...
    def write_model_card(self, model_dict, dry_run: bool = False) -> str:
        """
        Construct card from data parsed from YAML and the model's name. upload command: aws s3 sync model_card_dir
        s3://models.huggingface.co/bert/Helsinki-NLP/ --dryrun
        """
    def download_lang_info(self) -> None: ...
    def parse_metadata(self, model_name, repo_path=..., method: str = 'best'): ...

GROUP_MEMBERS: Incomplete

def l2front_matter(langs): ...
def dedup(lst):
    """Preservers order"""
