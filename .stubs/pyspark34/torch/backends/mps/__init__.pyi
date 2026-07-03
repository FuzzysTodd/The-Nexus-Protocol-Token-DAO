__all__ = ['is_built', 'is_available', 'is_macos13_or_newer']

def is_built() -> bool:
    """Returns whether PyTorch is built with MPS support. Note that this
    doesn't necessarily mean MPS is available; just that if this PyTorch
    binary were run a machine with working MPS drivers and devices, we
    would be able to use it."""
def is_available() -> bool:
    """Returns a bool indicating if MPS is currently available."""
def is_macos13_or_newer() -> bool:
    """Returns a bool indicating whether MPS is running on MacOS 13 or newer."""
