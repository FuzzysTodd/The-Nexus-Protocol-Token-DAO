from typing_extensions import Final

WILDCARD_TAG: Final[str]

def make_trigger(name: str) -> str: ...
def make_wildcard_trigger(module: str) -> str:
    '''Special trigger fired when any top-level name is changed in a module.

    Note that this is different from a module trigger, as module triggers are only
    fired if the module is created, deleted, or replaced with a non-module, whereas
    a wildcard trigger is triggered for namespace changes.

    This is used for "from m import *" dependencies.
    '''
