from .exceptions import JsonSchemaDefinitionException as JsonSchemaDefinitionException, JsonSchemaException as JsonSchemaException, JsonSchemaValueException as JsonSchemaValueException
from .version import VERSION as VERSION

__all__ = ['VERSION', 'JsonSchemaException', 'JsonSchemaValueException', 'JsonSchemaDefinitionException', 'validate', 'compile', 'compile_to_code']

def validate(definition, data, handlers={}, formats={}, use_default: bool = True):
    """
    Validation function for lazy programmers or for use cases when you need
    to call validation only once, so you do not have to compile it first.
    Use it only when you do not care about performance (even though it will
    be still faster than alternative implementations).

    .. code-block:: python

        import fastjsonschema

        fastjsonschema.validate({'type': 'string'}, 'hello')
        # same as: compile({'type': 'string'})('hello')

    Preferred is to use :any:`compile` function.
    """
def compile(definition, handlers={}, formats={}, use_default: bool = True):
    """
    Generates validation function for validating JSON schema passed in ``definition``.
    Example:

    .. code-block:: python

        import fastjsonschema

        validate = fastjsonschema.compile({'type': 'string'})
        validate('hello')

    This implementation supports keyword ``default`` (can be turned off
    by passing `use_default=False`):

    .. code-block:: python

        validate = fastjsonschema.compile({
            'type': 'object',
            'properties': {
                'a': {'type': 'number', 'default': 42},
            },
        })

        data = validate({})
        assert data == {'a': 42}

    Supported implementations are draft-04, draft-06 and draft-07. Which version
    should be used is determined by `$draft` in your ``definition``. When not
    specified, the latest implementation is used (draft-07).

    .. code-block:: python

        validate = fastjsonschema.compile({
            '$schema': 'http://json-schema.org/draft-04/schema',
            'type': 'number',
        })

    You can pass mapping from URI to function that should be used to retrieve
    remote schemes used in your ``definition`` in parameter ``handlers``.

    Also, you can pass mapping for custom formats. Key is the name of your
    formatter and value can be regular expression, which will be compiled or
    callback returning `bool` (or you can raise your own exception).

    .. code-block:: python

        validate = fastjsonschema.compile(definition, formats={
            'foo': r'foo|bar',
            'bar': lambda value: value in ('foo', 'bar'),
        })

    Exception :any:`JsonSchemaDefinitionException` is raised when generating the
    code fails (bad definition).

    Exception :any:`JsonSchemaValueException` is raised from generated function when
    validation fails (data do not follow the definition).
    """
def compile_to_code(definition, handlers={}, formats={}, use_default: bool = True):
    '''
    Generates validation code for validating JSON schema passed in ``definition``.
    Example:

    .. code-block:: python

        import fastjsonschema

        code = fastjsonschema.compile_to_code({\'type\': \'string\'})
        with open(\'your_file.py\', \'w\') as f:
            f.write(code)

    You can also use it as a script:

    .. code-block:: bash

        echo "{\'type\': \'string\'}" | python3 -m fastjsonschema > your_file.py
        python3 -m fastjsonschema "{\'type\': \'string\'}" > your_file.py

    Exception :any:`JsonSchemaDefinitionException` is raised when generating the
    code fails (bad definition).
    '''
