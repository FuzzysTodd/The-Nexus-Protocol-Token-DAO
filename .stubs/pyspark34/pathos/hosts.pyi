from _typeshed import Incomplete

default_profile: str

def get_profile(rhost, assume: bool = True):
    """get the default $PROFILE for a remote host"""
def get_profiles():
    """get $PROFILE for each registered host"""
def register_profiles(profiles) -> None:
    """add dict of {'host':$PROFILE} to registered host profiles"""
def register(rhost, profile: Incomplete | None = None) -> None:
    """register a host and $PROFILE"""
