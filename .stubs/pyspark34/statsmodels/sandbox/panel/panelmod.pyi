from _typeshed import Incomplete
from pandas import Panel

__all__ = ['PanelModel']

class PanelData(Panel): ...

class PanelModel:
    """
    An abstract statistical model class for panel (longitudinal) datasets.

    Parameters
    ----------
    endog : array_like or str
        If a pandas object is used then endog should be the name of the
        endogenous variable as a string.
#    exog
#    panel_arr
#    time_arr
    panel_data : pandas.Panel object

    Notes
    -----
    If a pandas object is supplied it is assumed that the major_axis is time
    and that the minor_axis has the panel variable.
    """
    def __init__(self, endog: Incomplete | None = None, exog: Incomplete | None = None, panel: Incomplete | None = None, time: Incomplete | None = None, xtnames: Incomplete | None = None, equation: Incomplete | None = None, panel_data: Incomplete | None = None) -> None: ...
    endog_name: Incomplete
    panel_name: Incomplete
    time_name: Incomplete
    exog_names: Incomplete
    endog: Incomplete
    exog: Incomplete
    panel: Incomplete
    time: Incomplete
    paneluniq: Incomplete
    timeuniq: Incomplete
    def initialize(self, endog, exog, panel, time, xtnames, equation) -> None:
        """
        Initialize plain array model.

        See PanelModel
        """
    panel_data: Incomplete
    def initialize_pandas(self, panel_data, endog_name, exog_name) -> None: ...
    def fit(self, model: Incomplete | None = None, method: Incomplete | None = None, effects: str = 'oneway'):
        """
        method : LSDV, demeaned, MLE, GLS, BE, FE, optional
        model :
                between
                fixed
                random
                pooled
                [gmm]
        effects :
                oneway
                time
                twoway
        femethod : demeaned (only one implemented)
                   WLS
        remethod :
                swar -
                amemiya
                nerlove
                walhus


        Notes
        -----
        This is unfinished.  None of the method arguments work yet.
        Only oneway effects should work.
        """

class SURPanel(PanelModel): ...
class SEMPanel(PanelModel): ...
class DynamicPanel(PanelModel): ...
