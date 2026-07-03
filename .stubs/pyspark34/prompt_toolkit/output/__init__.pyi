from .base import DummyOutput as DummyOutput, Output as Output
from .color_depth import ColorDepth as ColorDepth
from .defaults import create_output as create_output

__all__ = ['Output', 'DummyOutput', 'ColorDepth', 'create_output']
