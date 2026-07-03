from enum import Enum, IntEnum

class Permissions(IntEnum):
    READ: int
    READWRITE: int
    COPY: int
    CREATE: int
    ALL: int

class TokenType(IntEnum):
    AAD: int
    EMBED: int

class EmbedMode(IntEnum):
    VIEW: int
    EDIT: int
    CREATE: int

class ExportDataType(IntEnum):
    SUMMARIZED: int
    UNDERLYING: int

class ReportCreationMode(Enum):
    DEFAULT: str
    QUICK_EXPLORE: str

class DataType(Enum):
    NUMBER: str
    CURRENCY: str
    INT32: str
    PERCENTAGE: str
    DATE_TIME: str
    DATE_TIME_ZONE: str
    DATE: str
    TIME: str
    DURATION: str
    TEXT: str
    LOGICAL: str
    BINARY: str
