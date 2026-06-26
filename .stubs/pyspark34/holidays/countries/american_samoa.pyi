from _typeshed import Incomplete
from holidays.countries.united_states import US as US

class HolidaysAS(US):
    country: str
    subdivisions: Incomplete

class AS(HolidaysAS): ...
class ASM(HolidaysAS): ...
class AmericanSamoa(HolidaysAS): ...
