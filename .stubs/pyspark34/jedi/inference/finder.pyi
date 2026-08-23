from jedi import settings as settings
from jedi.inference.arguments import TreeArguments as TreeArguments
from jedi.inference.base_value import NO_VALUES as NO_VALUES
from jedi.inference.value import iterable as iterable
from jedi.parser_utils import is_scope as is_scope

def filter_name(filters, name_or_str):
    """
    Searches names that are defined in a scope (the different
    ``filters``), until a name fits.
    """
def check_flow_information(value, flow, search_name, pos):
    """ Try to find out the type of a variable just with the information that
    is given by the flows: e.g. It is also responsible for assert checks.::

        if isinstance(k, str):
            k.  # <- completion here

    ensures that `k` is a string.
    """
