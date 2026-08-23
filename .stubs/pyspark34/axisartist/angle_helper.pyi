from _typeshed import Incomplete
from mpl_toolkits.axisartist.grid_finder import ExtremeFinderSimple

def select_step_degree(dv): ...
def select_step_hour(dv): ...
def select_step_sub(dv): ...
def select_step(v1, v2, nv, hour: bool = False, include_last: bool = True, threshold_factor: float = 3600.0): ...
def select_step24(v1, v2, nv, include_last: bool = True, threshold_factor: int = 3600): ...
def select_step360(v1, v2, nv, include_last: bool = True, threshold_factor: int = 3600): ...

class LocatorBase:
    nbins: Incomplete
    def __init__(self, nbins, include_last: bool = True) -> None: ...
    def set_params(self, nbins: Incomplete | None = None) -> None: ...

class LocatorHMS(LocatorBase):
    def __call__(self, v1, v2): ...

class LocatorHM(LocatorBase):
    def __call__(self, v1, v2): ...

class LocatorH(LocatorBase):
    def __call__(self, v1, v2): ...

class LocatorDMS(LocatorBase):
    def __call__(self, v1, v2): ...

class LocatorDM(LocatorBase):
    def __call__(self, v1, v2): ...

class LocatorD(LocatorBase):
    def __call__(self, v1, v2): ...

class FormatterDMS:
    deg_mark: str
    min_mark: str
    sec_mark: str
    fmt_d: Incomplete
    fmt_ds: Incomplete
    fmt_d_m: Incomplete
    fmt_d_ms: Incomplete
    fmt_d_m_partial: Incomplete
    fmt_s_partial: Incomplete
    fmt_ss_partial: Incomplete
    def __call__(self, direction, factor, values): ...

class FormatterHMS(FormatterDMS):
    deg_mark: str
    min_mark: str
    sec_mark: str
    fmt_d: Incomplete
    fmt_ds: Incomplete
    fmt_d_m: Incomplete
    fmt_d_ms: Incomplete
    fmt_d_m_partial: Incomplete
    fmt_s_partial: Incomplete
    fmt_ss_partial: Incomplete
    def __call__(self, direction, factor, values): ...

class ExtremeFinderCycle(ExtremeFinderSimple):
    lon_minmax: Incomplete
    lat_minmax: Incomplete
    def __init__(self, nx, ny, lon_cycle: float = 360.0, lat_cycle: Incomplete | None = None, lon_minmax: Incomplete | None = None, lat_minmax=(-90, 90)) -> None:
        '''
        This subclass handles the case where one or both coordinates should be
        taken modulo 360, or be restricted to not exceed a specific range.

        Parameters
        ----------
        nx, ny : int
            The number of samples in each direction.

        lon_cycle, lat_cycle : 360 or None
            If not None, values in the corresponding direction are taken modulo
            *lon_cycle* or *lat_cycle*; in theory this can be any number but
            the implementation actually assumes that it is 360 (if not None);
            other values give nonsensical results.

            This is done by "unwrapping" the transformed grid coordinates so
            that jumps are less than a half-cycle; then normalizing the span to
            no more than a full cycle.

            For example, if values are in the union of the [0, 2] and
            [358, 360] intervals (typically, angles measured modulo 360), the
            values in the second interval are normalized to [-2, 0] instead so
            that the values now cover [-2, 2].  If values are in a range of
            [5, 1000], this gets normalized to [5, 365].

        lon_minmax, lat_minmax : (float, float) or None
            If not None, the computed bounding box is clipped to the given
            range in the corresponding direction.
        '''
    def __call__(self, transform_xy, x1, y1, x2, y2): ...
