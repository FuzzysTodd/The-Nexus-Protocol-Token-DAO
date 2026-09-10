from _typeshed import Incomplete
from dateutil.zoneinfo import METADATA_FN as METADATA_FN, ZONEFILENAME as ZONEFILENAME

def rebuild(filename, tag: Incomplete | None = None, format: str = 'gz', zonegroups=[], metadata: Incomplete | None = None) -> None:
    """Rebuild the internal timezone info in dateutil/zoneinfo/zoneinfo*tar*

    filename is the timezone tarball from ``ftp.iana.org/tz``.

    """
