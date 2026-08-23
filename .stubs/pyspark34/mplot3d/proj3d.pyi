from _typeshed import Incomplete

def world_transformation(xmin, xmax, ymin, ymax, zmin, zmax, pb_aspect: Incomplete | None = None):
    """
    Produce a matrix that scales homogeneous coords in the specified ranges
    to [0, 1], or [0, pb_aspect[i]] if the plotbox aspect ratio is specified.
    """
def rotation_about_vector(v, angle):
    """
    Produce a rotation matrix for an angle in radians about a vector.
    """
def view_transformation(E, R, V, roll):
    """
    Return the view transformation matrix.

    Parameters
    ----------
    E : 3-element numpy array
        The coordinates of the eye/camera.
    R : 3-element numpy array
        The coordinates of the center of the view box.
    V : 3-element numpy array
        Unit vector in the direction of the vertical axis.
    roll : float
        The roll angle in radians.
    """
def persp_transformation(zfront, zback, focal_length): ...
def ortho_transformation(zfront, zback): ...
def inv_transform(xs, ys, zs, M):
    """
    Transform the points by the inverse of the projection matrix *M*.
    """
def proj_transform(xs, ys, zs, M):
    """
    Transform the points by the projection matrix *M*.
    """
transform = proj_transform

def proj_transform_clip(xs, ys, zs, M):
    """
    Transform the points by the projection matrix
    and return the clipping result
    returns txs, tys, tzs, tis
    """
def proj_points(points, M): ...
def proj_trans_points(points, M): ...
def rot_x(V, alpha): ...
