from pbr.hooks import backwards as backwards, commands as commands, files as files, metadata as metadata

def setup_hook(config) -> None:
    """Filter config parsed from a setup.cfg to inject our defaults."""
