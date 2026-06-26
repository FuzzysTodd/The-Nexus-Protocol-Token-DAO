LOCAL_IPS: list
PUBLIC_IPS: list
LOCALHOST: str

class NoIPAddresses(Exception): ...

def local_ips() -> list[str]:
    """return the IP addresses that point to this machine"""
def public_ips() -> list[str]:
    """return the IP addresses for this machine that are visible to other machines"""
def localhost() -> str:
    """return ip for localhost (almost always 127.0.0.1)"""
def is_local_ip(ip: str) -> bool:
    """does `ip` point to this machine?"""
def is_public_ip(ip: str) -> bool:
    """is `ip` a publicly visible address?"""
