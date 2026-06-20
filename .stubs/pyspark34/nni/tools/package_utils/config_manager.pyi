from .common import AlgoMeta

__all__ = ['get_algo_meta', 'get_all_algo_meta', 'register_algo_meta', 'unregister_algo_meta']

def get_algo_meta(name: str) -> AlgoMeta | None:
    """
    Get meta information of a built-in or registered algorithm.
    Return None if not found.
    """
def get_all_algo_meta() -> list[AlgoMeta]:
    """
    Get meta information of all built-in and registered algorithms.
    """
def register_algo_meta(algo_meta: AlgoMeta) -> None:
    """
    Register a custom algorithm.
    If it already exists, overwrite it.
    """
def unregister_algo_meta(algo_name: str) -> None:
    """
    Unregister a custom algorithm.
    If it does not exist, do nothing.
    """
