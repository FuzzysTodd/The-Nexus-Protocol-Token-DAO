def disable_importlib_metadata_finder(metadata) -> None:
    """
    Ensure importlib_metadata doesn't provide older, incompatible
    Distributions.

    Workaround for #3102.
    """
