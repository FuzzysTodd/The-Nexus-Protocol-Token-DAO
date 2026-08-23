from collections.abc import Generator
from scipy._lib._fpumode import get_fpu_mode as get_fpu_mode
from scipy._lib._testutils import FPUModeChangeWarning as FPUModeChangeWarning

def pytest_configure(config) -> None: ...
def pytest_runtest_setup(item) -> None: ...
def check_fpu_mode(request) -> Generator[None, None, None]:
    """
    Check FPU mode was not changed during the test.
    """
