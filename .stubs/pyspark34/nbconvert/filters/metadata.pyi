from _typeshed import Incomplete

def get_metadata(output, key, mimetype: Incomplete | None = None):
    """Resolve an output metadata key

    If mimetype given, resolve at mimetype level first,
    then fallback to top-level.
    Otherwise, just resolve at top-level.
    Returns None if no data found.
    """
