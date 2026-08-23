from _typeshed import Incomplete
from urlparse import urlparse as urlparse

logger: Incomplete

def send_request(mex_endpoint, http_client, **kwargs): ...

class Mex:
    NS: Incomplete
    ACTION_13: str
    ACTION_2005: str
    dom: Incomplete
    def __init__(self, mex_document) -> None: ...
    def get_wstrust_username_password_endpoint(self):
        '''Returns {"address": "https://...", "action": "the soapAction value"}'''
