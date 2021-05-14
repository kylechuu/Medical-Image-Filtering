import numpy as np
import cv2

##
# Objective: Simulate different types of acquisition patterns by implementing the
# following functions.
##


def cartesianPattern(mask_size, percent):
    rows, cols = mask_size
    mask = np.zeros((rows, cols))
    lines = int(cols * percent)
    for line in range(0, cols, int(cols/lines)):
        mask = cv2.line(mask, (0, line), (rows, line), (1, 1), 1)

    return mask


def circlePattern(mask_size, radius):
    rows, cols = mask_size
    mask = np.zeros((rows, cols))
    mask = cv2.circle(mask, (int(rows/2), int(cols/2)), radius, (1, 1), -1)
    return mask


def ellipsePattern(mask_size, major_axis, minor_axis, angle):
    rows, cols = mask_size
    mask = np.zeros((rows, cols))
    mask = cv2.ellipse(mask, (int(rows / 2), int(cols / 2)), (major_axis, minor_axis), angle, 0, 360, (1, 1), -1)
    return mask


def bandPattern(mask_size, width, length, angle):
    rows, cols = mask_size
    mask = np.zeros((rows, cols))

    minAreaRect = ((int(rows / 2), int(cols / 2)), (np.abs(length), np.abs(width)), angle)
    rectCnt = np.int0(cv2.boxPoints(minAreaRect))
    cv2.drawContours(mask, [rectCnt], -1, (1,1), -1)

    return mask


def radialPattern(mask_size, ray_count):
    rows, cols = mask_size
    mask = np.zeros((rows, cols))
    for angle in range(0, 180, int(180/ray_count)):
        minAreaRect = ((int(rows / 2), int(cols / 2)), (np.abs(rows), 0), angle)
        rectCnt = np.int0(cv2.boxPoints(minAreaRect))
        cv2.drawContours(mask, [rectCnt], -1, (1, 1), -1)

    return mask


def spiralPattern(mask_size, sparsity):
    mask = None
    return mask
