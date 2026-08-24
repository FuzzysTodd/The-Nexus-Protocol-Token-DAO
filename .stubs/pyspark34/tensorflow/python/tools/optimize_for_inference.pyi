from _typeshed import Incomplete
from tensorflow.core.framework import graph_pb2 as graph_pb2
from tensorflow.python.framework import dtypes as dtypes, graph_io as graph_io
from tensorflow.python.platform import gfile as gfile
from tensorflow.python.tools import optimize_for_inference_lib as optimize_for_inference_lib

FLAGS: Incomplete

def main(unused_args): ...
def parse_args():
    """Parses command line arguments."""
