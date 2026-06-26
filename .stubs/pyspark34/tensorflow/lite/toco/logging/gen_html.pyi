from _typeshed import Incomplete

html_escape_table: Incomplete

def html_escape(text): ...
def get_input_type_from_signature(op_signature):
    """Parses op_signature and returns a string denoting the input tensor type.

  Args:
    op_signature: a string specifying the signature of a particular operator.
      The signature of an operator contains the input tensor's shape and type,
      output tensor's shape and type, operator's name and its version. It has
      the following schema:
      INPUT:input_1_shape::input_1_type::input_2_shape::input_2_type::..
        ::OUTPUT:output_1_shape::output_1_type::output_2_shape::output_2_type::
        ..::NAME:operator_name ::VERSION:operator_version
     An example of an operator signature is:
     INPUT:[1,73,73,160]::float::[64,1,1,160]::float::[64]::float::
     OUTPUT:[1,73,73,64]::float::NAME:Conv::VERSION:1

  Returns:
    A string denoting the input tensors' type. In the form of shape/type
    separated
    by comma. For example:
    shape:[1,73,73,160],type:float,shape:[64,1,1,160],type:float,shape:[64],
    type:float
  """
def get_operator_type(op_name, conversion_log): ...

class HTMLGenerator:
    """Utility class to generate an HTML report."""
    html_template: Incomplete
    export_report_path: Incomplete
    def __init__(self, html_template_path, export_report_path) -> None:
        """Reads the HTML template content.

    Args:
      html_template_path: A string, path to the template HTML file.
      export_report_path: A string, path to the generated HTML report. This path
        should point to a '.html' file with date and time in its name.
        e.g. 2019-01-01-10:05.toco_report.html.

    Raises:
      IOError: File doesn't exist.
    """
    def generate(self, toco_conversion_log_before, toco_conversion_log_after, post_training_quant_enabled, dot_before, dot_after, toco_err_log: str = '', tflite_graph_path: str = '') -> None:
        """Generates the HTML report and writes it to local directory.

    This function uses the fields in `toco_conversion_log_before` and
    `toco_conversion_log_after` to populate the HTML content. Certain markers
    (placeholders) in the HTML template are then substituted with the fields
    from the protos. Once finished it will write the HTML file to the specified
    local file path.

    Args:
      toco_conversion_log_before: A `TocoConversionLog` protobuf generated
        before the model is converted by TOCO.
      toco_conversion_log_after: A `TocoConversionLog` protobuf generated after
        the model is converted by TOCO.
      post_training_quant_enabled: A boolean, whether post-training quantization
        is enabled.
      dot_before: A string, the dot representation of the model
        before the conversion.
      dot_after: A string, the dot representation of the model after
        the conversion.
      toco_err_log: A string, the logs emitted by TOCO during conversion. Caller
        need to ensure that this string is properly anonymized (any kind of
        user data should be eliminated).
      tflite_graph_path: A string, the filepath to the converted TFLite model.

    Raises:
      RuntimeError: When error occurs while generating the template.
    """

def gen_conversion_log_html(conversion_log_dir, quantization_enabled, tflite_graph_path) -> None:
    """Generates an HTML report about the conversion process.

  Args:
    conversion_log_dir: A string specifying the file directory of the conversion
      logs. It's required that before calling this function, the
      `conversion_log_dir`
      already contains the following files: `toco_log_before.pb`,
        `toco_log_after.pb`, `toco_tf_graph.dot`,
        `toco_tflite_graph.dot`.
    quantization_enabled: A boolean, passed from the tflite converter to
      indicate whether post-training quantization is enabled during conversion.
    tflite_graph_path: A string, the filepath to the converted TFLite model.

  Raises:
    IOError: When any of the required files doesn't exist.
  """
