from contourpy._contourpy import FillType as FillType, LineType as LineType, ZInterp as ZInterp

def as_fill_type(fill_type: FillType | str) -> FillType:
    """Coerce a FillType or string value to a FillType.

    Args:
        fill_type (FillType or str): Value to convert.

    Return:
        FillType: Converted value.
    """
def as_line_type(line_type: LineType | str) -> LineType:
    """Coerce a LineType or string value to a LineType.

    Args:
        line_type (LineType or str): Value to convert.

    Return:
        LineType: Converted value.
    """
def as_z_interp(z_interp: ZInterp | str) -> ZInterp:
    """Coerce a ZInterp or string value to a ZInterp.

    Args:
        z_interp (ZInterp or str): Value to convert.

    Return:
        ZInterp: Converted value.
    """
