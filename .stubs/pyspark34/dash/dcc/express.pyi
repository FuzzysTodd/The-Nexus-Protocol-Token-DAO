from _typeshed import Incomplete

def send_file(path, filename: Incomplete | None = None, type: Incomplete | None = None):
    """
    Convert a file into the format expected by the Download component.
    :param path: path to the file to be sent
    :param filename: name of the file, if not provided the original filename is used
    :param type: type of the file (optional, passed to Blob in the javascript layer)
    :return: dict of file content (base64 encoded) and meta data used by the Download component
    """
def send_bytes(src, filename, type: Incomplete | None = None, **kwargs):
    """
    Convert data written to BytesIO into the format expected by the Download component.
    :param src: array of bytes or a writer that can write to BytesIO
    :param filename: the name of the file
    :param type: type of the file (optional, passed to Blob in the javascript layer)
    :return: dict of data frame content (base64 encoded) and meta data used by the Download component
    """
def send_string(src, filename, type: Incomplete | None = None, **kwargs):
    """
    Convert data written to StringIO into the format expected by the Download component.
    :param src: a string or a writer that can write to StringIO
    :param filename: the name of the file
    :param type: type of the file (optional, passed to Blob in the javascript layer)
    :return: dict of data frame content (NOT base64 encoded) and meta data used by the Download component
    """
def send_data_frame(writer, filename, type: Incomplete | None = None, **kwargs):
    '''
    Convert data frame into the format expected by the Download component.
    :param writer: a data frame writer
    :param filename: the name of the file
    :param type: type of the file (optional, passed to Blob in the javascript layer)
    :return: dict of data frame content (base64 encoded) and meta data used by the Download component

    Examples
    --------

    >>> df = pd.DataFrame({\'a\': [1, 2, 3, 4], \'b\': [2, 1, 5, 6], \'c\': [\'x\', \'x\', \'y\', \'y\']})
    ...
    >>> send_data_frame(df.to_csv, "mydf.csv")  # download as csv
    >>> send_data_frame(df.to_json, "mydf.json")  # download as json
    >>> send_data_frame(df.to_excel, "mydf.xls", index=False) # download as excel
    >>> send_data_frame(df.to_pickle, "mydf.pkl") # download as pickle

    '''
