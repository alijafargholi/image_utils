Quick Examples
==============

.. code-block::  python

   # import the required libraries
   from image_utils.image import constant
   from image_utils.image import Read
   from image_utils.transform import resize
   from image_utils.merge import over

   # create a red 4k constant image
   constant_image = constant(4000, 4000, (1, 0, 0, 0))
   # read an image into buffer
   buffer_image = image.Read('input.exr')
   buffer_image.premult()
   # resize the input image to 4k
   resize_image = resize(buffer_image, 4000, 4000)
   # comp the input image over the constant image
   comp_image = over(resize_image, constant_image)
   # save the comp image into disk as PNG
   comp_image.write('comp.png')
