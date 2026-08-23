from prompt_toolkit.application import Application
from prompt_toolkit.completion import Completer
from prompt_toolkit.filters import FilterOrBool
from prompt_toolkit.formatted_text import AnyFormattedText
from prompt_toolkit.styles import BaseStyle
from prompt_toolkit.validation import Validator
from typing import Callable, Sequence

__all__ = ['yes_no_dialog', 'button_dialog', 'input_dialog', 'message_dialog', 'radiolist_dialog', 'checkboxlist_dialog', 'progress_dialog']

def yes_no_dialog(title: AnyFormattedText = '', text: AnyFormattedText = '', yes_text: str = 'Yes', no_text: str = 'No', style: BaseStyle | None = None) -> Application[bool]:
    """
    Display a Yes/No dialog.
    Return a boolean.
    """
def button_dialog(title: AnyFormattedText = '', text: AnyFormattedText = '', buttons: list[tuple[str, _T]] = [], style: BaseStyle | None = None) -> Application[_T]:
    """
    Display a dialog with button choices (given as a list of tuples).
    Return the value associated with button.
    """
def input_dialog(title: AnyFormattedText = '', text: AnyFormattedText = '', ok_text: str = 'OK', cancel_text: str = 'Cancel', completer: Completer | None = None, validator: Validator | None = None, password: FilterOrBool = False, style: BaseStyle | None = None, default: str = '') -> Application[str]:
    """
    Display a text input box.
    Return the given text, or None when cancelled.
    """
def message_dialog(title: AnyFormattedText = '', text: AnyFormattedText = '', ok_text: str = 'Ok', style: BaseStyle | None = None) -> Application[None]:
    """
    Display a simple message box and wait until the user presses enter.
    """
def radiolist_dialog(title: AnyFormattedText = '', text: AnyFormattedText = '', ok_text: str = 'Ok', cancel_text: str = 'Cancel', values: Sequence[tuple[_T, AnyFormattedText]] | None = None, default: _T | None = None, style: BaseStyle | None = None) -> Application[_T]:
    """
    Display a simple list of element the user can choose amongst.

    Only one element can be selected at a time using Arrow keys and Enter.
    The focus can be moved between the list and the Ok/Cancel button with tab.
    """
def checkboxlist_dialog(title: AnyFormattedText = '', text: AnyFormattedText = '', ok_text: str = 'Ok', cancel_text: str = 'Cancel', values: Sequence[tuple[_T, AnyFormattedText]] | None = None, default_values: Sequence[_T] | None = None, style: BaseStyle | None = None) -> Application[list[_T]]:
    """
    Display a simple list of element the user can choose multiple values amongst.

    Several elements can be selected at a time using Arrow keys and Enter.
    The focus can be moved between the list and the Ok/Cancel button with tab.
    """
def progress_dialog(title: AnyFormattedText = '', text: AnyFormattedText = '', run_callback: Callable[[Callable[[int], None], Callable[[str], None]], None] = ..., style: BaseStyle | None = None) -> Application[None]:
    """
    :param run_callback: A function that receives as input a `set_percentage`
        function and it does the work.
    """
