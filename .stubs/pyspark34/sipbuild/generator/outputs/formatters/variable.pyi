from .scoped import EmbeddedScopeFormatter as EmbeddedScopeFormatter

class VariableFormatter(EmbeddedScopeFormatter):
    """ This creates various string representations of a variable. """
    def as_rest_ref(self):
        """ Return the fully qualified Python name as a reST reference. """
