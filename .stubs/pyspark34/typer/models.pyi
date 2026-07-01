import click
import click.shell_completion
import io
from .core import TyperCommand as TyperCommand, TyperGroup as TyperGroup
from .main import Typer as Typer
from _typeshed import Incomplete
from typing import Any, Callable, Dict, List, Sequence, Type, TypeVar

NoneType: Incomplete
AnyType = Type[Any]
Required: Incomplete

class Context(click.Context): ...
class FileText(io.TextIOWrapper): ...
class FileTextWrite(FileText): ...
class FileBinaryRead(io.BufferedReader): ...
class FileBinaryWrite(io.BufferedWriter): ...
class CallbackParam(click.Parameter): ...

class DefaultPlaceholder:
    """
    You shouldn't use this class directly.

    It's used internally to recognize when a default value has been overwritten, even
    if the new value is `None`.
    """
    value: Incomplete
    def __init__(self, value: Any) -> None: ...
    def __bool__(self) -> bool: ...
DefaultType = TypeVar('DefaultType')
CommandFunctionType = TypeVar('CommandFunctionType', bound=Callable[..., Any])

def Default(value: DefaultType) -> DefaultType:
    """
    You shouldn't use this function directly.

    It's used internally to recognize when a default value has been overwritten, even
    if the new value is `None`.
    """

class CommandInfo:
    name: Incomplete
    cls: Incomplete
    context_settings: Incomplete
    callback: Incomplete
    help: Incomplete
    epilog: Incomplete
    short_help: Incomplete
    options_metavar: Incomplete
    add_help_option: Incomplete
    no_args_is_help: Incomplete
    hidden: Incomplete
    deprecated: Incomplete
    rich_help_panel: Incomplete
    def __init__(self, name: str | None = None, *, cls: Type['TyperCommand'] | None = None, context_settings: Dict[Any, Any] | None = None, callback: Callable[..., Any] | None = None, help: str | None = None, epilog: str | None = None, short_help: str | None = None, options_metavar: str = '[OPTIONS]', add_help_option: bool = True, no_args_is_help: bool = False, hidden: bool = False, deprecated: bool = False, rich_help_panel: str | None = None) -> None: ...

class TyperInfo:
    typer_instance: Incomplete
    name: Incomplete
    cls: Incomplete
    invoke_without_command: Incomplete
    no_args_is_help: Incomplete
    subcommand_metavar: Incomplete
    chain: Incomplete
    result_callback: Incomplete
    context_settings: Incomplete
    callback: Incomplete
    help: Incomplete
    epilog: Incomplete
    short_help: Incomplete
    options_metavar: Incomplete
    add_help_option: Incomplete
    hidden: Incomplete
    deprecated: Incomplete
    rich_help_panel: Incomplete
    def __init__(self, typer_instance: Typer | None = ..., *, name: str | None = ..., cls: Type['TyperGroup'] | None = ..., invoke_without_command: bool = ..., no_args_is_help: bool = ..., subcommand_metavar: str | None = ..., chain: bool = ..., result_callback: Callable[..., Any] | None = ..., context_settings: Dict[Any, Any] | None = ..., callback: Callable[..., Any] | None = ..., help: str | None = ..., epilog: str | None = ..., short_help: str | None = ..., options_metavar: str = ..., add_help_option: bool = ..., hidden: bool = ..., deprecated: bool = ..., rich_help_panel: str | None = ...) -> None: ...

class ParameterInfo:
    default: Incomplete
    param_decls: Incomplete
    callback: Incomplete
    metavar: Incomplete
    expose_value: Incomplete
    is_eager: Incomplete
    envvar: Incomplete
    shell_complete: Incomplete
    autocompletion: Incomplete
    default_factory: Incomplete
    parser: Incomplete
    click_type: Incomplete
    show_default: Incomplete
    show_choices: Incomplete
    show_envvar: Incomplete
    help: Incomplete
    hidden: Incomplete
    case_sensitive: Incomplete
    min: Incomplete
    max: Incomplete
    clamp: Incomplete
    formats: Incomplete
    mode: Incomplete
    encoding: Incomplete
    errors: Incomplete
    lazy: Incomplete
    atomic: Incomplete
    exists: Incomplete
    file_okay: Incomplete
    dir_okay: Incomplete
    writable: Incomplete
    readable: Incomplete
    resolve_path: Incomplete
    allow_dash: Incomplete
    path_type: Incomplete
    rich_help_panel: Incomplete
    def __init__(self, *, default: Any | None = None, param_decls: Sequence[str] | None = None, callback: Callable[..., Any] | None = None, metavar: str | None = None, expose_value: bool = True, is_eager: bool = False, envvar: str | List[str] | None = None, shell_complete: Callable[[click.Context, click.Parameter, str], List['click.shell_completion.CompletionItem'] | List[str]] | None = None, autocompletion: Callable[..., Any] | None = None, default_factory: Callable[[], Any] | None = None, parser: Callable[[str], Any] | None = None, click_type: click.ParamType | None = None, show_default: bool | str = True, show_choices: bool = True, show_envvar: bool = True, help: str | None = None, hidden: bool = False, case_sensitive: bool = True, min: int | float | None = None, max: int | float | None = None, clamp: bool = False, formats: List[str] | None = None, mode: str | None = None, encoding: str | None = None, errors: str | None = 'strict', lazy: bool | None = None, atomic: bool = False, exists: bool = False, file_okay: bool = True, dir_okay: bool = True, writable: bool = False, readable: bool = True, resolve_path: bool = False, allow_dash: bool = False, path_type: None | Type[str] | Type[bytes] = None, rich_help_panel: str | None = None) -> None: ...

class OptionInfo(ParameterInfo):
    prompt: Incomplete
    confirmation_prompt: Incomplete
    prompt_required: Incomplete
    hide_input: Incomplete
    is_flag: Incomplete
    flag_value: Incomplete
    count: Incomplete
    allow_from_autoenv: Incomplete
    def __init__(self, *, default: Any | None = None, param_decls: Sequence[str] | None = None, callback: Callable[..., Any] | None = None, metavar: str | None = None, expose_value: bool = True, is_eager: bool = False, envvar: str | List[str] | None = None, shell_complete: Callable[[click.Context, click.Parameter, str], List['click.shell_completion.CompletionItem'] | List[str]] | None = None, autocompletion: Callable[..., Any] | None = None, default_factory: Callable[[], Any] | None = None, parser: Callable[[str], Any] | None = None, click_type: click.ParamType | None = None, show_default: bool = True, prompt: bool | str = False, confirmation_prompt: bool = False, prompt_required: bool = True, hide_input: bool = False, is_flag: bool | None = None, flag_value: Any | None = None, count: bool = False, allow_from_autoenv: bool = True, help: str | None = None, hidden: bool = False, show_choices: bool = True, show_envvar: bool = True, case_sensitive: bool = True, min: int | float | None = None, max: int | float | None = None, clamp: bool = False, formats: List[str] | None = None, mode: str | None = None, encoding: str | None = None, errors: str | None = 'strict', lazy: bool | None = None, atomic: bool = False, exists: bool = False, file_okay: bool = True, dir_okay: bool = True, writable: bool = False, readable: bool = True, resolve_path: bool = False, allow_dash: bool = False, path_type: None | Type[str] | Type[bytes] = None, rich_help_panel: str | None = None) -> None: ...

class ArgumentInfo(ParameterInfo):
    def __init__(self, *, default: Any | None = None, param_decls: Sequence[str] | None = None, callback: Callable[..., Any] | None = None, metavar: str | None = None, expose_value: bool = True, is_eager: bool = False, envvar: str | List[str] | None = None, shell_complete: Callable[[click.Context, click.Parameter, str], List['click.shell_completion.CompletionItem'] | List[str]] | None = None, autocompletion: Callable[..., Any] | None = None, default_factory: Callable[[], Any] | None = None, parser: Callable[[str], Any] | None = None, click_type: click.ParamType | None = None, show_default: bool | str = True, show_choices: bool = True, show_envvar: bool = True, help: str | None = None, hidden: bool = False, case_sensitive: bool = True, min: int | float | None = None, max: int | float | None = None, clamp: bool = False, formats: List[str] | None = None, mode: str | None = None, encoding: str | None = None, errors: str | None = 'strict', lazy: bool | None = None, atomic: bool = False, exists: bool = False, file_okay: bool = True, dir_okay: bool = True, writable: bool = False, readable: bool = True, resolve_path: bool = False, allow_dash: bool = False, path_type: None | Type[str] | Type[bytes] = None, rich_help_panel: str | None = None) -> None: ...

class ParamMeta:
    empty: Incomplete
    name: Incomplete
    default: Incomplete
    annotation: Incomplete
    def __init__(self, *, name: str, default: Any = ..., annotation: Any = ...) -> None: ...

class DeveloperExceptionConfig:
    pretty_exceptions_enable: Incomplete
    pretty_exceptions_show_locals: Incomplete
    pretty_exceptions_short: Incomplete
    def __init__(self, *, pretty_exceptions_enable: bool = True, pretty_exceptions_show_locals: bool = True, pretty_exceptions_short: bool = True) -> None: ...
