from _typeshed import Incomplete
from openai import api_requestor as api_requestor, error as error, util as util
from openai.api_resources.abstract import DeletableAPIResource as DeletableAPIResource, ListableAPIResource as ListableAPIResource
from openai.util import ApiType as ApiType

class File(ListableAPIResource, DeletableAPIResource):
    OBJECT_NAME: str
    @classmethod
    def create(cls, file, purpose, model: Incomplete | None = None, api_key: Incomplete | None = None, api_base: Incomplete | None = None, api_type: Incomplete | None = None, api_version: Incomplete | None = None, organization: Incomplete | None = None, user_provided_filename: Incomplete | None = None): ...
    @classmethod
    async def acreate(cls, file, purpose, model: Incomplete | None = None, api_key: Incomplete | None = None, api_base: Incomplete | None = None, api_type: Incomplete | None = None, api_version: Incomplete | None = None, organization: Incomplete | None = None, user_provided_filename: Incomplete | None = None): ...
    @classmethod
    def download(cls, id, api_key: Incomplete | None = None, api_base: Incomplete | None = None, api_type: Incomplete | None = None, api_version: Incomplete | None = None, organization: Incomplete | None = None): ...
    @classmethod
    async def adownload(cls, id, api_key: Incomplete | None = None, api_base: Incomplete | None = None, api_type: Incomplete | None = None, api_version: Incomplete | None = None, organization: Incomplete | None = None): ...
    @classmethod
    def find_matching_files(cls, name, bytes, purpose, api_key: Incomplete | None = None, api_base: Incomplete | None = None, api_type: Incomplete | None = None, api_version: Incomplete | None = None, organization: Incomplete | None = None):
        """Find already uploaded files with the same name, size, and purpose."""
    @classmethod
    async def afind_matching_files(cls, name, bytes, purpose, api_key: Incomplete | None = None, api_base: Incomplete | None = None, api_type: Incomplete | None = None, api_version: Incomplete | None = None, organization: Incomplete | None = None):
        """Find already uploaded files with the same name, size, and purpose."""
