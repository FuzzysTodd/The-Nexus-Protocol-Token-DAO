from enum import Enum
from pathlib import Path
from typing import Tuple

class Shells(str, Enum):
    bash: str
    zsh: str
    fish: str
    powershell: str
    pwsh: str

COMPLETION_SCRIPT_BASH: str
COMPLETION_SCRIPT_ZSH: str
COMPLETION_SCRIPT_FISH: str
COMPLETION_SCRIPT_POWER_SHELL: str

def get_completion_script(*, prog_name: str, complete_var: str, shell: str) -> str: ...
def install_bash(*, prog_name: str, complete_var: str, shell: str) -> Path: ...
def install_zsh(*, prog_name: str, complete_var: str, shell: str) -> Path: ...
def install_fish(*, prog_name: str, complete_var: str, shell: str) -> Path: ...
def install_powershell(*, prog_name: str, complete_var: str, shell: str) -> Path: ...
def install(shell: str | None = None, prog_name: str | None = None, complete_var: str | None = None) -> Tuple[str, Path]: ...
