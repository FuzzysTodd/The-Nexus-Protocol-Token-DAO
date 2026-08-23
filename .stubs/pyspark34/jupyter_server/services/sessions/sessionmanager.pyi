from _typeshed import Incomplete
from dataclasses import dataclass
from jupyter_server.traittypes import InstanceFromClasses as InstanceFromClasses
from traitlets.config.configurable import LoggingConfigurable
from typing import Any, Dict

KernelName: Incomplete
ModelName: Incomplete

class KernelSessionRecordConflict(Exception):
    """Exception class to use when two KernelSessionRecords cannot
    merge because of conflicting data.
    """

@dataclass
class KernelSessionRecord:
    """A record object for tracking a Jupyter Server Kernel Session.

    Two records that share a session_id must also share a kernel_id, while
    kernels can have multiple session (and thereby) session_ids
    associated with them.
    """
    session_id: str | None = ...
    kernel_id: str | None = ...
    def __eq__(self, other: object) -> bool:
        """Whether a record equals another."""
    def update(self, other: KernelSessionRecord) -> None:
        """Updates in-place a kernel from other (only accepts positive updates"""
    def __init__(self, session_id, kernel_id) -> None: ...

class KernelSessionRecordList:
    """An object for storing and managing a list of KernelSessionRecords.

    When adding a record to the list, the KernelSessionRecordList
    first checks if the record already exists in the list. If it does,
    the record will be updated with the new information; otherwise,
    it will be appended.
    """
    def __init__(self, *records: KernelSessionRecord) -> None:
        """Initialize a record list."""
    def __contains__(self, record: KernelSessionRecord | str) -> bool:
        """Search for records by kernel_id and session_id"""
    def __len__(self) -> int:
        """The length of the record list."""
    def get(self, record: KernelSessionRecord | str) -> KernelSessionRecord:
        """Return a full KernelSessionRecord from a session_id, kernel_id, or
        incomplete KernelSessionRecord.
        """
    def update(self, record: KernelSessionRecord) -> None:
        """Update a record in-place or append it if not in the list."""
    def remove(self, record: KernelSessionRecord) -> None:
        """Remove a record if its found in the list. If it's not found,
        do nothing.
        """

class SessionManager(LoggingConfigurable):
    """A session manager."""
    database_filepath: Incomplete
    kernel_manager: Incomplete
    contents_manager: Incomplete
    def __init__(self, *args, **kwargs) -> None:
        """Initialize a record list."""
    @property
    def cursor(self):
        """Start a cursor and create a database called 'session'"""
    @property
    def connection(self):
        """Start a database connection"""
    def close(self) -> None:
        """Close the sqlite connection"""
    def __del__(self) -> None:
        """Close connection once SessionManager closes"""
    async def session_exists(self, path):
        """Check to see if the session of a given name exists"""
    def new_session_id(self) -> str:
        """Create a uuid for a new session"""
    async def create_session(self, path: str | None = None, name: ModelName | None = None, type: str | None = None, kernel_name: KernelName | None = None, kernel_id: str | None = None) -> Dict[str, Any]:
        """Creates a session and returns its model

        Parameters
        ----------
        name: ModelName(str)
            Usually the model name, like the filename associated with current
            kernel.
        """
    def get_kernel_env(self, path: str | None, name: ModelName | None = None) -> Dict[str, str]:
        """Return the environment variables that need to be set in the kernel

        Parameters
        ----------
        path : str
            the url path for the given session.
        name: ModelName(str), optional
            Here the name is likely to be the name of the associated file
            with the current kernel at startup time.
        """
    async def start_kernel_for_session(self, session_id: str, path: str | None, name: ModelName | None, type: str | None, kernel_name: KernelName | None) -> str:
        """Start a new kernel for a given session.

        Parameters
        ----------
        session_id : str
            uuid for the session; this method must be given a session_id
        path : str
            the path for the given session - seem to be a session id sometime.
        name : str
            Usually the model name, like the filename associated with current
            kernel.
        type : str
            the type of the session
        kernel_name : str
            the name of the kernel specification to use.  The default kernel name will be used if not provided.
        """
    async def save_session(self, session_id, path: Incomplete | None = None, name: Incomplete | None = None, type: Incomplete | None = None, kernel_id: Incomplete | None = None):
        """Saves the items for the session with the given session_id

        Given a session_id (and any other of the arguments), this method
        creates a row in the sqlite session database that holds the information
        for a session.

        Parameters
        ----------
        session_id : str
            uuid for the session; this method must be given a session_id
        path : str
            the path for the given session
        name : str
            the name of the session
        type : str
            the type of the session
        kernel_id : str
            a uuid for the kernel associated with this session

        Returns
        -------
        model : dict
            a dictionary of the session model
        """
    async def get_session(self, **kwargs):
        """Returns the model for a particular session.

        Takes a keyword argument and searches for the value in the session
        database, then returns the rest of the session's info.

        Parameters
        ----------
        **kwargs : dict
            must be given one of the keywords and values from the session database
            (i.e. session_id, path, name, type, kernel_id)

        Returns
        -------
        model : dict
            returns a dictionary that includes all the information from the
            session described by the kwarg.
        """
    async def update_session(self, session_id, **kwargs) -> None:
        """Updates the values in the session database.

        Changes the values of the session with the given session_id
        with the values from the keyword arguments.

        Parameters
        ----------
        session_id : str
            a uuid that identifies a session in the sqlite3 database
        **kwargs : str
            the key must correspond to a column title in session database,
            and the value replaces the current value in the session
            with session_id.
        """
    async def kernel_culled(self, kernel_id: str) -> bool:
        """Checks if the kernel is still considered alive and returns true if its not found."""
    async def row_to_model(self, row, tolerate_culled: bool = False):
        """Takes sqlite database session row and turns it into a dictionary"""
    async def list_sessions(self):
        """Returns a list of dictionaries containing all the information from
        the session database"""
    async def delete_session(self, session_id) -> None:
        """Deletes the row in the session database with given session_id"""
