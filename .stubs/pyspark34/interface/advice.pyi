from _typeshed import Incomplete

__all__ = ['determineMetaclass', 'getFrameInfo', 'isClassAdvisor', 'minimalBases']

def getFrameInfo(frame):
    '''Return (kind,module,locals,globals) for a frame

    \'kind\' is one of "exec", "module", "class", "function call", or "unknown".
    '''
def isClassAdvisor(ob):
    """True if 'ob' is a class advisor function"""
def determineMetaclass(bases, explicit_mc: Incomplete | None = None):
    """Determine metaclass from 1+ bases and optional explicit __metaclass__"""
def minimalBases(classes):
    """Reduce a list of base classes to its ordered minimum equivalent"""
