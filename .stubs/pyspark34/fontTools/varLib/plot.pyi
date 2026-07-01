from _typeshed import Incomplete
from fontTools.designspaceLib import DesignSpaceDocument as DesignSpaceDocument
from fontTools.varLib.models import VariationModel as VariationModel, supportScalar as supportScalar
from mpl_toolkits.mplot3d import axes3d as axes3d

log: Incomplete

def stops(support, count: int = 10): ...
def plotLocations(locations, fig, names: Incomplete | None = None, **kwargs) -> None: ...
def plotDocument(doc, fig, **kwargs) -> None: ...
def plotModelFromMasters(model, masterValues, fig, **kwargs) -> None:
    """Plot a variation model and set of master values corresponding
    to the locations to the model into a pyplot figure.  Variation
    model must have axisOrder of size 1 or 2."""
def main(args: Incomplete | None = None) -> None: ...
