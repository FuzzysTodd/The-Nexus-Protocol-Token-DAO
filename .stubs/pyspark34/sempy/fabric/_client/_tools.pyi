from sempy._utils._log import log as log
from uuid import UUID

def import_pbix_sample(datasets: str | list[str], workspace: str | UUID | None = None, overwrite: bool | None = False, skip_report: bool | None = True):
    """
    Import .pbix file to the workspace.

    Parameters
    ----------
    datasets : str or list of str
        Name(s) of the dataset(s).
    workspace_id : str
        PowerBI Workspace Name or UUID object containing the workspace ID.
    overwrite : bool, default=False
        Whether to overwrite existing dataset.
    skip_report : bool, default=True
        Whether to skip report import.
    """
def create_lakehouse_if_not_exists(workspace_id, lakehouse_name) -> str: ...
def upload_to_lakehouse(dir_or_file, workspace_id, lakehouse_id, onelake_url, bearer_token, date: str = ''): ...
