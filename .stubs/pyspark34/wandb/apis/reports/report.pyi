from ... import termlog as termlog, termwarn as termwarn
from ...sdk.lib import ipython as ipython
from ..public import RetryingClient as RetryingClient
from ._blocks import P as P, PanelGrid as PanelGrid, UnknownBlock as UnknownBlock, WeaveBlock as WeaveBlock, block_mapping as block_mapping, weave_blocks as weave_blocks
from .mutations import UPSERT_VIEW as UPSERT_VIEW, VIEW_REPORT as VIEW_REPORT
from .runset import Runset as Runset
from .util import Attr as Attr, Base as Base, Block as Block, coalesce as coalesce, generate_name as generate_name, nested_get as nested_get, nested_set as nested_set
from .validators import OneOf as OneOf, TypeValidator as TypeValidator
from _typeshed import Incomplete
from typing import List as LList

class Report(Base):
    project: str
    entity: str
    title: str
    description: str
    width: str
    blocks: list
    def __init__(self, project, entity: Incomplete | None = None, title: str = 'Untitled Report', description: str = '', width: str = 'readable', blocks: Incomplete | None = None, _api: Incomplete | None = None, *args, **kwargs) -> None: ...
    @classmethod
    def from_url(cls, url, api: Incomplete | None = None): ...
    @classmethod
    def from_json(cls, viewspec): ...
    @property
    def viewspec(self): ...
    @property
    def modified(self) -> bool: ...
    @property
    def spec(self) -> dict: ...
    @property
    def client(self) -> RetryingClient: ...
    @property
    def id(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def panel_grids(self) -> LList[PanelGrid]: ...
    @property
    def runsets(self) -> LList[Runset]: ...
    @property
    def url(self) -> str: ...
    def save(self, draft: bool = False, clone: bool = False) -> Report: ...
    def to_html(self, height: int = 1024, hidden: bool = False) -> str:
        """Generate HTML containing an iframe displaying this report."""
