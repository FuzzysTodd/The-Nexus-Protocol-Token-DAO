from .wandb_logging import wandb_log as wandb_log
from _typeshed import Incomplete
from typing import Callable, List, Mapping

MIN_KFP_VERSION: str
decorator_code: Incomplete
wandb_logging_extras: Incomplete

def full_path_exists(full_func): ...
def patch(module_name, func): ...
def unpatch(module_name) -> None: ...
def unpatch_kfp() -> None: ...
def patch_kfp() -> None: ...
def create_component_from_func(func: Callable, output_component_file: str | None = None, base_image: str | None = None, packages_to_install: List[str] | None = None, annotations: Mapping[str, str] | None = None):
    '''Convert a Python function to a component and returns a task factory.

    The returned task factory accepts arguments and returns a task object.

    This function is modified from KFP.  The original source is below:
    https://github.com/kubeflow/pipelines/blob/b6406b02f45cdb195c7b99e2f6d22bf85b12268b/sdk/python/kfp/components/_python_op.py#L998-L1110.

    Args:
        func: The python function to convert
        base_image: Optional. Specify a custom Docker container image to use in the component. For lightweight components, the image needs to have python 3.5+. Default is the python image corresponding to the current python environment.
        output_component_file: Optional. Write a component definition to a local file. The produced component file can be loaded back by calling :code:`load_component_from_file` or :code:`load_component_from_uri`.
        packages_to_install: Optional. List of [versioned] python packages to pip install before executing the user function.
        annotations: Optional. Allows adding arbitrary key-value data to the component specification.

    Returns:
        A factory function with a strongly-typed signature taken from the python function.
        Once called with the required arguments, the factory constructs a task instance that can run the original function in a container.

    Examples:
        The function name and docstring are used as component name and description. Argument and return annotations are used as component input/output types::

            def add(a: float, b: float) -> float:
                """Return sum of two arguments"""
                return a + b

            # add_op is a task factory function that creates a task object when given arguments
            add_op = create_component_from_func(
                func=add,
                base_image=\'python:3.7\', # Optional
                output_component_file=\'add.component.yaml\', # Optional
                packages_to_install=[\'pandas==0.24\'], # Optional
            )

            # The component spec can be accessed through the .component_spec attribute:
            add_op.component_spec.save(\'add.component.yaml\')

            # The component function can be called with arguments to create a task:
            add_task = add_op(1, 3)

            # The resulting task has output references, corresponding to the component outputs.
            # When the function only has a single anonymous return value, the output name is "Output":
            sum_output_ref = add_task.outputs[\'Output\']

            # These task output references can be passed to other component functions, constructing a computation graph:
            task2 = add_op(sum_output_ref, 5)


        :code:`create_component_from_func` function can also be used as decorator::

            @create_component_from_func
            def add_op(a: float, b: float) -> float:
                """Return sum of two arguments"""
                return a + b

        To declare a function with multiple return values, use the :code:`NamedTuple` return annotation syntax::

            from typing import NamedTuple

            def add_multiply_two_numbers(a: float, b: float) -> NamedTuple(\'Outputs\', [(\'sum\', float), (\'product\', float)]):
                """Return sum and product of two arguments"""
                return (a + b, a * b)

            add_multiply_op = create_component_from_func(add_multiply_two_numbers)

            # The component function can be called with arguments to create a task:
            add_multiply_task = add_multiply_op(1, 3)

            # The resulting task has output references, corresponding to the component outputs:
            sum_output_ref = add_multiply_task.outputs[\'sum\']

            # These task output references can be passed to other component functions, constructing a computation graph:
            task2 = add_multiply_op(sum_output_ref, 5)

        Bigger data should be read from files and written to files.
        Use the :py:class:`kfp.components.InputPath` parameter annotation to tell the system that the function wants to consume the corresponding input data as a file. The system will download the data, write it to a local file and then pass the **path** of that file to the function.
        Use the :py:class:`kfp.components.OutputPath` parameter annotation to tell the system that the function wants to produce the corresponding output data as a file. The system will prepare and pass the **path** of a file where the function should write the output data. After the function exits, the system will upload the data to the storage system so that it can be passed to downstream components.

        You can specify the type of the consumed/produced data by specifying the type argument to :py:class:`kfp.components.InputPath` and :py:class:`kfp.components.OutputPath`. The type can be a python type or an arbitrary type name string. :code:`OutputPath(\'CatBoostModel\')` means that the function states that the data it has written to a file has type :code:`CatBoostModel`. :code:`InputPath(\'CatBoostModel\')` means that the function states that it expect the data it reads from a file to have type \'CatBoostModel\'. When the pipeline author connects inputs to outputs the system checks whether the types match.
        Every kind of data can be consumed as a file input. Conversely, bigger data should not be consumed by value as all value inputs pass through the command line.

        Example of a component function declaring file input and output::

            def catboost_train_classifier(
                training_data_path: InputPath(\'CSV\'),            # Path to input data file of type "CSV"
                trained_model_path: OutputPath(\'CatBoostModel\'), # Path to output data file of type "CatBoostModel"
                number_of_trees: int = 100,                      # Small output of type "Integer"
            ) -> NamedTuple(\'Outputs\', [
                (\'Accuracy\', float),  # Small output of type "Float"
                (\'Precision\', float), # Small output of type "Float"
                (\'JobUri\', \'URI\'),    # Small output of type "URI"
            ]):
                """Train CatBoost classification model"""
                ...

                return (accuracy, precision, recall)
    '''
def strip_type_hints(source_code: str) -> str:
    """Strip type hints from source code.

    This function is modified from KFP.  The original source is below:
    https://github.com/kubeflow/pipelines/blob/b6406b02f45cdb195c7b99e2f6d22bf85b12268b/sdk/python/kfp/components/_python_op.py#L237-L248.
    """
