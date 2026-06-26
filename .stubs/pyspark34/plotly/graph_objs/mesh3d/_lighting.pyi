from _typeshed import Incomplete
from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class Lighting(_BaseTraceHierarchyType):
    @property
    def ambient(self):
        """
        Ambient light increases overall color visibility but can wash
        out the image.

        The 'ambient' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
    @ambient.setter
    def ambient(self, val) -> None: ...
    @property
    def diffuse(self):
        """
        Represents the extent that incident rays are reflected in a
        range of angles.

        The 'diffuse' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
    @diffuse.setter
    def diffuse(self, val) -> None: ...
    @property
    def facenormalsepsilon(self):
        """
        Epsilon for face normals calculation avoids math issues arising
        from degenerate geometry.

        The 'facenormalsepsilon' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
    @facenormalsepsilon.setter
    def facenormalsepsilon(self, val) -> None: ...
    @property
    def fresnel(self):
        """
        Represents the reflectance as a dependency of the viewing
        angle; e.g. paper is reflective when viewing it from the edge
        of the paper (almost 90 degrees), causing shine.

        The 'fresnel' property is a number and may be specified as:
          - An int or float in the interval [0, 5]

        Returns
        -------
        int|float
        """
    @fresnel.setter
    def fresnel(self, val) -> None: ...
    @property
    def roughness(self):
        """
        Alters specular reflection; the rougher the surface, the wider
        and less contrasty the shine.

        The 'roughness' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
    @roughness.setter
    def roughness(self, val) -> None: ...
    @property
    def specular(self):
        """
        Represents the level that incident rays are reflected in a
        single direction, causing shine.

        The 'specular' property is a number and may be specified as:
          - An int or float in the interval [0, 2]

        Returns
        -------
        int|float
        """
    @specular.setter
    def specular(self, val) -> None: ...
    @property
    def vertexnormalsepsilon(self):
        """
        Epsilon for vertex normals calculation avoids math issues
        arising from degenerate geometry.

        The 'vertexnormalsepsilon' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
    @vertexnormalsepsilon.setter
    def vertexnormalsepsilon(self, val) -> None: ...
    def __init__(self, arg: Incomplete | None = None, ambient: Incomplete | None = None, diffuse: Incomplete | None = None, facenormalsepsilon: Incomplete | None = None, fresnel: Incomplete | None = None, roughness: Incomplete | None = None, specular: Incomplete | None = None, vertexnormalsepsilon: Incomplete | None = None, **kwargs) -> None:
        """
        Construct a new Lighting object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.mesh3d.Lighting`
        ambient
            Ambient light increases overall color visibility but
            can wash out the image.
        diffuse
            Represents the extent that incident rays are reflected
            in a range of angles.
        facenormalsepsilon
            Epsilon for face normals calculation avoids math issues
            arising from degenerate geometry.
        fresnel
            Represents the reflectance as a dependency of the
            viewing angle; e.g. paper is reflective when viewing it
            from the edge of the paper (almost 90 degrees), causing
            shine.
        roughness
            Alters specular reflection; the rougher the surface,
            the wider and less contrasty the shine.
        specular
            Represents the level that incident rays are reflected
            in a single direction, causing shine.
        vertexnormalsepsilon
            Epsilon for vertex normals calculation avoids math
            issues arising from degenerate geometry.

        Returns
        -------
        Lighting
        """
