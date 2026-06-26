from _typeshed import Incomplete
from pyasn1.type import univ
from pyasn1_modules import rfc5280 as rfc5280

MAX: Incomplete
AttributeType = rfc5280.AttributeType
AttributeValue = rfc5280.AttributeValue
id_ct_anyContentType: Incomplete

class AttrConstraint(univ.Sequence): ...
class AttrConstraintList(univ.SequenceOf): ...
class ContentTypeGeneration(univ.Enumerated): ...
class ContentTypeConstraint(univ.Sequence): ...

id_pe_cmsContentConstraints: Incomplete

class CMSContentConstraints(univ.SequenceOf): ...
