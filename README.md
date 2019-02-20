# Image Utils [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

Utility/Convenient API that handles the common **image** processing
such as read, write, image conversion, resize, etc.

The idea behind this utility module is to mimic the basic [Nuke](https://www.foundry.com/products/nuke) 
feature via `python`. This library uses `OpenImageIO` at its core and utilizes 
its API features 

==If you are comfortable with using OpenImageIo itself, I 
recommend using that instead of this library. This library 
is mostly for training purposes==

## Documentation

For more info, please visit the [documentation page](https://alijafargholi.github.io/image_utils/)

## Getting Started

``` python
>>> from image_utils.nodes.image import constant
>>> from image_utils.nodes.image import Read
>>> from image_utils.nodes.transform import resize
>>> from image_utils.nodes.merge import over
>>> # create a red 4k constant image
>>> constant_image = constant(4000, 4000, (1, 0, 0, 0))
>>> # read an image into buffer
>>> buffer_image = image.Read('input.exr')
>>> # resize the input image to 4k
>>> resize_image = resize(buffer_image, 4000, 4000)
>>> # comp the input image over the contant image
>>> comp_image = over(resize_image, constant_image)
>>> # save the comp image into disk as PNG
>>> comp_image.write('comp.png')
```

### Prerequisites

This API utilize the [OpenImageIo](https://github.com/OpenImageIO/oiio.git) library

- For Windows installation please [visit here](https://github.com/OpenImageIO/oiio/blob/master/INSTALL.md)
- For MacOs installation you can use [brew]()
   ```bash
   brew install OpenImageIO
   ```

### Installing

Clone the repository somewhere in your `PYTHONPATH`

## Running the tests

WIP

## Contributing

* **Ali Jafargholi**

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who toke the time to test/use this
