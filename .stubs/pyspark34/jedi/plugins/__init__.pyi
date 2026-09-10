from _typeshed import Incomplete

class _PluginManager:
    def __init__(self) -> None: ...
    def register(self, *plugins) -> None:
        """
        Makes it possible to register your plugin.
        """
    def decorate(self, name: Incomplete | None = None): ...

plugin_manager: Incomplete
