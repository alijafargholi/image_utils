"""
Implementing **transform** node features:

- **Crop**: Crop an image by the specified window
- **Crop_by_data_window**: Crop an image by its data window
- **Resize**: Resize the image to the new width and height. *Note that if the
  new dimensions do not match the image proportion the image will be stretch*
- **Scale**: Scale the image by given factor
"""
from OpenImageIO import ImageBufAlgo
from OpenImageIO import ROI

from image_utils.image import Read


def crop(source_image, x1, y1, x2, y2):
    """crop the given image by the given window. begin point is at top-left and
       end point is at the lower-right of the image.

    Example:

    ::

        >>> # read an image
        >>> source_image = Read('source.exr')
        >>> # crop the source image and store it in a new variable
        >>> bar = crop(source_image, 10, 10, 510, 510)
        >>> # save the cropped image as a new image on disk
        >>> bar.write('cropped.png')

    :type source_image: Image
    :param source_image: source image to crop
    :type x1: int
    :param x1: X coordinate of beginning of the crop window
    :type y1: int
    :param y1: Y coordinate of beginning of the crop window
    :type x2: int
    :param x2: X coordinate of end of the crop window
    :type y2: int
    :param y2: Y coordinate of end of the crop window
    :rtype: Image
    :return: cropped image if crop process successful, otherwise source image
    """
    # calculate the new width and height
    width = x2 - x1
    height = y2 - y1

    # construct a new image
    number_of_channels = len(source_image.channels)
    cropped_image = Read(width=width,
                         height=height,
                         channels=number_of_channels,
                         pixel_type=source_image.pixeltype)
    # crop the source image into the new image
    crop_window = ROI(x1, x2, y1, y2)
    crop_result = ImageBufAlgo.crop(cropped_image, source_image, crop_window)

    if crop_result:
        return cropped_image

    # TODO: Log instead of printing
    print "ERROR: failed during the crop process:", cropped_image.geterror()
    return source_image


def crop_by_data_window(source_image):
    """corp the source image to its data window.

    :type source_image: Read
    :param source_image: source image to crop
    :rtype: Read
    :return: cropped image if crop process successful, otherwise source image
    """
    # crop the source image by it's data window coordinate
    return crop(source_image, *source_image.data_window_coordinate)


def resize(source_image, width, height):
    """resize the given image into the new width and height

    Example:

    ::

        >>> # read an image
        >>> source_image = Read('source.exr')
        >>> # resize the source image and store it in a new variable
        >>> bar = resize(source_image, 1000, 500)
        >>> # save the resize image as a new image on disk
        >>> bar.write('resize.png')

    :type source_image: Image
    :param source_image: source image to crop
    :type width: int
    :param width: width size
    :type height: int
    :param height: height size
    :rtype: Image
    :return: resize image if resize process successful, otherwise source image
    """
    number_of_channels = len(source_image.channels)
    scale_resize = Read(width=width,
                        height=height,
                        channels=number_of_channels,
                        pixel_type=source_image.pixeltype)
    resize_result = ImageBufAlgo.resize(scale_resize, source_image)

    if resize_result:
        return scale_resize

    # Log instead of printing
    print "ERROR: failed during the resize process:", scale_resize.geterror()
    return source_image


def scale(source_image, scale_value):
    """scale the given image iby the scale value.

    Example:

    ::

        >>> # read an image
        >>> source_image = Read('source.exr')
        >>> # scale the source image and store it in a new variable
        >>> bar = scale(source_image, 1.5)
        >>> # save the scaled image as a new image on disk
        >>> bar.write('scaled.png')

    :type source_image: Image
    :param source_image: source image to crop
    :type scale_value: float
    :param scale_value: scale value
    :rtype: Image
    :return: scaled image if scale process successful, otherwise source image
    """
    new_width = int(source_image.width*scale_value)
    new_height = int(source_image.height*scale_value)

    return resize(source_image, new_width, new_height)


if __name__ == '__main__':
    print(__doc__)
