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


def over(input_a, input_b):
    """composite *(merge)* input A over input B

    .. code-block: python

       >>> from image_utils.nodes import image
       >>> from image_utils.nodes import merge
       >>> foreground_image = image.Read("fg.exr")
       >>> background_image = image.Read("bg.exr")
       >>> merged_image = merge.over(foreground_image, background_image)
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

    .. code-block:: python

       >>> from image_utils.nodes import image
       >>> from image_utils.nodes import merge
       >>> image_a = image.Read("A.exr")
       >>> image_b = image.Read("B.exr")
       >>> z_merged_image = merge.over(image_a, image_b)
       >>> z_merged_image.write("result.exr")

    :type input_a: Read
    :param input_a: foreground image
    :type input_b: :ref:`Read <read-node>`
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

       >>> from image_utils.nodes import image
       >>> from image_utils.nodes import merge
       >>> input_a = image.Read("image_a.exr")
       >>> input_b = image.Read("image_b.exr")
       >>> add_image = merge.add(input_a, input_b)
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

    .. code-block:: python

       >>> from image_utils.nodes import image
       >>> from image_utils.nodes import merge
       >>> input_a = image.Read("image_a.exr")
       >>> input_b = image.Read("image_b.exr")
       >>> sub_image = merge.sub(input_a, input_b)
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
