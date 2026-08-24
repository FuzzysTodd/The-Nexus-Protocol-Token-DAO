def test_trivial() -> None:
    """A trivial passing test."""
def doctest_run() -> None:
    """Test running a trivial script.

    In [13]: run simplevars.py
    x is: 1
    """
def doctest_runvars() -> None:
    """Test that variables defined in scripts get loaded correctly via %run.

    In [13]: run simplevars.py
    x is: 1

    In [14]: x
    Out[14]: 1
    """
def doctest_ivars() -> None:
    """Test that variables defined interactively are picked up.
    In [5]: zz=1

    In [6]: zz
    Out[6]: 1
    """
