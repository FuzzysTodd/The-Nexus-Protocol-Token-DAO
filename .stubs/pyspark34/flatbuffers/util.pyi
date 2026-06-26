from . import encode as encode, number_types as number_types, packer as packer

def GetSizePrefix(buf, offset):
    """Extract the size prefix from a buffer."""
def GetBufferIdentifier(buf, offset, size_prefixed: bool = False):
    """Extract the file_identifier from a buffer"""
def BufferHasIdentifier(buf, offset, file_identifier, size_prefixed: bool = False): ...
def RemoveSizePrefix(buf, offset):
    """
\tCreate a slice of a size-prefixed buffer that has
\tits position advanced just past the size prefix.
\t"""
