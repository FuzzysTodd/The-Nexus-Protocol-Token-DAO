import abc
from .._version import __version__ as __version__
from ._environment import ENV_DETECTED as ENV_DETECTED, EnvironmentDetector as EnvironmentDetector, is_cloud_env as is_cloud_env
from _typeshed import Incomplete
from abc import ABC, abstractmethod

JS_URL: Incomplete

class VisualizeProvider(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def render(self, explanation, key: int = -1, **kwargs): ...

class AutoVisualizeProvider(VisualizeProvider):
    has_initialized: bool
    environment_detector: Incomplete
    in_cloud_env: Incomplete
    provider: Incomplete
    app_runner: Incomplete
    kwargs: Incomplete
    def __init__(self, app_runner: Incomplete | None = None, **kwargs) -> None: ...
    def render(self, explanation, key: int = -1, **kwargs) -> None: ...

class PreserveProvider(VisualizeProvider):
    def render(self, explanation, key: int = -1, **kwargs) -> None: ...

class DashProvider(VisualizeProvider):
    """Provides rendering via Plotly's Dash.

    This works in the event of an environment that can expose HTTP(s) ports.
    """
    app_runner: Incomplete
    def __init__(self, app_runner) -> None:
        """Initializes class.

        This requires an instantiated `AppRunner`, call `.from_address` instead
        to initialize both.

        Args:
            app_runner: An AppRunner instance.
        """
    @classmethod
    def from_address(cls, addr: Incomplete | None = None, base_url: Incomplete | None = None, use_relative_links: bool = False):
        """Initialize a new `AppRunner` along with the provider.

        Args:
            addr: A tuple that is (ip_addr, port).
            base_url: Base URL, this useful when behind a proxy.
            use_relative_links: Relative links for rendered pages instead of full URI.
        """
    def idempotent_start(self) -> None: ...
    def link(self, explanation, **kwargs): ...
    def render(self, explanation, **kwargs) -> None: ...

class InlineProvider(VisualizeProvider):
    """Provides rendering via JavaScript that are invoked within Jupyter cells."""
    detected_envs: Incomplete
    js_url: Incomplete
    def __init__(self, detected_envs: Incomplete | None = None, js_url: Incomplete | None = None) -> None:
        """Initializes class.

        Args:
            detected_envs: Environments targetted as defined in `interpret.utils.environment`.
            js_url: If defined, will load the JavaScript bundle for interpret-inline from the given URL.
        """
    def render(self, explanation, key: int = -1, **kwargs) -> None: ...
