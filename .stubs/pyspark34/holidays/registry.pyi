from _typeshed import Incomplete
from holidays.holiday_base import HolidayBase as HolidayBase
from typing import Any, Dict, Iterable, Tuple

RegistryDict = Dict[str, Tuple[str, ...]]
COUNTRIES: RegistryDict
FINANCIAL: RegistryDict

class EntityLoader:
    """Country and financial holidays entities lazy loader."""
    entity: Incomplete
    entity_name: Incomplete
    module_name: Incomplete
    def __init__(self, path: str, *args, **kwargs) -> None:
        """Set up a lazy loader."""
    def __call__(self, *args, **kwargs) -> HolidayBase:
        """Create a new instance of a lazy-loaded entity."""
    def __getattr__(self, name: str) -> Any | None:
        """Return attribute of a lazy-loaded entity."""
    def get_entity(self) -> HolidayBase | None:
        """Return lazy-loaded entity."""
    @staticmethod
    def get_country_codes(include_aliases: bool = True) -> Iterable[str]:
        """Get supported country codes.

        :param include_aliases:
            Whether to include entity aliases (e.g. UK for GB).
        """
    @staticmethod
    def get_financial_codes(include_aliases: bool = True) -> Iterable[str]:
        """Get supported financial codes.

        :param include_aliases:
            Whether to include entity aliases(e.g. TAR for ECB, XNYS for NYSE).
        """
    @staticmethod
    def load(prefix: str, scope: Dict) -> None:
        """Load country or financial entities."""
