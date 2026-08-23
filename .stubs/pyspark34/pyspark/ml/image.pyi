import numpy as np
from _typeshed import Incomplete
from pyspark.sql.types import Row, StructType
from typing import Dict, List

__all__ = ['ImageSchema']

class _ImageSchema:
    """
    Internal class for `pyspark.ml.image.ImageSchema` attribute. Meant to be private and
    not to be instantized. Use `pyspark.ml.image.ImageSchema` attribute to access the
    APIs of this class.
    """
    def __init__(self) -> None: ...
    @property
    def imageSchema(self) -> StructType:
        '''
        Returns the image schema.

        Returns
        -------
        :class:`StructType`
            with a single column of images named "image" (nullable)
            and having the same type returned by :meth:`columnSchema`.

        .. versionadded:: 2.3.0
        '''
    @property
    def ocvTypes(self) -> Dict[str, int]:
        """
        Returns the OpenCV type mapping supported.

        Returns
        -------
        dict
            a dictionary containing the OpenCV type mapping supported.

        .. versionadded:: 2.3.0
        """
    @property
    def columnSchema(self) -> StructType:
        """
        Returns the schema for the image column.

        Returns
        -------
        :class:`StructType`
            a schema for image column,
            ``struct<origin:string, height:int, width:int, nChannels:int, mode:int, data:binary>``.

        .. versionadded:: 2.4.0
        """
    @property
    def imageFields(self) -> List[str]:
        """
        Returns field names of image columns.

        Returns
        -------
        list
            a list of field names.

        .. versionadded:: 2.3.0
        """
    @property
    def undefinedImageType(self) -> str:
        """
        Returns the name of undefined image type for the invalid image.

        .. versionadded:: 2.3.0
        """
    def toNDArray(self, image: Row) -> np.ndarray:
        """
        Converts an image to an array with metadata.

        Parameters
        ----------
        image : :class:`Row`
            image: A row that contains the image to be converted. It should
            have the attributes specified in `ImageSchema.imageSchema`.

        Returns
        -------
        :class:`numpy.ndarray`
            that is an image.

        .. versionadded:: 2.3.0
        """
    def toImage(self, array: np.ndarray, origin: str = '') -> Row:
        """
        Converts an array with metadata to a two-dimensional image.

        Parameters
        ----------
        array : :class:`numpy.ndarray`
            The array to convert to image.
        origin : str
            Path to the image, optional.

        Returns
        -------
        :class:`Row`
            that is a two dimensional image.

        .. versionadded:: 2.3.0
        """

ImageSchema: Incomplete
