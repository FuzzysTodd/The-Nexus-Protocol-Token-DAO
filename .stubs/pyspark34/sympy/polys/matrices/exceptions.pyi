__all__ = ['DMError', 'DMBadInputError', 'DMDomainError', 'DMFormatError', 'DMRankError', 'DMShapeError', 'DMNotAField', 'DMNonInvertibleMatrixError', 'DMNonSquareMatrixError', 'DMValueError']

class DMError(Exception):
    """Base class for errors raised by DomainMatrix"""
class DMBadInputError(DMError):
    """list of lists is inconsistent with shape"""
class DMDomainError(DMError):
    """domains do not match"""
class DMNotAField(DMDomainError):
    """domain is not a field"""
class DMFormatError(DMError):
    """mixed dense/sparse not supported"""
class DMNonInvertibleMatrixError(DMError):
    """The matrix in not invertible"""
class DMRankError(DMError):
    """matrix does not have expected rank"""
class DMShapeError(DMError):
    """shapes are inconsistent"""
class DMNonSquareMatrixError(DMShapeError):
    """The matrix is not square"""
class DMValueError(DMError):
    """The value passed is invalid"""
