from _typeshed import Incomplete
from collections.abc import Generator

def pretty_source(source):
    """ Prettify the source.
    """
def split_lines(source, maxline: int = 79):
    """Split inputs according to lines.
       If a line is short enough, just yield it.
       Otherwise, fix it.
    """
def count(group, slen=...): ...
def wrap_line(line, maxline: int = 79, result=[], count=...):
    """ We have a line that is too long,
        so we're going to try to wrap it.
    """
def split_group(source, pos, maxline):
    """ Split a group into two subgroups.  The
        first will be appended to the current
        line, the second will start the new line.

        Note that the first group must always
        contain at least one item.

        The original group may be destroyed.
    """

begin_delim: Incomplete
end_delim: Incomplete

def delimiter_groups(line, begin_delim=..., end_delim=...) -> Generator[Incomplete, None, None]:
    """Split a line into alternating groups.
       The first group cannot have a line feed inserted,
       the next one can, etc.
    """

statements: Incomplete

def add_parens(line, maxline, indent, statements=..., count=...):
    """Attempt to add parentheses around the line
       in order to make it splittable.
    """

ops: Incomplete

def get_assign_groups(line, ops=...) -> Generator[Incomplete, None, None]:
    """ Split a line into groups by assignment (including
        augmented assignment)
    """
