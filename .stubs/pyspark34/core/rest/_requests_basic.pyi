import collections.abc as collections
from ..pipeline.transport._requests_basic import StreamDownloadGenerator as StreamDownloadGenerator
from ._http_response_impl import HttpResponseImpl as HttpResponseImpl, _HttpResponseBackcompatMixinBase, _HttpResponseBaseImpl
from requests.structures import CaseInsensitiveDict

class _ItemsView(collections.ItemsView):
    def __contains__(self, item) -> bool: ...

class _CaseInsensitiveDict(CaseInsensitiveDict):
    """Overriding default requests dict so we can unify
    to not raise if users pass in incorrect items to contains.
    Instead, we return False
    """
    def items(self):
        """Return a new view of the dictionary's items.

        :rtype: ~collections.abc.ItemsView[str, str]
        :returns: a view object that displays a list of (key, value) tuple pairs
        """

class _RestRequestsTransportResponseBaseMixin(_HttpResponseBackcompatMixinBase):
    """Backcompat mixin for the sync and async requests responses

    Overriding the default mixin behavior here because we need to synchronously
    read the response's content for the async requests responses
    """

class _RestRequestsTransportResponseBase(_HttpResponseBaseImpl, _RestRequestsTransportResponseBaseMixin):
    def __init__(self, **kwargs) -> None: ...

class RestRequestsTransportResponse(HttpResponseImpl, _RestRequestsTransportResponseBase):
    def __init__(self, **kwargs) -> None: ...
