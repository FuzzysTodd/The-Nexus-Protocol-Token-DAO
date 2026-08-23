import doctest
from _typeshed import Incomplete

class _FloatExtractor:
    '''Class for extracting floats from a string.

  For example:

  >>> text_parts, floats = _FloatExtractor()("Text 1.0 Text")
  >>> text_parts
  ["Text ", " Text"]
  >>> floats
  np.array([1.0])
  '''
    def __call__(self, string):
        '''Extracts floats from a string.

    >>> text_parts, floats = _FloatExtractor()("Text 1.0 Text")
    >>> text_parts
    ["Text ", " Text"]
    >>> floats
    np.array([1.0])

    Args:
      string: the string to extract floats from.

    Returns:
      A (string, array) pair, where `string` has each float replaced by "..."
      and `array` is a `float32` `numpy.array` containing the extracted floats.
    '''

class TfDoctestOutputChecker(doctest.OutputChecker):
    """Customizes how `want` and `got` are compared, see `check_output`."""
    extract_floats: Incomplete
    text_good: Incomplete
    float_size_good: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    MESSAGE: Incomplete
    def check_output(self, want, got, optionflags):
        """Compares the docstring output to the output gotten by running the code.

    Python addresses in the output are replaced with wildcards.

    Float values in the output compared as using `np.allclose`:

      * Float values are extracted from the text and replaced with wildcards.
      * The wildcard text is compared to the actual output.
      * The float values are compared using `np.allclose`.

    The method returns `True` if both the text comparison and the numeric
    comparison are successful.

    The numeric comparison will fail if either:

      * The wrong number of floats are found.
      * The float values are not within tolerence.

    Args:
      want: The output in the docstring.
      got: The output generated after running the snippet.
      optionflags: Flags passed to the doctest.

    Returns:
      A bool, indicating if the check was successful or not.
    """
    def output_difference(self, example, got, optionflags): ...
