from enum import Enum

class ExpiryOptionType(Enum):
    never_expire: str
    relative_to_now: str
    relative_to_creation_date: str
    absolute: str
