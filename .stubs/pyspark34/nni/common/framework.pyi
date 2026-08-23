__all__ = ['set_default_framework', 'get_default_framework', 'shortcut_module', 'shortcut_framework']

def set_default_framework(framework: framework_type) -> None:
    '''Set default deep learning framework to simplify imports.

    Some functionalities in NNI (e.g., NAS / Compression), relies on an underlying DL framework.
    For different DL frameworks, the implementation of NNI can be very different.
    Thus, users need import things tailored for their own framework. For example: ::

        from nni.nas.xxx.pytorch import yyy

    rather than: ::

        from nni.nas.xxx import yyy

    By setting a default framework, shortcuts will be made. As such ``nni.nas.xxx`` will be equivalent to ``nni.nas.xxx.pytorch``.

    Another way to setting it is through environment variable ``NNI_FRAMEWORK``,
    which needs to be set before the whole process starts.

    If you set the framework with :func:`set_default_framework`,
    it should be done before all imports (except nni itself) happen,
    because it will affect other import\'s behaviors.
    And the behavior is undefined if the framework is "re"-set in the middle.

    The supported frameworks here are listed below.
    It doesn\'t mean that they are fully supported by NAS / Compression in NNI.

    * ``pytorch`` (default)
    * ``tensorflow``
    * ``mxnet``
    * ``none`` (to disable the shortcut-import behavior).

    Examples
    --------
    >>> import nni
    >>> nni.set_default_framework(\'tensorflow\')
    >>> # then other imports
    >>> from nni.nas.xxx import yyy
    '''
def get_default_framework() -> framework_type:
    """Retrieve default deep learning framework set either with env variables or manually."""
def shortcut_module(current: str, target: str, package: str | None = None) -> None:
    """Make ``current`` module an alias of ``target`` module in ``package``."""
def shortcut_framework(current: str) -> None:
    """Make ``current`` a shortcut of ``current.framework``."""
