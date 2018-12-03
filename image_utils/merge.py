"""
Implementing **merge** node features:

- **Over**: composite input a over input B
- **ZOver**: composite input and input B based on their z channel
- **Add**:
- **Sub**:
- **premult**:
- **unpremult**:
- **clamp**:

"""


# TODO: not implement yet
def over(input_a, input_b):
    """composite input A over input B

    :param input_a:
    :param input_b:
    :return:
    """
    #     bool ImageBufAlgo.over (dst, A, B, roi=ROI.All, nthreads=0)
    # Composite ImageBuf A over ImageBuf B.
    # Examples:
    # Comp = ImageBufAlgo.over (ImageBuf("fg.exr"), ImageBuf("bg.exr"))


# TODO: not implement yet
def zover(input_a, input_b):
    """composite input A and input B using their respective Z channels to
    decide which is in front on a pixel-by-pixel basis.

    :param input_a:
    :param input_b:
    :return:
    """
    #     bool ImageBufAlgo.zover (dst, A, B, bool z zeroisinf=False,
    # roi=ROI.All, nthreads=0)
    # Composite ImageBuf A and ImageBuf B using their respective Z channels to decide which
    # is in front on a pixel-by-pixel basis.
    # Examples:
    # Comp = ImageBufAlgo.zover (ImageBuf("fg.exr"), ImageBuf("bg.exr"))


# TODO: not implement yet
def add(input_a, input_b):
    """add input A to input B

    :param input_a:
    :param input_b:
    :return:
    """
    # ImageBufAlgo.unpremult(dst, src, roi=ROI.All, nthreads=0)


# TODO: not implement yet
def sub(input_a, input_b):
    """subtract input A from input B.

    :param input_a:
    :param input_b:
    :return:
    """
    #     bool ImageBufAlgo.sub (dst, A, B, roi=ROI.All, nthreads=0)
    # Compute A - B. A and B each may be an ImageBuf, a float value (for all channels) or a
    # tuple giving a float for each color channel.
    # Examples:
    # buf = ImageBufAlgo.sub (ImageBuf("a.exr"), ImageBuf("b.exr"))


# TODO: not implement yet
def premult(source_image):
    """pre-multiply the channels by alpha

    :param source_image:
    :return:
    """
    # bool ImageBufAlgo.premult (dst, src, roi=ROI.All, nthreads=0)


# TODO: not implement yet
def unpremult(source_image):
    """un-premultiply the channels by alpha

    :param source_image:
    :return:
    """
    # bool ImageBufAlgo.unpremult (dst, src, roi=ROI.All, nthreads=0)


# TODO: not implement yet
def clamp(source_image, min_value, max_value):
    """clamp the source image's pixel values between given min and max limit.

    :param source_image:
    :param min_value:
    :param max_value:
    :return:
    """
    # bool ImageBufAlgo.clamp (dst, src, min, max, bool clampalpha01=False,
    # roi=ROI.All, nthreads=0)
    # Copy pixels while clamping between the min and max values. The min and max may
    # either be tuples (one min and max value per channel), or single floats (same value for
    # all channels). Additionally, if clampalpha01 is True, then any alpha channel is clamped
    # to the 0–1 range.
    # Examples:
    # OpenImageIO Programmer’s Documentation
    # 11.9. IMAGEBUFALGO 281
    # # Clamp image buffer A in-place to the [0,1] range for all channels.
    # ImageBufAlgo.clamp (A, A, 0.0, 1.0)