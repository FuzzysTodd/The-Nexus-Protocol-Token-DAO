from click.testing import CliRunner as ClickCliRunner, Result as Result
from typer.main import Typer as Typer
from typing import Any, IO, Mapping, Sequence

class CliRunner(ClickCliRunner):
    def invoke(self, app: Typer, args: str | Sequence[str] | None = None, input: bytes | str | IO[Any] | None = None, env: Mapping[str, str] | None = None, catch_exceptions: bool = True, color: bool = False, **extra: Any) -> Result: ...
