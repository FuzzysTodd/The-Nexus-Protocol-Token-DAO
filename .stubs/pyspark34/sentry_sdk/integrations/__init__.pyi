from _typeshed import Incomplete
from sentry_sdk._compat import iteritems as iteritems
from sentry_sdk._types import TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.utils import logger as logger
from typing import Dict, List

iter_default_integrations: Incomplete

def setup_integrations(integrations: List[Integration], with_defaults: bool = True, with_auto_enabling_integrations: bool = False) -> Dict[str, Integration]:
    """
    Given a list of integration instances, this installs them all.

    When `with_defaults` is set to `True` all default integrations are added
    unless they were already provided before.
    """

class DidNotEnable(Exception):
    """
    The integration could not be enabled due to a trivial user error like
    `flask` not being installed for the `FlaskIntegration`.

    This exception is silently swallowed for default integrations, but reraised
    for explicitly enabled integrations.
    """

class Integration:
    """Baseclass for all integrations.

    To accept options for an integration, implement your own constructor that
    saves those options on `self`.
    """
    install: Incomplete
    identifier: str
    @staticmethod
    def setup_once() -> None:
        """
        Initialize the integration.

        This function is only called once, ever. Configuration is not available
        at this point, so the only thing to do here is to hook into exception
        handlers, and perhaps do monkeypatches.

        Inside those hooks `Integration.current` can be used to access the
        instance again.
        """
