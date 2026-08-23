from ..plugins.opencv import OpenCVPlugin as OpenCVPlugin
from ..plugins.pillow import PillowPlugin as PillowPlugin
from ..plugins.pyav import PyAVPlugin as PyAVPlugin
from ..plugins.tifffile_v3 import TifffilePlugin as TifffilePlugin
from ..typing import ImageResource as ImageResource
from .legacy_plugin_wrapper import LegacyPlugin as LegacyPlugin
from .v3_plugin_api import PluginV3 as PluginV3
from typing import Literal, Type, TypeVar, overload

CustomPlugin = TypeVar('CustomPlugin', bound=PluginV3)

@overload
def imopen(uri: ImageResource, io_mode: Literal['r', 'w'], *, extension: str = None, format_hint: str = None) -> PluginV3: ...
@overload
def imopen(uri: ImageResource, io_mode: Literal['r', 'w'], *, plugin: str = None, format_hint: str = None, extension: str = None, legacy_mode: Literal[True], **kwargs) -> LegacyPlugin: ...
@overload
def imopen(uri: ImageResource, io_mode: Literal['r', 'w'], *, format_hint: str = None, extension: str = None, legacy_mode: Literal[False] = False) -> PluginV3: ...
@overload
def imopen(uri: ImageResource, io_mode: Literal['r', 'w'], *, plugin: Literal['pillow'], extension: str = None, format_hint: str = None) -> PillowPlugin: ...
@overload
def imopen(uri: ImageResource, io_mode: Literal['r', 'w'], *, plugin: Literal['pyav'], extension: str = None, format_hint: str = None, container: str = None) -> PyAVPlugin: ...
@overload
def imopen(uri, io_mode: Literal['r', 'w'], *, plugin: Literal['opencv'], extension: str = None, format_hint: str = None) -> OpenCVPlugin: ...
@overload
def imopen(uri, io_mode: Literal['r', 'w'], *, plugin: Literal['tifffile'], extension: str = None, format_hint: str = None) -> TifffilePlugin: ...
@overload
def imopen(uri: ImageResource, io_mode: Literal['r', 'w'], *, plugin: Type[CustomPlugin], extension: str = None, format_hint: str = None, **kwargs) -> CustomPlugin: ...
