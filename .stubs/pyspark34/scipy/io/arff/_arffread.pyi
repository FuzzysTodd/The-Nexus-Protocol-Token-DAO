from _typeshed import Incomplete

__all__ = ['MetaData', 'loadarff', 'ArffError', 'ParseArffError']

class ArffError(OSError): ...
class ParseArffError(ArffError): ...

class Attribute:
    type_name: Incomplete
    name: Incomplete
    range: Incomplete
    dtype: Incomplete
    def __init__(self, name) -> None: ...
    @classmethod
    def parse_attribute(cls, name, attr_string) -> None:
        """
        Parse the attribute line if it knows how. Returns the parsed
        attribute, or None.
        """
    def parse_data(self, data_str) -> None:
        """
        Parse a value of this type.
        """

class NominalAttribute(Attribute):
    type_name: str
    values: Incomplete
    range: Incomplete
    dtype: Incomplete
    def __init__(self, name, values) -> None: ...
    @classmethod
    def parse_attribute(cls, name, attr_string):
        """
        Parse the attribute line if it knows how. Returns the parsed
        attribute, or None.

        For nominal attributes, the attribute string would be like '{<attr_1>,
         <attr2>, <attr_3>}'.
        """
    def parse_data(self, data_str):
        """
        Parse a value of this type.
        """

class NumericAttribute(Attribute):
    type_name: str
    dtype: Incomplete
    def __init__(self, name) -> None: ...
    @classmethod
    def parse_attribute(cls, name, attr_string):
        """
        Parse the attribute line if it knows how. Returns the parsed
        attribute, or None.

        For numeric attributes, the attribute string would be like
        'numeric' or 'int' or 'real'.
        """
    def parse_data(self, data_str):
        """
        Parse a value of this type.

        Parameters
        ----------
        data_str : str
           string to convert

        Returns
        -------
        f : float
           where float can be nan

        Examples
        --------
        >>> atr = NumericAttribute('atr')
        >>> atr.parse_data('1')
        1.0
        >>> atr.parse_data('1\\n')
        1.0
        >>> atr.parse_data('?\\n')
        nan
        """

class StringAttribute(Attribute):
    type_name: str
    def __init__(self, name) -> None: ...
    @classmethod
    def parse_attribute(cls, name, attr_string):
        """
        Parse the attribute line if it knows how. Returns the parsed
        attribute, or None.

        For string attributes, the attribute string would be like
        'string'.
        """

class DateAttribute(Attribute):
    date_format: Incomplete
    datetime_unit: Incomplete
    type_name: str
    range: Incomplete
    dtype: Incomplete
    def __init__(self, name, date_format, datetime_unit) -> None: ...
    @classmethod
    def parse_attribute(cls, name, attr_string):
        """
        Parse the attribute line if it knows how. Returns the parsed
        attribute, or None.

        For date attributes, the attribute string would be like
        'date <format>'.
        """
    def parse_data(self, data_str):
        """
        Parse a value of this type.
        """

class RelationalAttribute(Attribute):
    type_name: str
    dtype: Incomplete
    attributes: Incomplete
    dialect: Incomplete
    def __init__(self, name) -> None: ...
    @classmethod
    def parse_attribute(cls, name, attr_string):
        """
        Parse the attribute line if it knows how. Returns the parsed
        attribute, or None.

        For date attributes, the attribute string would be like
        'date <format>'.
        """
    def parse_data(self, data_str): ...

class MetaData:
    """Small container to keep useful information on a ARFF dataset.

    Knows about attributes names and types.

    Examples
    --------
    ::

        data, meta = loadarff('iris.arff')
        # This will print the attributes names of the iris.arff dataset
        for i in meta:
            print(i)
        # This works too
        meta.names()
        # Getting attribute type
        types = meta.types()

    Methods
    -------
    names
    types

    Notes
    -----
    Also maintains the list of attributes in order, i.e., doing for i in
    meta, where meta is an instance of MetaData, will return the
    different attribute names in the order they were defined.
    """
    name: Incomplete
    def __init__(self, rel, attr) -> None: ...
    def __iter__(self): ...
    def __getitem__(self, key): ...
    def names(self):
        """Return the list of attribute names.

        Returns
        -------
        attrnames : list of str
            The attribute names.
        """
    def types(self):
        """Return the list of attribute types.

        Returns
        -------
        attr_types : list of str
            The attribute types.
        """

def loadarff(f):
    '''
    Read an arff file.

    The data is returned as a record array, which can be accessed much like
    a dictionary of NumPy arrays. For example, if one of the attributes is
    called \'pressure\', then its first 10 data points can be accessed from the
    ``data`` record array like so: ``data[\'pressure\'][0:10]``


    Parameters
    ----------
    f : file-like or str
       File-like object to read from, or filename to open.

    Returns
    -------
    data : record array
       The data of the arff file, accessible by attribute names.
    meta : `MetaData`
       Contains information about the arff file such as name and
       type of attributes, the relation (name of the dataset), etc.

    Raises
    ------
    ParseArffError
        This is raised if the given file is not ARFF-formatted.
    NotImplementedError
        The ARFF file has an attribute which is not supported yet.

    Notes
    -----

    This function should be able to read most arff files. Not
    implemented functionality include:

    * date type attributes
    * string type attributes

    It can read files with numeric and nominal attributes. It cannot read
    files with sparse data ({} in the file). However, this function can
    read files with missing data (? in the file), representing the data
    points as NaNs.

    Examples
    --------
    >>> from scipy.io import arff
    >>> from io import StringIO
    >>> content = """
    ... @relation foo
    ... @attribute width  numeric
    ... @attribute height numeric
    ... @attribute color  {red,green,blue,yellow,black}
    ... @data
    ... 5.0,3.25,blue
    ... 4.5,3.75,green
    ... 3.0,4.00,red
    ... """
    >>> f = StringIO(content)
    >>> data, meta = arff.loadarff(f)
    >>> data
    array([(5.0, 3.25, \'blue\'), (4.5, 3.75, \'green\'), (3.0, 4.0, \'red\')],
          dtype=[(\'width\', \'<f8\'), (\'height\', \'<f8\'), (\'color\', \'|S6\')])
    >>> meta
    Dataset: foo
    \twidth\'s type is numeric
    \theight\'s type is numeric
    \tcolor\'s type is nominal, range is (\'red\', \'green\', \'blue\', \'yellow\', \'black\')

    '''
