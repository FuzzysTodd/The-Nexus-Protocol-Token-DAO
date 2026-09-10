from _typeshed import Incomplete
from collections.abc import Generator

HAVE_MATPLOTLIB: bool
logger: Incomplete
cow: bool

def pytest_addoption(parser) -> None: ...
def pytest_runtest_setup(item) -> None: ...
def pytest_configure(config) -> None: ...
def close_figures() -> Generator[Incomplete, None, None]:
    """
    Fixture that closes all figures after a test function has completed

    Returns
    -------
    closer : callable
        Function that will close all figures when called.

    Notes
    -----
    Used by passing as an argument to the function that produces a plot,
    for example

    def test_some_plot(close_figures):
        <test code>

    If a function creates many figures, then these can be destroyed within a
    test function by calling close_figures to ensure that the number of
    figures does not become too large.

    def test_many_plots(close_figures):
        for i in range(100000):
            plt.plot(x,y)
            close_figures()
    """
def reset_randomstate() -> Generator[None, None, None]:
    """
    Fixture that set the global RandomState to the fixed seed 1

    Notes
    -----
    Used by passing as an argument to the function that uses the global
    RandomState

    def test_some_plot(reset_randomstate):
        <test code>

    Returns the state after the test function exits
    """
