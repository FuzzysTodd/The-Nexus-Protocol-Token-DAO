class PerfectSeparationError(Exception):
    """
    Error due to perfect prediction in discrete models
    """
class MissingDataError(Exception):
    """
    Error raised if variables contain missing values when forbidden
    """
class X13NotFoundError(Exception):
    """
    Error locating the X13 binary
    """
class X13Error(Exception):
    """
    Error when running modes using X13
    """
class ParseError(Exception):
    """
    Error when parsing a docstring.
    """
class X13Warning(Warning):
    """
    Unexpected conditions when using X13
    """
class IOWarning(RuntimeWarning):
    """
    Resource not deleted
    """
class ModuleUnavailableWarning(Warning):
    """
    Non-fatal import error
    """

module_unavailable_doc: str

class ModelWarning(UserWarning):
    """
    Base internal Warning class to simplify end-user filtering
    """
class ConvergenceWarning(ModelWarning):
    """
    Nonlinear optimizer failed to converge to a unique solution
    """

convergence_doc: str

class CacheWriteWarning(ModelWarning):
    """
    Attempting to write to a read-only cached value
    """
class IterationLimitWarning(ModelWarning):
    """
    Iteration limit reached without convergence
    """

iteration_limit_doc: str

class InvalidTestWarning(ModelWarning):
    """
    Test not applicable to model
    """
class NotImplementedWarning(ModelWarning):
    """
    Non-fatal function non-implementation
    """
class OutputWarning(ModelWarning):
    """
    Function output contains atypical values
    """
class DomainWarning(ModelWarning):
    """
    Variables are not compliant with required domain constraints
    """
class ValueWarning(ModelWarning):
    """
    Non-fatal out-of-range value given
    """
class EstimationWarning(ModelWarning):
    """
    Unexpected condition encountered during estimation
    """
class SingularMatrixWarning(ModelWarning):
    """
    Non-fatal matrix inversion affects output results
    """
class HypothesisTestWarning(ModelWarning):
    """
    Issue occurred when performing hypothesis test
    """
class InterpolationWarning(ModelWarning):
    """
    Table granularity and limits restrict interpolation
    """
class PrecisionWarning(ModelWarning):
    """
    Numerical implementation affects precision
    """
class SpecificationWarning(ModelWarning):
    """
    Non-fatal model specification issue
    """
class HessianInversionWarning(ModelWarning):
    """
    Hessian noninvertible and standard errors unavailable
    """
class CollinearityWarning(ModelWarning):
    """
    Variables are highly collinear
    """
class PerfectSeparationWarning(ModelWarning):
    """
    Perfect separation or prediction
    """
class InfeasibleTestError(RuntimeError):
    """
    Test statistic cannot be computed
    """

recarray_exception: str
