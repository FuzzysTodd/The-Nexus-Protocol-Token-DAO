from .debugger import Pdb as Pdb, TerminalPdb as TerminalPdb
from .magics import TerminalMagics as TerminalMagics
from .prompts import ClassicPrompts as ClassicPrompts, Prompts as Prompts, RichPromptDisplayHook as RichPromptDisplayHook
from .pt_inputhooks import get_inputhook_name_and_func as get_inputhook_name_and_func
from .ptutils import IPythonPTCompleter as IPythonPTCompleter, IPythonPTLexer as IPythonPTLexer
from .shortcuts import KEY_BINDINGS as KEY_BINDINGS, RuntimeBinding as RuntimeBinding, add_binding as add_binding, create_identifier as create_identifier, create_ipython_shortcuts as create_ipython_shortcuts
from .shortcuts.auto_suggest import AppendAutoSuggestionInAnyLine as AppendAutoSuggestionInAnyLine, NavigableAutoSuggestFromHistory as NavigableAutoSuggestFromHistory
from .shortcuts.filters import KEYBINDING_FILTERS as KEYBINDING_FILTERS, filter_from_string as filter_from_string
from IPython.core.async_helpers import get_asyncio_loop as get_asyncio_loop
from IPython.core.interactiveshell import InteractiveShell as InteractiveShell, InteractiveShellABC as InteractiveShellABC
from IPython.utils.process import abbrev_cwd as abbrev_cwd
from IPython.utils.py3compat import input as input
from IPython.utils.terminal import restore_term_title as restore_term_title, set_term_title as set_term_title, toggle_set_term_title as toggle_set_term_title
from _typeshed import Incomplete
from collections.abc import Generator
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.history import History
from prompt_toolkit.shortcuts import PromptSession
from pygments.style import Style

PTK3: Incomplete

class _NoStyle(Style): ...

def get_default_editor(): ...
def black_reformat_handler(text_before_cursor):
    """
    We do not need to protect against error,
    this is taken care at a higher level where any reformat error is ignored.
    Indeed we may call reformatting on incomplete code.
    """
def yapf_reformat_handler(text_before_cursor): ...

class PtkHistoryAdapter(History):
    """
    Prompt toolkit has it's own way of handling history, Where it assumes it can
    Push/pull from history.

    """
    shell: Incomplete
    def __init__(self, shell) -> None: ...
    def append_string(self, string) -> None: ...
    def load_history_strings(self) -> Generator[Incomplete, Incomplete, None]: ...
    def store_string(self, string: str) -> None: ...

class TerminalInteractiveShell(InteractiveShell):
    mime_renderers: Incomplete
    space_for_menu: Incomplete
    pt_app: PromptSession | None
    auto_suggest: AutoSuggestFromHistory | NavigableAutoSuggestFromHistory | None
    debugger_history: Incomplete
    debugger_history_file: Incomplete
    simple_prompt: Incomplete
    @property
    def debugger_cls(self): ...
    confirm_exit: Incomplete
    editing_mode: Incomplete
    emacs_bindings_in_vi_insert_mode: Incomplete
    modal_cursor: Incomplete
    ttimeoutlen: Incomplete
    timeoutlen: Incomplete
    autoformatter: Incomplete
    auto_match: Incomplete
    mouse_support: Incomplete
    highlighting_style: Incomplete
    def refresh_style(self) -> None: ...
    highlighting_style_overrides: Incomplete
    true_color: Incomplete
    editor: Incomplete
    prompts_class: Incomplete
    prompts: Incomplete
    term_title: Incomplete
    term_title_format: Incomplete
    display_completions: Incomplete
    highlight_matching_brackets: Incomplete
    extra_open_editor_shortcuts: Incomplete
    handle_return: Incomplete
    enable_history_search: Incomplete
    autosuggestions_provider: Incomplete
    shortcuts: Incomplete
    prompt_includes_vi_mode: Incomplete
    def init_term_title(self, change: Incomplete | None = None) -> None: ...
    def restore_term_title(self) -> None: ...
    def init_display_formatter(self) -> None: ...
    style: Incomplete
    pt_loop: Incomplete
    def init_prompt_toolkit_cli(self): ...
    @property
    def pt_complete_style(self): ...
    @property
    def color_depth(self): ...
    rl_next_input: Incomplete
    def prompt_for_code(self): ...
    def enable_win_unicode_console(self) -> None: ...
    def init_io(self) -> None: ...
    def init_magics(self) -> None: ...
    def init_alias(self) -> None: ...
    keep_running: bool
    def __init__(self, *args, **kwargs) -> None: ...
    def ask_exit(self) -> None: ...
    def interact(self) -> None: ...
    def mainloop(self) -> None: ...
    def inputhook(self, context) -> None: ...
    active_eventloop: Incomplete
    def enable_gui(self, gui: Incomplete | None = None) -> None: ...
    system: Incomplete
    def auto_rewrite_input(self, cmd) -> None:
        """Overridden from the parent class to use fancy rewriting prompt"""
    def switch_doctest_mode(self, mode) -> None:
        """Switch prompts to classic for %doctest_mode"""
