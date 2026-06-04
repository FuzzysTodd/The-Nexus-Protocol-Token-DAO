import json
from _typeshed import Incomplete

__all__ = ['register_tag', 'json_tags', 'JSONTaggedEncoder', 'JSONTaggedDecoder']

json_tags: Incomplete

def register_tag(cls):
    """
    Decorates a class to register it's json tag.
    """

class JSONTaggedEncoder(json.JSONEncoder):
    def default(self, obj): ...

class JSONTaggedDecoder(json.JSONDecoder):
    def decode(self, s): ...
    @classmethod
    def decode_obj(cls, obj): ...
