from typing import Type
from uvicorn.supervisors.basereload import BaseReload
from uvicorn.supervisors.multiprocess import Multiprocess as Multiprocess

__all__ = ['Multiprocess', 'ChangeReload']

ChangeReload: Type[BaseReload]
