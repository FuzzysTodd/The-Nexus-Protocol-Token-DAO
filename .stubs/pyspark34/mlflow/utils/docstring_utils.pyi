from _typeshed import Incomplete
from mlflow.utils.autologging_utils.versioning import FLAVOR_TO_MODULE_NAME_AND_VERSION_INFO_KEY as FLAVOR_TO_MODULE_NAME_AND_VERSION_INFO_KEY

class ParamDocs(dict):
    """
    Represents a set of parameter documents in the docstring.
    """
    def format(self, **kwargs):
        '''
        Formats placeholders in this instance with `kwargs`.

        :param kwargs: A `dict` in the form of `{"< placeholder name >": "< value >"}`.
        :return: A new `ParamDocs` instance with the formatted param docs.

        Examples
        --------
        >>> pd = ParamDocs(p1="{{ doc1 }}", p2="{{ doc2 }}")
        >>> pd.format(doc1="foo", doc2="bar")
        ParamDocs({\'p1\': \'foo\', \'p2\': \'bar\'})
        '''
    def format_docstring(self, docstring):
        '''
        Formats placeholders in `docstring`.

        :param docstring: Docstring to format.
        :return: Formatted docstring.

        Examples
        --------
        >>> pd = ParamDocs(p1="doc1", p2="doc2")
        >>> docstring = \'\'\'
        ... :param p1: {{ p1 }}
        ... :param p2: {{ p2 }}
        ... \'\'\'.strip()
        >>> print(pd.format_docstring(docstring))
        :param p1:
            doc1
        :param p2:
            doc2
        '''

def format_docstring(param_docs):
    '''
    Returns a decorator that replaces param doc placeholders (e.g. \'{{ param_name }}\') in the
    docstring of the decorated function.

    :param param_docs: A `ParamDocs` instance or `dict`.
    :return: A decorator to apply the formatting.

    Examples
    --------
    >>> param_docs = {"p1": "doc1", "p2": "doc2"}
    >>> @format_docstring(param_docs)
    ... def func(p1, p2):
    ...     \'\'\'
    ...     :param p1: {{ p1 }}
    ...     :param p2: {{ p2 }}
    ...     \'\'\'
    >>> import textwrap
    >>> print(textwrap.dedent(func.__doc__).strip())
    :param p1:
        doc1
    :param p2:
        doc2
    '''

LOG_MODEL_PARAM_DOCS: Incomplete

def get_module_min_and_max_supported_ranges(module_name):
    """
    Extracts the minimum and maximum supported package versions from the provided module name.
    The version information is provided via the yaml-to-python-script generation script in
    dev/update_ml_package_versions.py which writes a python file to the importable namespace of
    mlflow.ml_package_versions

    :param module_name: The string name of the module as it is registered in ml_package_versions.py
    :return: tuple of minimum supported version, maximum supported version as strings.
    """
def docstring_version_compatibility_warning(integration_name):
    """
    Generates a docstring that can be applied as a note stating a version compatibility range for
    a given flavor.

    :param integration_name: The name of the module as stored within ml-package-versions.yml
    :return: The wrapped function with the additional docstring header applied
    """
