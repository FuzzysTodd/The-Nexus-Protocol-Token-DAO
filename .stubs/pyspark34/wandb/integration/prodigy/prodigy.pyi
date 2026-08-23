from wandb import util as util
from wandb.plots.utils import test_missing as test_missing

def named_entity(docs):
    """Create a named entity visualization.

    Taken from https://github.com/wandb/wandb/blob/main/wandb/plots/named_entity.py.
    """
def merge(dict1, dict2):
    """Return a new dictionary by merging two dictionaries recursively."""
def get_schema(list_data_dict, struct, array_dict_types):
    """Get a schema of the dataset's structure and data types."""
def standardize(item, structure, array_dict_types) -> None:
    """Standardize all rows/entries in dataset to fit the schema.

    Will look for missing values and fill it in so all rows have
    the same items and structure.
    """
def create_table(data):
    """Create a W&B Table.

    - Create/decode images from URL/Base64
    - Uses spacy to translate NER span data to visualizations.
    """
def upload_dataset(dataset_name) -> None:
    """Upload dataset from local database to Weights & Biases.

    Args:
        dataset_name: The name of the dataset in the Prodigy database.
    """
