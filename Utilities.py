import os
from pathlib import Path
import cv2
import numpy as np
from numpy import asarray


def loadImage(image_path):
    image = cv2.imread(str(Path(os.getcwd())) + "/" + image_path, 0)
    return image


def loadMatrix(filename):
    matrix = np.load(str(Path(os.getcwd())) + "/" + filename)
    return matrix


def saveImage(filename, image):
    cv2.imwrite(str(Path(os.getcwd())) + "/" + filename, image)
    return True


def saveMatrix(filename, matrix):
    np.save(str(Path(os.getcwd())) + "/" + filename, matrix)
    return True


# map input image to values from 0 to 255"
def normalizeImage(image):
    normalized = image * 255.0 / image.max()
    normalized = normalized.astype('float64')
    return normalized


# # Remember: the DFT its a decomposition of signals
# #  To be able to save it as an image you must convert it.
def writableDFT(dft_image):
    converted = None
    return converted


# # Use openCV to display your image"
# # Remember: normalize binary masks and convert FFT matrices to be able to see and save them"
def displayImage(image):
    cv2.namedWindow("Image")
    cv2.imshow("Image", image)
    cv2.waitKey()
    cv2.destroyAllWindows()


def getDFT(image):
    fft = np.fft.fft2(image)
    dft_shift = np.fft.fftshift(fft)
    return dft_shift


# Confert from fft matrix to an image"
def getImage(dft_img):
    idft = np.fft.ifftshift(dft_img)
    ifft = np.fft.ifft2(idft).real

    # return np.uint8(cv2.magnitude(np.real(ifft),np.imag(ifft)))
    return normalizeImage(ifft)






# # Both input values must be raw values"
def applyMask(image_dft, mask):
    return image_dft * mask


def signalToNoise():
    return False


def signalToNoise(matrix, axis=0, ddof=0):
    matrix = np.asanyarray(matrix)
    me = matrix.mean(axis)
    sd = matrix.std(axis=axis, ddof=ddof)
    return np.abs(np.where(sd == 0, 0, me/sd))


# [Provide] Use this function to acomplish a good final image
def post_process_image(image):
    a = np.min(image)
    b = np.max(image)
    k = 255
    image = (image - a) * (k / (b - a))
    return image.astype('uint8')

def post_process_images(image):
    a = 0
    b = 255
    c = np.min(image)
    d = np.max(image)
    rows, columns = np.shape(image)
    image1 = np.zeros((rows, columns), dtype=int)
    for i in range(rows):
        for j in range(columns):
            if (d - c) == 0:
                image1[i, j] = ((b - a) / 0.000001) * (image[i, j] - c) + a
            else:
                image1[i, j] = ((b - a) / (d - c)) * (image[i, j] - c) + a

    return np.uint8(image1)
