import typing as t
from _typeshed import Incomplete
from _typeshed.wsgi import WSGIApplication as WSGIApplication
from werkzeug.datastructures import Headers as Headers
from werkzeug.sansio.response import Response as Response

ResponseValue: Incomplete
HeaderValue: Incomplete
HeadersValue: Incomplete
ResponseReturnValue: Incomplete
ResponseClass = t.TypeVar('ResponseClass', bound='Response')
AppOrBlueprintKey: Incomplete
AfterRequestCallable: Incomplete
BeforeFirstRequestCallable: Incomplete
BeforeRequestCallable: Incomplete
ShellContextProcessorCallable: Incomplete
TeardownCallable: Incomplete
TemplateContextProcessorCallable: Incomplete
TemplateFilterCallable: Incomplete
TemplateGlobalCallable: Incomplete
TemplateTestCallable: Incomplete
URLDefaultCallable: Incomplete
URLValuePreprocessorCallable: Incomplete
ErrorHandlerCallable: Incomplete
RouteCallable: Incomplete
