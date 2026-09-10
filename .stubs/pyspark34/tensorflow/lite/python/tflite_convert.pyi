import argparse
from _typeshed import Incomplete
from tensorflow.lite.python import lite as lite
from tensorflow.lite.python.convert import register_custom_opdefs as register_custom_opdefs
from tensorflow.lite.toco.logging import gen_html as gen_html
from tensorflow.python import tf2 as tf2
from tensorflow.python.framework import dtypes as dtypes
from tensorflow.python.util import keras_deps as keras_deps

class _ParseBooleanFlag(argparse.Action):
    """Helper class to parse boolean flag that optionally accepts truth value."""
    def __init__(self, option_strings, dest, nargs: Incomplete | None = None, **kwargs) -> None: ...
    def __call__(self, parser, namespace, values, option_string: Incomplete | None = None) -> None: ...

def run_main(_) -> None:
    """Main in tflite_convert.py."""
def main() -> None: ...
