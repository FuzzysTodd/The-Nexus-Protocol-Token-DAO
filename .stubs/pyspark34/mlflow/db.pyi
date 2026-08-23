def commands() -> None:
    """
    Commands for managing an MLflow tracking database.
    """
def upgrade(url) -> None:
    """
    Upgrade the schema of an MLflow tracking database to the latest supported version.

    **IMPORTANT**: Schema migrations can be slow and are not guaranteed to be transactional -
    **always take a backup of your database before running migrations**. The migrations README,
    which is located at
    https://github.com/mlflow/mlflow/blob/master/mlflow/store/db_migrations/README.md, describes
    large migrations and includes information about how to estimate their performance and
    recover from failures.
    """
