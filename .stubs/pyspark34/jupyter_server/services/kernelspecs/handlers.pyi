from ...base.handlers import APIHandler as APIHandler
from ...utils import url_path_join as url_path_join, url_unescape as url_unescape
from _typeshed import Incomplete
from jupyter_server.auth import authorized as authorized

pjoin: Incomplete
AUTH_RESOURCE: str

def kernelspec_model(handler, name, spec_dict, resource_dir):
    """Load a KernelSpec by name and return the REST API model"""
def is_kernelspec_model(spec_dict):
    """Returns True if spec_dict is already in proper form.  This will occur when using a gateway."""

class KernelSpecsAPIHandler(APIHandler):
    """A kernel spec API handler."""
    auth_resource = AUTH_RESOURCE

class MainKernelSpecHandler(KernelSpecsAPIHandler):
    """The root kernel spec handler."""
    async def get(self) -> None:
        """Get the list of kernel specs."""

class KernelSpecHandler(KernelSpecsAPIHandler):
    """A handler for an individual kernel spec."""
    async def get(self, kernel_name) -> None:
        """Get a kernel spec model."""

kernel_name_regex: str
default_handlers: Incomplete
