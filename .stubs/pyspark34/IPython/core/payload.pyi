from traitlets.config.configurable import Configurable

class PayloadManager(Configurable):
    def write_payload(self, data, single: bool = True) -> None:
        """Include or update the specified `data` payload in the PayloadManager.

        If a previous payload with the same source exists and `single` is True,
        it will be overwritten with the new one.
        """
    def read_payload(self): ...
    def clear_payload(self) -> None: ...
