"""

"""


# TODO: not implement yet
def set_color_look(source_image, look):
    """apply an OpenColorIo "look" transform to the pixels

    :param source_image:
    :param look:
    :return:
    """
    # bool ImageBufAlgo.ociolook (dst, src, looks, from, to,
    # inverse=False, unpremult=True,
    # context key="", context value="", colorconfig="",
    # roi=ROI.All, nthreads=0)
    # Apply an OpenColorIO “look” transform to the pixel values.
    # Examples:
    # Src = ImageBuf ("tahoe.jpg")
    # Dst = ImageBufAlgo.ociolook (Src, "look", "vd8", "lnf",
    # context_key="SHOT", context_value="pe0012")


# TODO: not implement yet
def set_color_display(source_image, display):
    """apply an OpenColorIo "display" transform to the pixels

    :param source_image:
    :param display:
    :return:
    """
    # bool ImageBufAlgo.ociodisplay (dst, src, display, view,
    # from=None, looks=None, unpremult=True,
    # context key="", context value="", colorconfig="",
    # roi=ROI.All, nthreads=0)
    # Apply an OpenColorIO “display” transform to the pixel values.
    # Examples:
    # Src = ImageBuf ("tahoe.exr")
    # Dst = ImageBufAlgo.ociodisplay (Src, "sRGB", "Film", "lnf",
    # context_key="SHOT", context_value="pe0012")


def gamma(source_image, gamma):
    """apply gamma change to the source image.

    :param source_image:
    :param gamma:
    :return:
    """
    # bool ImageBufAlgo.pow (dst, A, B, roi=ROI.All, nthreads=0)
    # Compute pow (A, B (channel-by-channel exponentiation). A is an ImageBuf, and B may
    # be a float (a single power for all channels) or a tuple giving a float for each color
    # channel.
    # Examples:
    # # Linearize a 2.2 gamma-corrected image (channels 0-2 only)
    # img = ImageBuf ("a.exr")
    # buf = ImageBufAlgo.pow (img, (2.2, 2.2, 2.2, 1.0))