from ..utils.io import ask_yes_no as ask_yes_no
from .application import BaseIPythonApplication as BaseIPythonApplication
from _typeshed import Incomplete
from traitlets.config.application import Application

trim_hist_help: str
clear_hist_help: str

class HistoryTrim(BaseIPythonApplication):
    description = trim_hist_help
    backup: Incomplete
    keep: Incomplete
    flags: Incomplete
    aliases: Incomplete
    def start(self) -> None: ...

class HistoryClear(HistoryTrim):
    description = clear_hist_help
    keep: Incomplete
    force: Incomplete
    flags: Incomplete
    aliases: Incomplete
    def start(self) -> None: ...

class HistoryApp(Application):
    name: str
    description: str
    subcommands: Incomplete
    def start(self): ...
