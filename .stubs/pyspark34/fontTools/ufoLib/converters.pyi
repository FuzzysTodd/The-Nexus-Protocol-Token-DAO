def convertUFO1OrUFO2KerningToUFO3Kerning(kerning, groups, glyphSet=()): ...
def findKnownKerningGroups(groups):
    '''
    This will find kerning groups with known prefixes.
    In some cases not all kerning groups will be referenced
    by the kerning pairs. The algorithm for locating groups
    in convertUFO1OrUFO2KerningToUFO3Kerning will miss these
    unreferenced groups. By scanning for known prefixes
    this function will catch all of the prefixed groups.

    These are the prefixes and sides that are handled:
    @MMK_L_ - side 1
    @MMK_R_ - side 2

    >>> testGroups = {
    ...     "@MMK_L_1" : None,
    ...     "@MMK_L_2" : None,
    ...     "@MMK_L_3" : None,
    ...     "@MMK_R_1" : None,
    ...     "@MMK_R_2" : None,
    ...     "@MMK_R_3" : None,
    ...     "@MMK_l_1" : None,
    ...     "@MMK_r_1" : None,
    ...     "@MMK_X_1" : None,
    ...     "foo" : None,
    ... }
    >>> first, second = findKnownKerningGroups(testGroups)
    >>> sorted(first) == [\'@MMK_L_1\', \'@MMK_L_2\', \'@MMK_L_3\']
    True
    >>> sorted(second) == [\'@MMK_R_1\', \'@MMK_R_2\', \'@MMK_R_3\']
    True
    '''
def makeUniqueGroupName(name, groupNames, counter: int = 0): ...
def test() -> None:
    '''
    No known prefixes.

    >>> testKerning = {
    ...     "A" : {
    ...         "A" : 1,
    ...         "B" : 2,
    ...         "CGroup" : 3,
    ...         "DGroup" : 4
    ...     },
    ...     "BGroup" : {
    ...         "A" : 5,
    ...         "B" : 6,
    ...         "CGroup" : 7,
    ...         "DGroup" : 8
    ...     },
    ...     "CGroup" : {
    ...         "A" : 9,
    ...         "B" : 10,
    ...         "CGroup" : 11,
    ...         "DGroup" : 12
    ...     },
    ... }
    >>> testGroups = {
    ...     "BGroup" : ["B"],
    ...     "CGroup" : ["C"],
    ...     "DGroup" : ["D"],
    ... }
    >>> kerning, groups, maps = convertUFO1OrUFO2KerningToUFO3Kerning(
    ...     testKerning, testGroups, [])
    >>> expected = {
    ...     "A" : {
    ...         "A": 1,
    ...         "B": 2,
    ...         "public.kern2.CGroup": 3,
    ...         "public.kern2.DGroup": 4
    ...     },
    ...     "public.kern1.BGroup": {
    ...         "A": 5,
    ...         "B": 6,
    ...         "public.kern2.CGroup": 7,
    ...         "public.kern2.DGroup": 8
    ...     },
    ...     "public.kern1.CGroup": {
    ...         "A": 9,
    ...         "B": 10,
    ...         "public.kern2.CGroup": 11,
    ...         "public.kern2.DGroup": 12
    ...     }
    ... }
    >>> kerning == expected
    True
    >>> expected = {
    ...     "BGroup": ["B"],
    ...     "CGroup": ["C"],
    ...     "DGroup": ["D"],
    ...     "public.kern1.BGroup": ["B"],
    ...     "public.kern1.CGroup": ["C"],
    ...     "public.kern2.CGroup": ["C"],
    ...     "public.kern2.DGroup": ["D"],
    ... }
    >>> groups == expected
    True

    Known prefixes.

    >>> testKerning = {
    ...     "A" : {
    ...         "A" : 1,
    ...         "B" : 2,
    ...         "@MMK_R_CGroup" : 3,
    ...         "@MMK_R_DGroup" : 4
    ...     },
    ...     "@MMK_L_BGroup" : {
    ...         "A" : 5,
    ...         "B" : 6,
    ...         "@MMK_R_CGroup" : 7,
    ...         "@MMK_R_DGroup" : 8
    ...     },
    ...     "@MMK_L_CGroup" : {
    ...         "A" : 9,
    ...         "B" : 10,
    ...         "@MMK_R_CGroup" : 11,
    ...         "@MMK_R_DGroup" : 12
    ...     },
    ... }
    >>> testGroups = {
    ...     "@MMK_L_BGroup" : ["B"],
    ...     "@MMK_L_CGroup" : ["C"],
    ...     "@MMK_L_XGroup" : ["X"],
    ...     "@MMK_R_CGroup" : ["C"],
    ...     "@MMK_R_DGroup" : ["D"],
    ...     "@MMK_R_XGroup" : ["X"],
    ... }
    >>> kerning, groups, maps = convertUFO1OrUFO2KerningToUFO3Kerning(
    ...     testKerning, testGroups, [])
    >>> expected = {
    ...     "A" : {
    ...         "A": 1,
    ...         "B": 2,
    ...         "public.kern2.CGroup": 3,
    ...         "public.kern2.DGroup": 4
    ...     },
    ...     "public.kern1.BGroup": {
    ...         "A": 5,
    ...         "B": 6,
    ...         "public.kern2.CGroup": 7,
    ...         "public.kern2.DGroup": 8
    ...     },
    ...     "public.kern1.CGroup": {
    ...         "A": 9,
    ...         "B": 10,
    ...         "public.kern2.CGroup": 11,
    ...         "public.kern2.DGroup": 12
    ...     }
    ... }
    >>> kerning == expected
    True
    >>> expected = {
    ...     "@MMK_L_BGroup": ["B"],
    ...     "@MMK_L_CGroup": ["C"],
    ...     "@MMK_L_XGroup": ["X"],
    ...     "@MMK_R_CGroup": ["C"],
    ...     "@MMK_R_DGroup": ["D"],
    ...     "@MMK_R_XGroup": ["X"],
    ...     "public.kern1.BGroup": ["B"],
    ...     "public.kern1.CGroup": ["C"],
    ...     "public.kern1.XGroup": ["X"],
    ...     "public.kern2.CGroup": ["C"],
    ...     "public.kern2.DGroup": ["D"],
    ...     "public.kern2.XGroup": ["X"],
    ... }
    >>> groups == expected
    True

    >>> from .validators import kerningValidator
    >>> kerningValidator(kerning)
    (True, None)

    Mixture of known prefixes and groups without prefixes.

    >>> testKerning = {
    ...     "A" : {
    ...         "A" : 1,
    ...         "B" : 2,
    ...         "@MMK_R_CGroup" : 3,
    ...         "DGroup" : 4
    ...     },
    ...     "BGroup" : {
    ...         "A" : 5,
    ...         "B" : 6,
    ...         "@MMK_R_CGroup" : 7,
    ...         "DGroup" : 8
    ...     },
    ...     "@MMK_L_CGroup" : {
    ...         "A" : 9,
    ...         "B" : 10,
    ...         "@MMK_R_CGroup" : 11,
    ...         "DGroup" : 12
    ...     },
    ... }
    >>> testGroups = {
    ...     "BGroup" : ["B"],
    ...     "@MMK_L_CGroup" : ["C"],
    ...     "@MMK_R_CGroup" : ["C"],
    ...     "DGroup" : ["D"],
    ... }
    >>> kerning, groups, maps = convertUFO1OrUFO2KerningToUFO3Kerning(
    ...     testKerning, testGroups, [])
    >>> expected = {
    ...     "A" : {
    ...         "A": 1,
    ...         "B": 2,
    ...         "public.kern2.CGroup": 3,
    ...         "public.kern2.DGroup": 4
    ...     },
    ...     "public.kern1.BGroup": {
    ...         "A": 5,
    ...         "B": 6,
    ...         "public.kern2.CGroup": 7,
    ...         "public.kern2.DGroup": 8
    ...     },
    ...     "public.kern1.CGroup": {
    ...         "A": 9,
    ...         "B": 10,
    ...         "public.kern2.CGroup": 11,
    ...         "public.kern2.DGroup": 12
    ...     }
    ... }
    >>> kerning == expected
    True
    >>> expected = {
    ...     "BGroup": ["B"],
    ...     "@MMK_L_CGroup": ["C"],
    ...     "@MMK_R_CGroup": ["C"],
    ...     "DGroup": ["D"],
    ...     "public.kern1.BGroup": ["B"],
    ...     "public.kern1.CGroup": ["C"],
    ...     "public.kern2.CGroup": ["C"],
    ...     "public.kern2.DGroup": ["D"],
    ... }
    >>> groups == expected
    True
    '''
