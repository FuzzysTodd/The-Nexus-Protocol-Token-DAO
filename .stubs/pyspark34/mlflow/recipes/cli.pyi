from mlflow.recipes import Recipe as Recipe

def commands() -> None:
    """
    Run MLflow Recipes and inspect recipe results.
    """
def run(step, profile) -> None:
    """
    Run the full recipe, or run a particular recipe step if specified, producing
    outputs and displaying a summary of results upon completion.
    """
def clean(step, profile) -> None:
    """
    Remove all recipe outputs from the cache, or remove the cached outputs of a particular
    recipe step if specified. After cached outputs are cleaned for a particular step, the step
    will be re-executed in its entirety the next time it is run.
    """
def inspect(step, profile) -> None:
    """
    Display a visual overview of the recipe graph, or display a summary of results from a
    particular recipe step if specified. If the specified step has not been executed,
    nothing is displayed.
    """
def get_artifact(profile, artifact) -> None:
    """
    Get the location of an artifact output from the recipe.
    """
