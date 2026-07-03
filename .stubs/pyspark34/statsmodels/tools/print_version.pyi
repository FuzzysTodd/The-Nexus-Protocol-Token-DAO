def safe_version(module, attr: str = '__version__', *others): ...
def show_versions(show_dirs: bool = True) -> None:
    """
    List the versions of statsmodels and any installed dependencies

    Parameters
    ----------
    show_dirs : bool
        Flag indicating to show module locations
    """
