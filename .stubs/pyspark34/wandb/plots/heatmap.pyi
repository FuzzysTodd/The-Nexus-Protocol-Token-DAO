from _typeshed import Incomplete
from wandb import util as util
from wandb.plots.utils import deprecation_notice as deprecation_notice, encode_labels as encode_labels, test_missing as test_missing, test_types as test_types

chart_limit: Incomplete

def heatmap(x_labels, y_labels, matrix_values, show_text: bool = False):
    """
    Generates a heatmap.

    Arguments:
     matrix_values (arr): 2D dataset of shape x_labels * y_labels, containing
                        heatmap values that can be coerced into an ndarray.
     x_labels  (list): Named labels for rows (x_axis).
     y_labels  (list): Named labels for columns (y_axis).
     show_text (bool): Show text values in heatmap cells.

    Returns:
     Nothing. To see plots, go to your W&B run page then expand the 'media' tab
           under 'auto visualizations'.

    Example:
     wandb.log({'heatmap': wandb.plots.HeatMap(x_labels, y_labels,
                matrix_values)})
    """
