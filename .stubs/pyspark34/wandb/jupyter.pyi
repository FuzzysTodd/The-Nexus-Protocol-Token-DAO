from IPython.core.magic import Magics
from _typeshed import Incomplete
from typing import Dict
from wandb.sdk.lib import filesystem as filesystem

class Magics: ...

logger: Incomplete

def maybe_display():
    """Display a run if the user added cell magic and we have run."""
def quiet(): ...

class IFrame:
    path: Incomplete
    api: Incomplete
    opts: Incomplete
    displayed: bool
    height: Incomplete
    def __init__(self, path: Incomplete | None = None, opts: Incomplete | None = None) -> None: ...
    def maybe_display(self) -> bool: ...

class WandBMagics(Magics):
    options: Incomplete
    def __init__(self, shell, require_interaction: bool = False) -> None: ...
    def wandb(self, line, cell: Incomplete | None = None) -> None:
        '''Display wandb resources in jupyter.  This can be used as cell or line magic.

        %wandb USERNAME/PROJECT/runs/RUN_ID
        ---
        %%wandb -h 1024
        with wandb.init() as run:
            run.log({"loss": 1})
        '''

def notebook_metadata_from_jupyter_servers_and_kernel_id(): ...
def notebook_metadata(silent: bool) -> Dict[str, str]:
    """Attempt to query jupyter for the path and name of the notebook file.

    This can handle different jupyter environments, specifically:

    1. Colab
    2. Kaggle
    3. JupyterLab
    4. Notebooks
    5. Other?
    """
def jupyter_servers_and_kernel_id():
    """Return a list of servers and the current kernel_id.

    Used to query for the name of the notebook.
    """
def attempt_colab_load_ipynb(): ...
def attempt_kaggle_load_ipynb(): ...
def attempt_colab_login(app_url):
    """This renders an iframe to wandb in the hopes it posts back an api key."""

class Notebook:
    outputs: Incomplete
    settings: Incomplete
    shell: Incomplete
    def __init__(self, settings) -> None: ...
    def save_display(self, exc_count, data_with_metadata) -> None: ...
    def probe_ipynb(self):
        """Return notebook as dict or None."""
    def save_ipynb(self) -> bool: ...
    def save_history(self) -> None:
        """This saves all cell executions in the current session as a new notebook."""
