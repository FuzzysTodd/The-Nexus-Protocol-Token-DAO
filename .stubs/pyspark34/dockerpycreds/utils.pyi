from _typeshed import Incomplete

def find_executable(executable, path: Incomplete | None = None):
    """
    As distutils.spawn.find_executable, but on Windows, look up
    every extension declared in PATHEXT instead of just `.exe`
    """
def create_environment_dict(overrides):
    """
    Create and return a copy of os.environ with the specified overrides
    """
