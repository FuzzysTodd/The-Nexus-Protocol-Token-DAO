__all__ = ['test']

def test(extra_args: list[str] | None = None) -> None:
    """
    Run the pandas test suite using pytest.

    By default, runs with the marks --skip-slow, --skip-network, --skip-db

    Parameters
    ----------
    extra_args : list[str], default None
        Extra marks to run the tests.
    """
