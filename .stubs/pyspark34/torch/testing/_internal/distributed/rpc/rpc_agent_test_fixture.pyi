import abc
from abc import ABC, abstractmethod

class RpcAgentTestFixture(ABC, metaclass=abc.ABCMeta):
    @property
    def world_size(self) -> int: ...
    @property
    def init_method(self): ...
    @property
    def file_init_method(self): ...
    @property
    @abstractmethod
    def rpc_backend(self): ...
    @property
    @abstractmethod
    def rpc_backend_options(self): ...
    def setup_fault_injection(self, faulty_messages, messages_to_delay) -> None:
        """Method used by dist_init to prepare the faulty agent.

        Does nothing for other agents.
        """
    @abstractmethod
    def get_shutdown_error_regex(self):
        """
        Return various error message we may see from RPC agents while running
        tests that check for failures. This function is used to match against
        possible errors to ensure failures were raised properly.
        """
    @abstractmethod
    def get_timeout_error_regex(self):
        """
        Returns a partial string indicating the error we should receive when an
        RPC has timed out. Useful for use with assertRaisesRegex() to ensure we
        have the right errors during timeout.
        """
