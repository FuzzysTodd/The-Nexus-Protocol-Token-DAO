from .exceptions import JsonSchemaDefinitionException as JsonSchemaDefinitionException, JsonSchemaValueException as JsonSchemaValueException
from .indent import indent as indent
from .ref_resolver import RefResolver as RefResolver
from _typeshed import Incomplete

def enforce_list(variable): ...

class CodeGenerator:
    """
    This class is not supposed to be used directly. Anything
    inside of this class can be changed without noticing.

    This class generates code of validation function from JSON
    schema object as string. Example:

    .. code-block:: python

        CodeGenerator(json_schema_definition).func_code
    """
    INDENT: int
    def __init__(self, definition, resolver: Incomplete | None = None) -> None: ...
    @property
    def func_code(self):
        """
        Returns generated code of whole validation function as string.
        """
    @property
    def global_state(self):
        """
        Returns global variables for generating function from ``func_code``. Includes
        compiled regular expressions and imports, so it does not have to do it every
        time when validation function is called.
        """
    @property
    def global_state_code(self):
        """
        Returns global variables for generating function from ``func_code`` as code.
        Includes compiled regular expressions and imports.
        """
    def generate_func_code(self) -> None:
        """
        Creates base code of validation function and calls helper
        for creating code by definition.
        """
    def generate_validation_function(self, uri, name) -> None:
        """
        Generate validation function for given uri with given name
        """
    def generate_func_code_block(self, definition, variable, variable_name, clear_variables: bool = False):
        """
        Creates validation rules for current definition.

        Returns the number of validation rules generated as code.
        """
    def run_generate_functions(self, definition):
        """Returns the number of generate functions that were executed."""
    def generate_ref(self) -> None:
        """
        Ref can be link to remote or local definition.

        .. code-block:: python

            {'$ref': 'http://json-schema.org/draft-04/schema#'}
            {
                'properties': {
                    'foo': {'type': 'integer'},
                    'bar': {'$ref': '#/properties/foo'}
                }
            }
        """
    def l(self, line, *args, **kwds):
        '''
        Short-cut of line. Used for inserting line. It\'s formated with parameters
        ``variable``, ``variable_name`` (as ``name`` for short-cut), all keys from
        current JSON schema ``definition`` and also passed arguments in ``args``
        and named ``kwds``.

        .. code-block:: python

            self.l(\'if {variable} not in {enum}: raise JsonSchemaValueException("Wrong!")\')

        When you want to indent block, use it as context manager. For example:

        .. code-block:: python

            with self.l(\'if {variable} not in {enum}:\'):
                self.l(\'raise JsonSchemaValueException("Wrong!")\')
        '''
    def e(self, string):
        '''
        Short-cut of escape. Used for inserting user values into a string message.

        .. code-block:: python

            self.l(\'raise JsonSchemaValueException("Variable: {}")\', self.e(variable))
        '''
    def exc(self, msg, *args, append_to_msg: Incomplete | None = None, rule: Incomplete | None = None) -> None:
        """
        Short-cut for creating raising exception in the code.
        """
    def create_variable_with_length(self) -> None:
        """
        Append code for creating variable with length of that variable
        (for example length of list or dictionary) with name ``{variable}_len``.
        It can be called several times and always it's done only when that variable
        still does not exists.
        """
    def create_variable_keys(self) -> None:
        """
        Append code for creating variable with keys of that variable (dictionary)
        with a name ``{variable}_keys``. Similar to `create_variable_with_length`.
        """
    def create_variable_is_list(self) -> None:
        """
        Append code for creating variable with bool if it's instance of list
        with a name ``{variable}_is_list``. Similar to `create_variable_with_length`.
        """
    def create_variable_is_dict(self) -> None:
        """
        Append code for creating variable with bool if it's instance of list
        with a name ``{variable}_is_dict``. Similar to `create_variable_with_length`.
        """

def serialize_regexes(patterns_dict): ...
def repr_regex(regex): ...
