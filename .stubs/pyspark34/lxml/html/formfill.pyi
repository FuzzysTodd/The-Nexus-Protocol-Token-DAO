from _typeshed import Incomplete

__all__ = ['FormNotFound', 'fill_form', 'fill_form_html', 'insert_errors', 'insert_errors_html', 'DefaultErrorCreator']

basestring = str

class FormNotFound(LookupError):
    """
    Raised when no form can be found
    """

def fill_form(el, values, form_id: Incomplete | None = None, form_index: Incomplete | None = None) -> None: ...
def fill_form_html(html, values, form_id: Incomplete | None = None, form_index: Incomplete | None = None): ...

class DefaultErrorCreator:
    insert_before: bool
    block_inside: bool
    error_container_tag: str
    error_message_class: str
    error_block_class: str
    default_message: str
    def __init__(self, **kw) -> None: ...
    def __call__(self, el, is_block, message) -> None: ...

def insert_errors(el, errors, form_id: Incomplete | None = None, form_index: Incomplete | None = None, error_class: str = 'error', error_creator=...) -> None: ...
def insert_errors_html(html, values, **kw): ...
