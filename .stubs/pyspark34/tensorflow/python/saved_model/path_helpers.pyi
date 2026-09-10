from tensorflow.python.lib.io import file_io as file_io
from tensorflow.python.saved_model import constants as constants
from tensorflow.python.util import compat as compat

def get_or_create_variables_dir(export_dir):
    """Return variables sub-directory, or create one if it doesn't exist."""
def get_variables_dir(export_dir):
    """Return variables sub-directory in the SavedModel."""
def get_variables_path(export_dir):
    """Return the variables path, used as the prefix for checkpoint files."""
def get_or_create_assets_dir(export_dir):
    """Return assets sub-directory, or create one if it doesn't exist."""
def get_assets_dir(export_dir):
    """Return path to asset directory in the SavedModel."""
def get_or_create_debug_dir(export_dir):
    """Returns path to the debug sub-directory, creating if it does not exist."""
def get_saved_model_pbtxt_path(export_dir): ...
def get_saved_model_pb_path(export_dir): ...
def get_debug_dir(export_dir):
    """Returns path to the debug sub-directory in the SavedModel."""
