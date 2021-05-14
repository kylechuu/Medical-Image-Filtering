# Use this file as you wish to generate the images needed to answer the report
import src.project.Utilities as util
import src.project.ImageSynthesisNoise as isn
import cv2
import numpy as np

# image = util.loadImage('images/brain.png')
matrix = util.loadMatrix('images/noisyimage.npy')
rows, cols = matrix.shape
mask = isn.gaussianLowpassFilter((rows, cols), cutoff=40)
im = np.multiply(matrix, mask)
im = util.post_process_images(util.getImage(im))

# im = np.abs(matrix)
# im = util.post_process_images(im)
# rows, cols = image.shape

util.displayImage(im)


# mask = isn.butterworthLowpassFilter((rows, cols), cutoff=40, order=7)
# mask = isn.gaussianHighpassFilter((rows, cols), cutoff=150)

# shift_fft = util.getDFT(image)
# filtered_image_fft = np.multiply(mask, shift_fft)
# filtered_image = util.post_process_images(util.getImage(filtered_image_fft))

# util.saveImage('butterworthLowpassFilter.png', filtered_image)
# print(util.signalToNoise(filtered_image))

# util.displayImage(filtered_image)



