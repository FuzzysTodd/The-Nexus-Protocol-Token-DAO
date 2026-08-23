from _typeshed import Incomplete

class ShowProgress:
    """ This is a simple wrapper around tqdm that includes a starting delay before printing.
    """
    iter: Incomplete
    start_time: Incomplete
    pbar: Incomplete
    total: Incomplete
    desc: Incomplete
    start_delay: Incomplete
    silent: Incomplete
    unshown_count: int
    def __init__(self, iterable, total, desc, silent, start_delay) -> None: ...
    def __next__(self): ...
    def __iter__(self): ...

def show_progress(iterable, total: Incomplete | None = None, desc: Incomplete | None = None, silent: bool = False, start_delay: int = 10): ...
