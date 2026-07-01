class _ExtensionDict:
    """Dict-like container for Extension fields on proto instances.

  Note that in all cases we expect extension handles to be
  FieldDescriptors.
  """
    def __init__(self, extended_message) -> None:
        """
    Args:
      extended_message: Message instance for which we are the Extensions dict.
    """
    def __getitem__(self, extension_handle):
        """Returns the current value of the given extension handle."""
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __len__(self) -> int: ...
    def __hash__(self): ...
    def __setitem__(self, extension_handle, value) -> None:
        """If extension_handle specifies a non-repeated, scalar extension
    field, sets the value of that field.
    """
    def __delitem__(self, extension_handle) -> None: ...
    def __iter__(self): ...
    def __contains__(self, extension_handle) -> bool: ...
