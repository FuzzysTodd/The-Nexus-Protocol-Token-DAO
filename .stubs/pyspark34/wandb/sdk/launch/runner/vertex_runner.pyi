from .._project_spec import LaunchProject as LaunchProject, get_entry_point_command as get_entry_point_command
from ..builder.build import get_env_vars_dict as get_env_vars_dict
from ..environment.gcp_environment import GcpEnvironment as GcpEnvironment
from ..errors import LaunchError as LaunchError
from ..registry.abstract import AbstractRegistry as AbstractRegistry
from ..utils import MAX_ENV_LENGTHS as MAX_ENV_LENGTHS, PROJECT_SYNCHRONOUS as PROJECT_SYNCHRONOUS
from .abstract import AbstractRun as AbstractRun, AbstractRunner as AbstractRunner, Status as Status
from _typeshed import Incomplete
from typing import Any, Dict
from wandb.apis.internal import Api as Api
from wandb.util import get_module as get_module

GCP_CONSOLE_URI: str

class VertexSubmittedRun(AbstractRun):
    def __init__(self, job: Any) -> None: ...
    @property
    def id(self) -> str: ...
    def get_logs(self) -> str | None: ...
    @property
    def name(self) -> str: ...
    @property
    def gcp_region(self) -> str: ...
    @property
    def gcp_project(self) -> str: ...
    def get_page_link(self) -> str: ...
    def wait(self) -> bool: ...
    def get_status(self) -> Status: ...
    def cancel(self) -> None: ...

class VertexRunner(AbstractRunner):
    """Runner class, uses a project to create a VertexSubmittedRun."""
    environment: Incomplete
    registry: Incomplete
    def __init__(self, api: Api, backend_config: Dict[str, Any], environment: GcpEnvironment, registry: AbstractRegistry) -> None:
        """Initialize a VertexRunner instance."""
    def run(self, launch_project: LaunchProject, image_uri: str) -> AbstractRun | None:
        """Run a Vertex job."""
