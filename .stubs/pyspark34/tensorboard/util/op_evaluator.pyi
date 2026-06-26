class PersistentOpEvaluator:
    '''Evaluate a fixed TensorFlow graph repeatedly, safely, efficiently.

    Extend this class to create a particular kind of op evaluator, like an
    image encoder. In `initialize_graph`, create an appropriate TensorFlow
    graph with placeholder inputs. In `run`, evaluate this graph and
    return its result. This class will manage a singleton graph and
    session to preserve memory usage, and will ensure that this graph and
    session do not interfere with other concurrent sessions.

    A subclass of this class offers a threadsafe, highly parallel Python
    entry point for evaluating a particular TensorFlow graph.

    Example usage:

        class FluxCapacitanceEvaluator(PersistentOpEvaluator):
          """Compute the flux capacitance required for a system.

          Arguments:
            x: Available power input, as a `float`, in jigawatts.

          Returns:
            A `float`, in nanofarads.
          """

          def initialize_graph(self):
            self._placeholder = tf.placeholder(some_dtype)
            self._op = some_op(self._placeholder)

          def run(self, x):
            return self._op.eval(feed_dict: {self._placeholder: x})

        evaluate_flux_capacitance = FluxCapacitanceEvaluator()

        for x in xs:
          evaluate_flux_capacitance(x)
    '''
    def __init__(self) -> None: ...
    def initialize_graph(self) -> None:
        """Create the TensorFlow graph needed to compute this operation.

        This should write ops to the default graph and return `None`.
        """
    def run(self, *args, **kwargs) -> None:
        """Evaluate the ops with the given input.

        When this function is called, the default session will have the
        graph defined by a previous call to `initialize_graph`. This
        function should evaluate any ops necessary to compute the result
        of the query for the given *args and **kwargs, likely returning
        the result of a call to `some_op.eval(...)`.
        """
    def __call__(self, *args, **kwargs): ...
