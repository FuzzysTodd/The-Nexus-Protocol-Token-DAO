from .hub import QuietHub as QuietHub
from .patched_tests_setup import get_switch_expected as get_switch_expected

def wrap_switch_count_check(method): ...

class CountingHub(QuietHub):
    switch_count: int
    def switch(self, *args): ...
