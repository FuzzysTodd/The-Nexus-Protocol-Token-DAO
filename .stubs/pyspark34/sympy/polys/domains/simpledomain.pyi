from sympy.polys.domains.domain import Domain as Domain
from sympy.utilities import public as public

class SimpleDomain(Domain):
    """Base class for simple domains, e.g. ZZ, QQ. """
    is_Simple: bool
    def inject(self, *gens):
        """Inject generators into this domain. """
