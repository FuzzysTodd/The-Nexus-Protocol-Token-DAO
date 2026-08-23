__version__: str

def server_binary():
    """Return the path to a TensorBoard data server binary, if possible.

    Returns:
      A string path on disk, or `None` if there is no binary bundled
      with this package.
    """
