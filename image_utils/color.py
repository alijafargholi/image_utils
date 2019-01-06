"""
============
Color Node
============

**Clamp**: clamp the pixel value of the input image between min and max value
**Gamma**: gamma the pixel value of the input image by given value

"""
from __future__ import print_function

from OpenImageIO import ImageBufAlgo

from image_utils.image import Read


def clamp(input_image, min_value, max_value, clamp_alpha=False):
    """clamp the source image's pixel values between given min and max limit.

    Example:

    ..

       >>> from image_utils.image import Read
       >>> from image_utils.color import clamp
       >>> source_image = Read("source.exr")
       >>> clamped_image = clamp(source_image, 0.1, 1.0)
       >>> clamped_image.write("result.exr")

    :type input_image: Read
    :param input_image: input image to be clamped
    :type min_value: float
    :param min_value: minimum pixel value
    :type max_value: float
    :param max_value: maximum pixel value
    :type clamp_alpha: bool
    :param clamp_alpha: weather or not to clamp the alpha channel as well
    :rtype: Read
    :return: result of the clamped image
    """
    result = input_image.duplicate()
    ImageBufAlgo.clamp(result,
                       input_image,
                       min_value,
                       max_value,
                       clampalpha01=clamp_alpha)
    if result.has_error:
        print("Error clamping:", result.geterror())

    return result


# TODO: not implement yet
def set_color_look(input_image, look):
    """apply an OpenColorIo "look" transform to the pixels

    :param source_image:
    :param look:
    :return:
    """
    # bool ImageBufAlgo.ociolook (dst, src, looks, from, to,
    # inverse=False, unpremult=True,
    # context key="", context value="", colorconfig="",
    # roi=ROI.All, nthreads=0)
    # Apply an OpenColorIO "look" transform to the pixel values.
    # Examples:
    # Src = ImageBuf ("tahoe.jpg")
    # Dst = ImageBufAlgo.ociolook (Src, "look", "vd8", "lnf",
    # context_key="SHOT", context_value="pe0012")


# TODO: not implement yet
def set_color_display(input_image, display):
    """apply an OpenColorIo "display" transform to the pixels

    :param source_image:
    :param display:
    :return:
    """
    # bool ImageBufAlgo.ociodisplay (dst, src, display, view,
    # from=None, looks=None, unpremult=True,
    # context key="", context value="", colorconfig="",
    # roi=ROI.All, nthreads=0)
    # Apply an OpenColorIO "display" transform to the pixel values.
    # Examples:
    # Src = ImageBuf ("tahoe.exr")
    # Dst = ImageBufAlgo.ociodisplay (Src, "sRGB", "Film", "lnf",
    # context_key="SHOT", context_value="pe0012")


def gamma(input_image, gamma_r, gamma_g=None, gamma_b=None, gamma_a=1.0):
    """apply gamma change to the source image.

    .. note: if only gamma value for red channel is provided, it'll be used for
             green and blue channel

    Example:

    ..

       >>> from image_utils.image import Read
       >>> from image_utils.color import gamma
       >>> source_image = Read("source.exr")
       >>> gamma_corrected = gamma(source_image, 2.2)
       >>> gamma_corrected.write("result.exr")

    :type input_image: Read
    :param input_image: input image to be gamma corrected
    :type gamma_r: float
    :param gamma_r: gamma value for red channel, or all channel.
    :type gamma_g: float
    :param gamma_g: gamma value for green channel *(optional)*
    :type gamma_b: float
    :param gamma_b: gamma value for blue channel *(optional)*
    :type gamma_a: float
    :param gamma_a: gamma value for alpha channel, default is 1 *(optional)*
    :rtype: Read
    :return: gamma corrected image
    """
    if not gamma_g:
        gamma_g = gamma_r
    if not gamma_b:
        gamma_b = gamma_r

    result = input_image.duplicate()

    ImageBufAlgo.pow(result, input_image, (gamma_r, gamma_g, gamma_b, gamma_a))

    if result.has_error:
        print("Error gamma:", result.geterror())

    return result
