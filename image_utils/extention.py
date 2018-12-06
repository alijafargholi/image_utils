"""

"""

openexr = {
    'colorspace': 'oiio:ColorSpace',
    'compression': 'compression',
    'resolution_unit': 'ResolutionUnit',
    'x_resolution': 'XResolution',
    'y_resolution': 'YResolution',
    'created_at': 'DateTime',
    'world_to_camera': 'worldtocamera',  # matrix
    'world_to_screen': 'worldtoscreen',  # matrix
    'exposure': 'ExposureTime',  # float
    'aperture': 'FNumber',  # float
    'ratio': 'PixelAspectRatio'}

jpeg = {
    "description": "ImageDescription",  # string the JPEG Comment field
    "orientation": "Orientation",  # int the image orientation
    "x_resolution": "XResolution",
    "y_resolution": "YResolution",
    "resolution_unit": "ResolutionUnit",
    "compression": "CompressionQuality",  # int Quality of compression (1-100)
    "icc": "ICCProfile",  # uint8[] The ICC color profile
    "sub_sampling": "jpeg:subsampling"}

png = {
    "description": "ImageDescription",  # string Description
    "author": "Artist",  # string Author
    "title": "DocumentName",  # string Title
    "timestamp": "DateTime",  # string the timestamp in the PNG header
    "ratio": "PixelAspectRatio",  # float pixel aspect ratio
    "x_resolution": "XResolution",
    "y_resolution": "YResolution",
    "resolution_unit": "ResolutionUnit",
    "colorspace": "oiio:ColorSpace",  # string Color space (see Section B.3).
    "gamma": "oiio:Gamma",  # float the gamma correction value (if specified).
    "icc": "ICCProfile"}

psd = {
    "raw_color": "oiio:RawColor"
    }

raw = {
    "auto_bright": "raw:auto_bright",  # int If nonzero, will use libraws exposure correction. (Default: 0)
    "use_camera_wb": "raw:use_camera_wb",  # int If 1, use libraws camera white balance adjustment (Default: 1)
    "use_camera_matrix": "raw:use_camera_matrix",  # int Whether to use the embedded color profile, if its present: 0 = never, 1 (default) = only for DNG files, 3 = always.
    "adjust_max_thr": "raw:adjust_maximum_thr",  # float If nonzero, auto-adjusting maximum value. (Default:0.0)
    "user_saturate": "raw:user_sat",  # int If nonzero, sets the camera maximum value that will be normalized to appear saturated. (Default:0)
    "aberration": "raw:aber",  # float[2] Red and blue scale factors for chromatic aberration correction when decoding the raw image. The default (1,1) means to perform no correction. This is an overall spatial scale, sensible values will be very close to 1.0.
    "colorspace": "raw:ColorSpace",  # string Which color primaries to use: "raw", "sRGB", "Adobe", "Wide", "ProPhoto", "ACES", "XYZ".(Default: "sRGB")
    "exposure": "raw:Exposure",  # float Amount of exposure before de-mosaicing, from 0.25 (2 stop darken) to 8 (3 stop brighten). (Default:0, meaning no correction.)
    "demosaic": "raw:Demosaic",  #string Force a demosaicing algorithm: "linear", "VNG", "PPG", "AHD" (default), "DCB","AHD-Mod", "AFD", "VCD", "Mixed", "LMMSE","AMaZE", "DHT", "AAHD", "none".
    "highlight_mode": "raw:HighlightMode",  # int
}

tiff = {
    "description": "ImageDescription",  # string comment
    "author": "Artist",  # string author
    "title": "DocumentName",  # string job name/ID
    "software": "Software",  # string software name
    "time_stamp": "DateTime",  # string TGA time stamp
    "job_time": "targa:JobTime",  # string TGA job time.
    "compression": "Compression",
    "image_id": "targa:ImageID",  # string Image ID
    "ratio": "PixelAspectRatio",  # float pixel aspect ratio
    "git_sample": "oiio:BitsPerSample",  # int the true bits per sample.
    "colorspace": "oiio:ColorSpace",  # string Color space (see Section B.3).
    "gamma": "oiio:Gamma",
    "associate_alpha": "oiio:UnassociatedAlpha",
    "raw_color": "oiio:RawColor",
    "tiff_colorspace": "tiff:ColorSpace",  # Choices are RGB, CMYK
    "zip_quality": "tiff:zipquality",  # for "zip" compression, ranging from
                                       # 1-9 (default is 6). Higher means
                                       # compress to less space
    "x_resolution": "XResultion",
    "y_resolution": "YResolution",
    "resolution_unit": "ResolutionUnit",  # string ResolutionUnit ("in" or "cm")
    "orientation": "Orientation",  # int Orientation
    "icc": "ICCProfile",
}
