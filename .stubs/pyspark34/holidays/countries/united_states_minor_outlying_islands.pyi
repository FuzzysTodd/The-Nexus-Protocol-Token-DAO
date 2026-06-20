from _typeshed import Incomplete
from holidays.countries.united_states import US as US

class HolidaysUM(US):
    country: str
    subdivisions: Incomplete

class UM(HolidaysUM): ...
class UMI(HolidaysUM): ...
class UnitedStatesMinorOutlyingIslands(HolidaysUM): ...
