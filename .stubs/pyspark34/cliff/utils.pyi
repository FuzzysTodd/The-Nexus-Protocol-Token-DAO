from _typeshed import Incomplete

COST: Incomplete

def damerau_levenshtein(s1, s2, cost):
    """Calculates the Damerau-Levenshtein distance between two strings.

    The Levenshtein distance says the minimum number of single-character edits
    (i.e. insertions, deletions, swap or substitution) required to change one
    string to the other.
    The idea is to reserve a matrix to hold the Levenshtein distances between
    all prefixes of the first string and all prefixes of the second, then we
    can compute the values in the matrix in a dynamic programming fashion. To
    avoid a large space complexity, only the last three rows in the matrix is
    needed.(row2 holds the current row, row1 holds the previous row, and row0
    the row before that.)

    More details:
        https://en.wikipedia.org/wiki/Levenshtein_distance
        https://github.com/git/git/commit/8af84dadb142f7321ff0ce8690385e99da8ede2f
    """
def terminal_width(stdout): ...
