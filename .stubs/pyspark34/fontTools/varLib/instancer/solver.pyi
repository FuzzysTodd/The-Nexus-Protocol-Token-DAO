__all__ = ['rebaseTent']

def rebaseTent(tent, axisLimit):
    '''Given a tuple (lower,peak,upper) "tent" and new axis limits
    (axisMin,axisDefault,axisMax), solves how to represent the tent
    under the new axis configuration.  All values are in normalized
    -1,0,+1 coordinate system. Tent values can be outside this range.

    Return value is a list of tuples. Each tuple is of the form
    (scalar,tent), where scalar is a multipler to multiply any
    delta-sets by, and tent is a new tent for that output delta-set.
    If tent value is None, that is a special deltaset that should
    be always-enabled (called "gain").'''
