# Use this file as you wish to generate the images needed to answer the report

import src.project.Utilities as util
import numpy as np
import src.project.SelectiveImageAcquisition as sia

image = util.loadImage('images/brain.png')
rows, cols = image.shape
print(image.shape)
# code for cardiac cartesian
# mask = sia.cartesianPattern((rows, cols), 0.7)
mask = sia.circlePattern((rows, cols), 90)

shift_fft = util.getDFT(image)
filtered_image_fft = np.multiply(mask, shift_fft)
filtered_image = util.post_process_images(util.getImage(filtered_image_fft))

util.displayImage(filtered_image)

