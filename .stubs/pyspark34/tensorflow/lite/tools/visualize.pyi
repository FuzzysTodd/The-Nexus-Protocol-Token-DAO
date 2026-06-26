from _typeshed import Incomplete

def TensorTypeToName(tensor_type):
    """Converts a numerical enum to a readable tensor type."""
def BuiltinCodeToName(code):
    """Converts a builtin op code enum to a readable name."""
def NameListToString(name_list):
    """Converts a list of integers to the equivalent ASCII string."""

class OpCodeMapper:
    """Maps an opcode index to an op name."""
    code_to_name: Incomplete
    def __init__(self, data) -> None: ...
    def __call__(self, x): ...

class DataSizeMapper:
    """For buffers, report the number of bytes."""
    def __call__(self, x): ...

class TensorMapper:
    """Maps a list of tensor indices to a tooltip hoverable indicator of more."""
    data: Incomplete
    def __init__(self, subgraph_data) -> None: ...
    def __call__(self, x): ...

def GenerateGraph(subgraph_idx, g, opcode_mapper):
    """Produces the HTML required to have a d3 visualization of the dag."""
def GenerateTableHtml(items, keys_to_print, display_index: bool = True):
    """Given a list of object values and keys to print, make an HTML table.

  Args:
    items: Items to print an array of dicts.
    keys_to_print: (key, display_fn). `key` is a key in the object. i.e.
      items[0][key] should exist. display_fn is the mapping function on display.
      i.e. the displayed html cell will have the string returned by
      `mapping_fn(items[0][key])`.
    display_index: add a column which is the index of each row in `items`.

  Returns:
    An html table.
  """
def CamelCaseToSnakeCase(camel_case_input):
    """Converts an identifier in CamelCase to snake_case."""
def FlatbufferToDict(fb, preserve_as_numpy):
    """Converts a hierarchy of FB objects into a nested dict.

  We avoid transforming big parts of the flat buffer into python arrays. This
  speeds conversion from ten minutes to a few seconds on big graphs.

  Args:
    fb: a flat buffer structure. (i.e. ModelT)
    preserve_as_numpy: true if all downstream np.arrays should be preserved.
      false if all downstream np.array should become python arrays
  Returns:
    A dictionary representing the flatbuffer rather than a flatbuffer object.
  """
def CreateDictFromFlatbuffer(buffer_data): ...
def create_html(tflite_input, input_is_filepath: bool = True):
    """Returns html description with the given tflite model.

  Args:
    tflite_input: TFLite flatbuffer model path or model object.
    input_is_filepath: Tells if tflite_input is a model path or a model object.

  Returns:
    Dump of the given tflite model in HTML format.

  Raises:
    RuntimeError: If the input is not valid.
  """
def main(argv) -> None: ...
