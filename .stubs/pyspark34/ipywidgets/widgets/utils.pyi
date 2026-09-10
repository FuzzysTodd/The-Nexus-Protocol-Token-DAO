def deprecation(message, internal: str = 'ipywidgets/widgets/') -> None:
    """Generate a deprecation warning targeting the first frame that is not 'internal'
    
    internal is a string or list of strings, which if they appear in filenames in the
    frames, the frames will be considered internal. Changing this can be useful if, for examnple,
    we know that ipywidgets is calling out to traitlets internally.
    """
