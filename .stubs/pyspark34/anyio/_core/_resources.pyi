from ..abc import AsyncResource as AsyncResource
from ._tasks import CancelScope as CancelScope

async def aclose_forcefully(resource: AsyncResource) -> None:
    """
    Close an asynchronous resource in a cancelled scope.

    Doing this closes the resource without waiting on anything.

    :param resource: the resource to close

    """
