from _typeshed import Incomplete
from plotly.express._chart_types import choropleth_mapbox as choropleth_mapbox, scatter_mapbox as scatter_mapbox
from plotly.express._core import build_dataframe as build_dataframe
from plotly.express._doc import make_docstring as make_docstring

def create_hexbin_mapbox(data_frame: Incomplete | None = None, lat: Incomplete | None = None, lon: Incomplete | None = None, color: Incomplete | None = None, nx_hexagon: int = 5, agg_func: Incomplete | None = None, animation_frame: Incomplete | None = None, color_discrete_sequence: Incomplete | None = None, color_discrete_map={}, labels={}, color_continuous_scale: Incomplete | None = None, range_color: Incomplete | None = None, color_continuous_midpoint: Incomplete | None = None, opacity: Incomplete | None = None, zoom: Incomplete | None = None, center: Incomplete | None = None, mapbox_style: Incomplete | None = None, title: Incomplete | None = None, template: Incomplete | None = None, width: Incomplete | None = None, height: Incomplete | None = None, min_count: Incomplete | None = None, show_original_data: bool = False, original_data_marker: Incomplete | None = None):
    """
    Returns a figure aggregating scattered points into connected hexagons
    """
