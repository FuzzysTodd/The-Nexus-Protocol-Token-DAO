from _typeshed import Incomplete

class DeterministicRandomTestTool:
    """DeterministicRandomTestTool is a testing tool.

    This tool is used to validate random number generation semantics match
    between TF1.x graphs/sessions and eager execution.

    This is useful when you are migrating from TF 1.x to TF2 and need to make
    sure your computation is still happening correctly along the way. See the
    validating correctness migration guide for more info:
    https://www.tensorflow.org/guide/migrate/validate_correctness

    The following DeterministicRandomTestTool object provides a context manager
    scope() that can make stateful random operations use the same seed across
    both TF1 graphs/sessions and eager execution,The tool provides two testing
    modes:
    - constant which uses the same seed for every single operation no matter how
    many times it has been called and,
    - num_random_ops which uses the number of previously-observed stateful
    random operations as the operation seed.
    The num_random_ops mode serves as a more sensitive validation check than the
    constant mode. It ensures that the random numbers initialization does not
    get accidentaly reused.(for example if several weights take on the same
    initializations), you can use the num_random_ops mode to avoid this. In the
    num_random_ops mode, the generated random numbers will depend on the
    ordering of random ops in the program.

    This applies both to the stateful random operations used for creating and
    initializing variables, and to the stateful random operations used in
    computation (such as for dropout layers).
    """
    seed_implementation: Incomplete
    def __init__(self, seed: int = 42, mode: str = 'constant') -> None:
        """Set mode to 'constant' or 'num_random_ops'. Defaults to
        'constant'."""
    @property
    def operation_seed(self): ...
    @operation_seed.setter
    def operation_seed(self, value) -> None: ...
    def scope(self):
        """set random seed."""
