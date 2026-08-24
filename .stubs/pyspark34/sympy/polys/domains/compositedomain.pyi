from _typeshed import Incomplete
from sympy.polys.domains.domain import Domain as Domain
from sympy.polys.polyerrors import GeneratorsError as GeneratorsError
from sympy.utilities import public as public

class CompositeDomain(Domain):
    """Base class for composite domains, e.g. ZZ[x], ZZ(X). """
    is_Composite: bool
    gens: Incomplete
    ngens: Incomplete
    symbols: Incomplete
    domain: Incomplete
    def inject(self, *symbols):
        """Inject generators into this domain.  """
    def drop(self, *symbols):
        """Drop generators from this domain. """
