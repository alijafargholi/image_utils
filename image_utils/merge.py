"""
============
Merge Node
============

- **Over**: Composite input A over input B
- **ZOver**: Composite input A and input B based on their z channel
- **Add**: Add the pixel value of input A to input B
- **Sub**: Subtract the pixel value of input A from input B
"""
from OpenImageIO import ImageBufAlgo

from image_utils.image import Read


def over(input_a, input_b):
    """composite *(merge)* input A over input B

    Example:

    ..

       >>> from image_utils.image import Read
       >>> from image_utils.merge import over
       >>> foreground_image = Read("fg.exr")
       >>> background_image = Read("bg.exr")
       >>> merged_image = over(foreground_image, background_image)
       >>> merged_image.write("result.exr")

    :type input_a: Read
    :param input_a: foreground image
    :type input_b: Read
    :param input_b: background image
    :rtype: Read
    :return: merged read object
    """

    comp = input_b.duplicate()
    input_a.premult()
    ImageBufAlgo.over(comp, input_a, input_b)

    if comp.has_error:
        print "Error merging over:", comp.geterror()

    return comp


def zover(input_a, input_b):
    """composite input A and input B using their respective Z channels to
       decide which is in front on a pixel-by-pixel basis.

    Example:

    ..

       >>> from image_utils.image import Read
       >>> from image_utils.merge import zover
       >>> image_a = Read("A.exr")
       >>> image_b = Read("B.exr")
       >>> z_merged_image = over(image_a, image_b)
       >>> z_merged_image.write("result.exr")

    :type input_a: Read
    :param input_a: foreground image
    :type input_b: Read
    :param input_b: background image
    :rtype: Read
    :return: merged read object
    """
    zcomp = input_b.duplicate()

    ImageBufAlgo.zover(zcomp, input_a, input_b)

    if zcomp.has_error:
        print "Error merging zover:", zcomp.geterror()

    return zcomp


def add(input_a, input_b):
    """add input A to input B

    Example:

    ..

       >>> from image_utils.image import Read
       >>> from image_utils.merge import add
       >>> input_a = Read("image_a.exr")
       >>> input_b = Read("image_b.exr")
       >>> add_image = add(input_a, input_b)
       >>> add_image.write("result.exr")

    :type input_a: Read
    :param input_a: foreground image
    :type input_b: Read
    :param input_b: background image
    :rtype: Read
    :return: result read object
    """
    add_comp = input_b.duplicate()

    ImageBufAlgo.add(add_comp, input_a, input_b)

    if add_comp.has_error:
        print "Error merging adding:", add_comp.geterror()

    return add_comp


def sub(input_a, input_b):
    """subtract input A from input B.

    Example:

    ..

       >>> from image_utils.image import Read
       >>> from image_utils.merge import sub
       >>> input_a = Read("image_a.exr")
       >>> input_b = Read("image_b.exr")
       >>> sub_image = sub(input_a, input_b)
       >>> sub_image.write("result.exr")

    :type input_a: Read
    :param input_a: foreground image
    :type input_b: Read
    :param input_b: background image
    :rtype: Read
    :return: merged read object
    """
    sub_comp = input_b.duplicate()

    ImageBufAlgo.sub(sub_comp, input_a, input_b)

    if sub_comp.has_error:
        print "Error merging subtracting:", sub_comp.geterror()

    return sub_comp
