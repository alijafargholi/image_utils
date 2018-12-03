"""
Image formats that could be used for image conversions

Example:

    >>> from image_utils.image import Read
    >>> from image_utils.pixel_type import PixelType
    >>> # open an image
    >>> A = Read("A.exr")
    >>> # Make a copy of A, but converting to float pixels
    >>> C = A.copy(PixelType.bit8)
"""
__all__ = ['PixelType']

import OpenImageIO as OIIO


class PixelType:
    def __init__(self):
        pass

    @property
    def float(self):
        """Float image format

        :rtype: OpenImageIO.BASETYPE
        """
        return OIIO.FLOAT

    @property
    def half(self):
        """Half image format

        :rtype: OpenImageIO.BASETYPE
        """
        return OIIO.HALF

    @property
    def bit8(self):
        """8 bit image format

        :rtype: OpenImageIO.BASETYPE
        """
        return OIIO.UINT8


if __name__ == '__main__':
    print(__doc__)
