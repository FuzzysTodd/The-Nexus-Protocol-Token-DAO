from typing import List

class ResourceInformation:
    """
    Class to hold information about a type of Resource. A resource could be a GPU, FPGA, etc.
    The array of addresses are resource specific and its up to the user to interpret the address.

    One example is GPUs, where the addresses would be the indices of the GPUs

    .. versionadded:: 3.0.0

    Parameters
    ----------
    name : str
        the name of the resource
    addresses : list
        a list of strings describing the addresses of the resource

    Notes
    -----
    This API is evolving.

    See Also
    --------
    :class:`pyspark.resource.ResourceProfile`
    """
    def __init__(self, name: str, addresses: List[str]) -> None: ...
    @property
    def name(self) -> str:
        """
        Returns
        -------
        str
            the name of the resource
        """
    @property
    def addresses(self) -> List[str]:
        """
        Returns
        -------
        list
            a list of strings describing the addresses of the resource
        """
