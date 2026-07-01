from _typeshed import Incomplete
from typing import NamedTuple

class CodeLine(NamedTuple):
    cell_number: Incomplete
    code: Incomplete

def is_python(cell):
    """Checks if the cell consists of Python code."""
def process_file(in_filename, out_filename, upgrader):
    """The function where we inject the support for ipynb upgrade."""
def skip_magic(code_line, magic_list):
    '''Checks if the cell has magic, that is not Python-based.

  Args:
      code_line: A line of Python code
      magic_list: A list of jupyter "magic" exceptions

  Returns:
    If the line jupyter "magic" line, not Python line

   >>> skip_magic(\'!ls -laF\', [\'%\', \'!\', \'?\'])
  True
  '''
def check_line_split(code_line):
    '''Checks if a line was split with `\\`.

  Args:
      code_line: A line of Python code

  Returns:
    If the line was split with `\\`

  >>> skip_magic("!gcloud ml-engine models create ${MODEL} \\\\\\n")
  True
  '''
