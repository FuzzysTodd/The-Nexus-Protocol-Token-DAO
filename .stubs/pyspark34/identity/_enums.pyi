from azure.core import CaseInsensitiveEnumMeta
from enum import Enum

class RegionalAuthority(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Identifies a regional authority for authentication"""
    AUTO_DISCOVER_REGION: str
    ASIA_EAST: str
    ASIA_SOUTHEAST: str
    AUSTRALIA_CENTRAL: str
    AUSTRALIA_CENTRAL_2: str
    AUSTRALIA_EAST: str
    AUSTRALIA_SOUTHEAST: str
    BRAZIL_SOUTH: str
    CANADA_CENTRAL: str
    CANADA_EAST: str
    CHINA_EAST: str
    CHINA_EAST_2: str
    CHINA_NORTH: str
    CHINA_NORTH_2: str
    EUROPE_NORTH: str
    EUROPE_WEST: str
    FRANCE_CENTRAL: str
    FRANCE_SOUTH: str
    GERMANY_CENTRAL: str
    GERMANY_NORTH: str
    GERMANY_NORTHEAST: str
    GERMANY_WEST_CENTRAL: str
    GOVERNMENT_US_ARIZONA: str
    GOVERNMENT_US_DOD_CENTRAL: str
    GOVERNMENT_US_DOD_EAST: str
    GOVERNMENT_US_IOWA: str
    GOVERNMENT_US_TEXAS: str
    GOVERNMENT_US_VIRGINIA: str
    INDIA_CENTRAL: str
    INDIA_SOUTH: str
    INDIA_WEST: str
    JAPAN_EAST: str
    JAPAN_WEST: str
    KOREA_CENTRAL: str
    KOREA_SOUTH: str
    NORWAY_EAST: str
    NORWAY_WEST: str
    SOUTH_AFRICA_NORTH: str
    SOUTH_AFRICA_WEST: str
    SWITZERLAND_NORTH: str
    SWITZERLAND_WEST: str
    UAE_CENTRAL: str
    UAE_NORTH: str
    UK_SOUTH: str
    UK_WEST: str
    US_CENTRAL: str
    US_EAST: str
    US_EAST_2: str
    US_NORTH_CENTRAL: str
    US_SOUTH_CENTRAL: str
    US_WEST: str
    US_WEST_2: str
    US_WEST_CENTRAL: str
