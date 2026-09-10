from _typeshed import Incomplete

borders: Incomplete
contains: Incomplete
city: Incomplete
country: Incomplete
circle_of_lat: Incomplete
circle_of_long: Incomplete
continent: Incomplete
region: Incomplete
ocean: Incomplete
sea: Incomplete
items: Incomplete
item_metadata: Incomplete
rels: Incomplete
not_unary: Incomplete

class Concept:
    """
    A Concept class, loosely based on SKOS
    (https://www.w3.org/TR/swbp-skos-core-guide/).
    """
    prefLabel: Incomplete
    arity: Incomplete
    altLabels: Incomplete
    closures: Incomplete
    extension: Incomplete
    def __init__(self, prefLabel, arity, altLabels=[], closures=[], extension=...) -> None:
        """
        :param prefLabel: the preferred label for the concept
        :type prefLabel: str
        :param arity: the arity of the concept
        :type arity: int
        :param altLabels: other (related) labels
        :type altLabels: list
        :param closures: closure properties of the extension
            (list items can be ``symmetric``, ``reflexive``, ``transitive``)
        :type closures: list
        :param extension: the extensional value of the concept
        :type extension: set
        """
    def augment(self, data):
        """
        Add more data to the ``Concept``'s extension set.

        :param data: a new semantic value
        :type data: string or pair of strings
        :rtype: set

        """
    def close(self) -> None:
        """
        Close a binary relation in the ``Concept``'s extension set.

        :return: a new extension for the ``Concept`` in which the
                 relation is closed under a given property
        """

def clause2concepts(filename, rel_name, schema, closures=[]):
    """
    Convert a file of Prolog clauses into a list of ``Concept`` objects.

    :param filename: filename containing the relations
    :type filename: str
    :param rel_name: name of the relation
    :type rel_name: str
    :param schema: the schema used in a set of relational tuples
    :type schema: list
    :param closures: closure properties for the extension of the concept
    :type closures: list
    :return: a list of ``Concept`` objects
    :rtype: list
    """
def cities2table(filename, rel_name, dbname, verbose: bool = False, setup: bool = False) -> None:
    """
    Convert a file of Prolog clauses into a database table.

    This is not generic, since it doesn't allow arbitrary
    schemas to be set as a parameter.

    Intended usage::

        cities2table('cities.pl', 'city', 'city.db', verbose=True, setup=True)

    :param filename: filename containing the relations
    :type filename: str
    :param rel_name: name of the relation
    :type rel_name: str
    :param dbname: filename of persistent store
    :type schema: str
    """
def sql_query(dbname, query):
    """
    Execute an SQL query over a database.
    :param dbname: filename of persistent store
    :type schema: str
    :param query: SQL query
    :type rel_name: str
    """
def unary_concept(label, subj, records):
    """
    Make a unary concept out of the primary key in a record.

    A record is a list of entities in some relation, such as
    ``['france', 'paris']``, where ``'france'`` is acting as the primary
    key.

    :param label: the preferred label for the concept
    :type label: string
    :param subj: position in the record of the subject of the predicate
    :type subj: int
    :param records: a list of records
    :type records: list of lists
    :return: ``Concept`` of arity 1
    :rtype: Concept
    """
def binary_concept(label, closures, subj, obj, records):
    """
    Make a binary concept out of the primary key and another field in a record.

    A record is a list of entities in some relation, such as
    ``['france', 'paris']``, where ``'france'`` is acting as the primary
    key, and ``'paris'`` stands in the ``'capital_of'`` relation to
    ``'france'``.

    More generally, given a record such as ``['a', 'b', 'c']``, where
    label is bound to ``'B'``, and ``obj`` bound to 1, the derived
    binary concept will have label ``'B_of'``, and its extension will
    be a set of pairs such as ``('a', 'b')``.


    :param label: the base part of the preferred label for the concept
    :type label: str
    :param closures: closure properties for the extension of the concept
    :type closures: list
    :param subj: position in the record of the subject of the predicate
    :type subj: int
    :param obj: position in the record of the object of the predicate
    :type obj: int
    :param records: a list of records
    :type records: list of lists
    :return: ``Concept`` of arity 2
    :rtype: Concept
    """
def process_bundle(rels):
    """
    Given a list of relation metadata bundles, make a corresponding
    dictionary of concepts, indexed by the relation name.

    :param rels: bundle of metadata needed for constructing a concept
    :type rels: list(dict)
    :return: a dictionary of concepts, indexed by the relation name.
    :rtype: dict(str): Concept
    """
def make_valuation(concepts, read: bool = False, lexicon: bool = False):
    """
    Convert a list of ``Concept`` objects into a list of (label, extension) pairs;
    optionally create a ``Valuation`` object.

    :param concepts: concepts
    :type concepts: list(Concept)
    :param read: if ``True``, ``(symbol, set)`` pairs are read into a ``Valuation``
    :type read: bool
    :rtype: list or Valuation
    """
def val_dump(rels, db) -> None:
    """
    Make a ``Valuation`` from a list of relation metadata bundles and dump to
    persistent database.

    :param rels: bundle of metadata needed for constructing a concept
    :type rels: list of dict
    :param db: name of file to which data is written.
               The suffix '.db' will be automatically appended.
    :type db: str
    """
def val_load(db):
    """
    Load a ``Valuation`` from a persistent database.

    :param db: name of file from which data is read.
               The suffix '.db' should be omitted from the name.
    :type db: str
    """
def label_indivs(valuation, lexicon: bool = False):
    """
    Assign individual constants to the individuals in the domain of a ``Valuation``.

    Given a valuation with an entry of the form ``{'rel': {'a': True}}``,
    add a new entry ``{'a': 'a'}``.

    :type valuation: Valuation
    :rtype: Valuation
    """
def make_lex(symbols):
    """
    Create lexical CFG rules for each individual symbol.

    Given a valuation with an entry of the form ``{'zloty': 'zloty'}``,
    create a lexical rule for the proper name 'Zloty'.

    :param symbols: a list of individual constants in the semantic representation
    :type symbols: sequence -- set(str)
    :rtype: list(str)
    """
def concepts(items=...):
    """
    Build a list of concepts corresponding to the relation names in ``items``.

    :param items: names of the Chat-80 relations to extract
    :type items: list(str)
    :return: the ``Concept`` objects which are extracted from the relations
    :rtype: list(Concept)
    """
def main() -> None: ...
def sql_demo() -> None:
    """
    Print out every row from the 'city.db' database.
    """
