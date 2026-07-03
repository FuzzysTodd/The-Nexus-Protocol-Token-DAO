from _typeshed import Incomplete
from holidays.countries.united_states import US as US

class HolidaysMP(US):
    country: str
    subdivisions: Incomplete

class MP(HolidaysMP): ...
class MNP(HolidaysMP): ...
class NorthernMarianaIslands(HolidaysMP): ...
