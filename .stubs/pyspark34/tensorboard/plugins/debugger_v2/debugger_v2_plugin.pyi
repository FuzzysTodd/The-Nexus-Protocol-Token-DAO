from _typeshed import Incomplete
from tensorboard import errors as errors, plugin_util as plugin_util
from tensorboard.backend import http_util as http_util
from tensorboard.plugins import base_plugin as base_plugin
from tensorboard.plugins.debugger_v2 import debug_data_provider as debug_data_provider

class DebuggerV2Plugin(base_plugin.TBPlugin):
    """Debugger V2 Plugin for TensorBoard."""
    plugin_name: Incomplete
    def __init__(self, context) -> None:
        """Instantiates Debugger V2 Plugin via TensorBoard core.

        Args:
          context: A base_plugin.TBContext instance.
        """
    def get_plugin_apps(self): ...
    def is_active(self):
        """The Debugger V2 plugin must be manually selected."""
    def frontend_metadata(self): ...
    def serve_runs(self, request): ...
    def serve_alerts(self, request): ...
    def serve_execution_digests(self, request): ...
    def serve_execution_data(self, request): ...
    def serve_graph_execution_digests(self, request):
        """Serve digests of intra-graph execution events.

        As the names imply, this route differs from `serve_execution_digests()`
        in that it is for intra-graph execution, while `serve_execution_digests()`
        is for top-level (eager) execution.
        """
    def serve_graph_execution_data(self, request):
        """Serve detailed data objects of intra-graph execution events.

        As the names imply, this route differs from `serve_execution_data()`
        in that it is for intra-graph execution, while `serve_execution_data()`
        is for top-level (eager) execution.

        Unlike `serve_graph_execution_digests()`, this method serves the
        full-sized data objects for intra-graph execution events.
        """
    def serve_graph_info(self, request):
        '''Serve basic information about a TensorFlow graph.

        The request specifies the debugger-generated ID of the graph being
        queried.

        The response contains a JSON object with the following fields:
          - graph_id: The debugger-generated ID (echoing the request).
          - name: The name of the graph (if any). For TensorFlow 2.x
            Function Graphs (FuncGraphs), this is typically the name of
            the underlying Python function, optionally prefixed with
            TensorFlow-generated prefixed such as "__inference_".
            Some graphs (e.g., certain outermost graphs) may have no names,
            in which case this field is `null`.
          - outer_graph_id: Outer graph ID (if any). For an outermost graph
            without an outer graph context, this field is `null`.
          - inner_graph_ids: Debugger-generated IDs of all the graphs
            nested inside this graph. For a graph without any graphs nested
            inside, this field is an empty array.
        '''
    def serve_graph_op_info(self, request):
        """Serve information for ops in graphs.

        The request specifies the op name and the ID of the graph that
        contains the op.

        The response contains a JSON object with the following fields:
          - op_type
          - op_name
          - graph_ids: Stack of graph IDs that the op is located in, from
            outermost to innermost. The length of this array is always >= 1.
            The length is 1 if and only if the graph is an outermost graph.
          - num_outputs: Number of output tensors.
          - output_tensor_ids: The debugger-generated number IDs for the
            symbolic output tensors of the op (an array of numbers).
          - host_name: Name of the host on which the op is created.
          - stack_trace: Stack frames of the op's creation.
          - inputs: Specifications of all inputs to this op.
            Currently only immediate (one level of) inputs are provided.
            This is an array of length N_in, where N_in is the number of
            data inputs received by the op. Each element of the array is an
            object with the following fields:
              - op_name: Name of the op that provides the input tensor.
              - output_slot: 0-based output slot index from which the input
                tensor emits.
              - data: A recursive data structure of this same schema.
                This field is not populated (undefined) at the leaf nodes
                of this recursive data structure.
                In the rare case wherein the data for an input cannot be
                retrieved properly (e.g., special internal op types), this
                field will be unpopulated.
            This is an empty list for an op with no inputs.
          - consumers: Specifications for all the downstream consuming ops of
            this. Currently only immediate (one level of) consumers are provided.
            This is an array of length N_out, where N_out is the number of
            symbolic tensors output by this op.
            Each element of the array is an array of which the length equals
            the number of downstream ops that consume the corresponding symbolic
            tensor (only data edges are tracked).
            Each element of the array is an object with the following fields:
              - op_name: Name of the op that receives the output tensor as an
                input.
              - input_slot: 0-based input slot index at which the downstream
                op receives this output tensor.
              - data: A recursive data structure of this very schema.
                This field is not populated (undefined) at the leaf nodes
                of this recursive data structure.
                In the rare case wherein the data for a consumer op cannot be
                retrieved properly (e.g., special internal op types), this
                field will be unpopulated.
            If this op has no output tensors, this is an empty array.
            If one of the output tensors of this op has no consumers, the
            corresponding element is an empty array.
        """
    def serve_source_files_list(self, request):
        """Serves a list of all source files involved in the debugged program."""
    def serve_source_file(self, request):
        """Serves the content of a given source file.

        The source file is referred to by the index in the list of all source
        files involved in the execution of the debugged program, which is
        available via the `serve_source_files_list()`  serving route.

        Args:
          request: HTTP request.

        Returns:
          Response to the request.
        """
    def serve_stack_frames(self, request):
        """Serves the content of stack frames.

        The source frames being requested are referred to be UUIDs for each of
        them, separated by commas.

        Args:
          request: HTTP request.

        Returns:
          Response to the request.
        """
