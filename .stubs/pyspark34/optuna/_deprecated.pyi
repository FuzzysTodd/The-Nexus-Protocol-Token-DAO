from typing import Any

def deprecated(deprecated_version: str, removed_version: str | None = None, name: str | None = None, text: str | None = None) -> Any:
    '''Decorate class or function as deprecated.

    Args:
        deprecated_version:
            The version in which the target feature is deprecated.
        removed_version:
            The version in which the target feature will be removed. If :obj:`None`, determined
            based on the deprecated version. In this case, it will become the next next major
            version after the deprecated version. E.g. if ``deprecated_version`` is ``1.5.0``,
            this version becomes ``3.0.0``.
        name:
            The name of the feature. Defaults to the function or class name. Optional.
        text:
            The additional text for the deprecation note. The default note is build using specified
            ``deprecated_version`` and ``removed_version``. If you want to provide additional
            information, please specify this argument yourself.

            .. note::
                The default deprecation note is as follows: "Deprecated in v{d_ver}. This feature
                will be removed in the future. The removal of this feature is currently scheduled
                for v{r_ver}, but this schedule is subject to change. See
                https://github.com/optuna/optuna/releases/tag/v{d_ver}."

            .. note::
                The specified text is concatenated after the default deprecation note.
    '''
