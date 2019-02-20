"""
============
Read Node
============

- **Read**:
- **Constant**:
- **Checker**:
"""
from __future__ import print_function
# __all__ = ['Read', 'constant', 'checker']

import os

import OpenImageIO as OIIO
from OpenImageIO import ImageBuf
from OpenImageIO import ImageSpec
from OpenImageIO import ImageBufAlgo

from image_utils.pixel_type import PixelType
from image_utils.nodes import merge

from image_utils import extention


def constant(width, height, color=(1, 1, 1, 0), data_type=PixelType().float):
    """Create constant image with specific dimension and color

    .. code-block::  python

       >>> # import the required module
       >>> from image_utils.nodes import image

       >>> # create a red 4k by 3k constant image in red
       >>> constant_image = image.constant(4000, 3000, (1, 0, 0, 0))

       >>> # save it as png
       >>> constant_image.write('foo.png')

    :type width: int
    :param width: image width
    :type height: int
    :param height: image height
    :type color: tuple
    :param color: rgba color
    :type data_type: OpenImageIO.BASETYPE
    :param data_type: type of image
    :rtype: OpenImageIO.ImageBuf
    :return: constant image
    """
    constant_image = Read(width=width,
                          height=height,
                          channels=4,
                          pixel_type=data_type)
    ImageBufAlgo.fill(constant_image, color, constant_image.roi_full)
    return constant_image


def checker(width,
            height,
            color_a=(1, 1, 1),
            color_b=(0, 0, 0),
            cells=10,
            data_type=PixelType().float):
    """Create checker image. default is black and white checker color

    .. code-block::  python

       >>> # import the checker module
       >>> from image_utils.nodes import image

       >>> # create a 4k checker, red by blue color, with 10 cells
       >>> checker_image = image.checker(4000, 4000, (1, 0, 0), (0, 0, 1), 10)
       >>> checker_image.write('check_me.png')

    Result

    .. image:: ./_static/images/output_examples/check_me.png
       :scale: 5%
       :alt: checker example image
       :align: center

    :type width: int
    :param width: image width
    :type height: int
    :param height: image height
    :type color_a: tuple
    :param color_a: color A
    :type color_b: tuple
    :param color_b: color B
    :type cells: int
    :param cells: number of cell rows
    :type data_type: OpenImageIO.BASETYPE
    :param data_type: type of image
    :rtype: OpenImageIO.ImageBuf
    :return: checker image
    """
    checker_image = ImageBuf(ImageSpec(width, height, 3, data_type))
    ImageBufAlgo.checker(checker_image,
                         width / cells,
                         height / cells,
                         1,
                         color_a,
                         color_b)

    return checker_image


class Read(ImageBuf):
    """Read an existing image

    Example:

    .. code-block::  python

       >>> # import the Read module
       >>> from image_utils.nodes import image

       >>> # read an EXR image
       >>> read_node = image.Read('input.exr')

       >>> # pre-multiply it by its alpha
       >>> read_node.premult()

       >>> # save it as tiff
       >>> read_node.write('output.tif')
    """
    def __init__(self, image_path='',
                 width=100,
                 height=100,
                 channels=4,
                 pixel_type=PixelType().float):
        # construct an image with image path
        if image_path:
            # make sure the path is correct and it exists
            if not os.path.exists(image_path):
                raise UserWarning("Can't locate the input image: "
                                  "{}".format(image_path))
            self.__image_path = image_path
            super(Read, self).__init__(image_path)

        # construct an image with image size
        else:
            new_spec = OIIO.ImageSpec(width, height, channels, pixel_type)
            super(Read, self).__init__(new_spec)

        self.__spec = self.spec()

        # add file format specific attributes
        if self.file_format:
            attribute_data = getattr(extention, self.file_format, None)
            if attribute_data:
                image_extension_attr = attribute_data.items()
                for attr_name, attr_value in image_extension_attr:
                    image_attr_value = self.spec().getattribute(attr_value)
                    setattr(self, attr_name, image_attr_value)

    def __repr__(self):
        return "Image Read node from {}".format(self.path)

    def __str__(self):
        return "image_utils.nodes.image.Read({})".format(self.path)

    def __add__(self, other):
        """Merge with the input image using the 'add' function

        :type other: Read
        :param other: secondary image to add to this image
        :rtype: Read
        :return: the image as a result of the add process
        """
        print(type(other))
        # merge.add(self, other)
        # raise NotImplementedError("This method is not implemented!")

    def premult(self):
        """pre-multiply the channels by alpha"""
        ImageBufAlgo.premult(self, self)

    def unpremult(self):
        """un-premultiply the channels by alpha"""
        ImageBufAlgo.unpremult(self, self)

    @property
    def path(self):
        """Path to the source image

        :rtype: str
        """
        return self.__image_path

    @property
    def data_width(self):
        """Width of the source image's data window

        :rtype: int
        """
        return self.__spec.width

    @property
    def data_height(self):
        """Height of the source image's data window

        :rtype: int
        """
        return self.__spec.height

    @property
    def width(self):
        """Image width

        :rtype: int
        """
        return self.roi_full.width

    @property
    def height(self):
        """Image height

        :rtype: int
        """
        return self.roi_full.height

    @property
    def channels(self):
        """A tuple of strings containing the names of each color channel

        .. code-block:: python

            >>> # import the checker module
            >>> from image_utils.nodes import image

            >>> read_image = image.Read('grid-overscan.exr')
            >>> print(read_image.channels)
            ... ('R', 'G', 'B', 'A')

        :rtype: tuple
        :return: list of existing channel
        """
        return self.__spec.channelnames

    @property
    def has_alpha(self):
        """Whether or not the image has alpha

        :rtype: bool
        :return: True or False
        """
        return bool(self.__spec.alpha_channel > 0)

    @property
    def file_format(self):
        """Returns the file format of the image"

        .. code-block:: python

            >>> from image_utils.nodes import image
            >>> image_node = image.Read('foo.exr')
            >>> print(image_node.file_format)
            ... openexr

        :rtype: str
        """
        return self.file_format_name

    @property
    def data_window_coordinate(self):
        """X and Y coordinate of data window (a.k.a. display window)

        .. code-block:: python

            >>> # import the checker module
            >>> from image_utils.nodes import image

            >>> read_image = image.Read('grid-overscan.exr')
            >>> print(read_image.data_window_coordinate)
            ... (-250, -250, 1250, 1250)

        .. image:: ./_static/images/output_examples/grid_overscan_exr.png
           :scale: 30
           :align: center

        :rtype: tuple
        """
        return (self.xbegin,
                self.ybegin,
                self.xend,
                self.yend)

    def set_data_window(self, x1, y1, x2, y2):
        """set data window (a.k.a. display window)

        :type x1: int
        :param x1: x begin
        :type y1: int
        :param y1: y begin
        :type x2: int
        :param x2: x end
        :type y2: int
        :param y2: y end
        """
        self.set_full(x1, x2, y1, y2, 0, 0)

    def duplicate(self, pixel_type=None):
        """make a exact copy of this image. If a file_format is provided, this
        will get the specified pixel data type rather than using the same pixel
        file_format as the source ImageBuf.

           Example:

                >>> from image_utils.nodes import image
                >>> from image_utils.pixel_type import PixelType
                >>> # create an image instance
                >>> A = image.Read('foo.exr')
                >>> # make a copy of it
                >>> B = A.duplicate(PixelType().bit8)

        :rtype pixel_type: OpenImageIO.BASETYPE
        :param pixel_type: new image type. i.e, float, half, 8bit
        :rtype: Image
        :return: duplicate of this image
        """

        # use the same pixel type as the source image if not specified
        if not pixel_type:
            pixel_type = self.pixeltype

        # Create an empty image with the same specs as the source image
        copy_image = Read(width=self.width,
                          height=self.height,
                          channels=len(self.channels),
                          pixel_type=pixel_type)

        copy_image.copy(self, pixel_type)

        return copy_image


if __name__ == '__main__':
    print(__doc__)
