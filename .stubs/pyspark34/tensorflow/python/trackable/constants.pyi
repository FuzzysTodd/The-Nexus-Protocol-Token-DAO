import enum

OBJECT_GRAPH_PROTO_KEY: str
VARIABLE_VALUE_KEY: str
OBJECT_CONFIG_JSON_KEY: str

class SaveType(str, enum.Enum):
    SAVEDMODEL: str
    CHECKPOINT: str
