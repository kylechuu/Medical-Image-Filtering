import numpy as np
import cv2


def idealLowpassFilter(emptymask, cutoff):
    rows, cols = emptymask
    mask = np.zeros((rows, cols))
    center_row, center_col = int(rows/2), int(cols/2)
    for row in range(rows):
        for col in range(cols):
            distance = np.sqrt((row - center_row)**2 + (col - center_col)**2)
            if distance <= cutoff:
                mask[row][col] = 1
            else:
                mask[row][col] = 0
    return mask


def idealHighpassFilter(emptymask, cutoff):
    rows, cols = emptymask
    mask = np.zeros((rows, cols))
    center_row, center_col = int(rows/2), int(cols/2)
    for row in range(rows):
        for col in range(cols):
            distance = np.sqrt((row - center_row)**2 + (col - center_col)**2)
            if distance <= cutoff:
                mask[row][col] = 0
            else:
                mask[row][col] = 1
    return mask


def gaussianLowpassFilter(emptymask, cutoff):
    rows, cols = emptymask
    mask = np.zeros((rows, cols))
    mid_R, mid_C = int(rows/2), int(cols/2)
    for i in range(rows):
        for j in range(cols):
            d = np.sqrt((i - mid_R) ** 2 + (j - mid_C) ** 2)
            mask[i, j] = np.exp(-(d * d) / (2 * cutoff * cutoff))
    return mask


def gaussianHighpassFilter(emptymask, cutoff):
    mask = 1 - gaussianLowpassFilter(emptymask, cutoff)
    return mask


def butterworthLowpassFilter(emptymask, cutoff, order):
    rows, cols = emptymask
    mask = np.zeros((rows, cols))

    for row in range(0, rows):
        for col in range(0, cols):
            a = (row - rows/2)*(row - rows/2)
            b = (col - cols/2)*(col - cols/2)
            c = np.sqrt(a + b)
            d = ((c/cutoff)**(2*order))
            mask[row][col] = 1/(d + 1)
    return mask


def butterworthHighpassFilter(emptymask, cutoff, order):
    return 1 - butterworthLowpassFilter(emptymask, cutoff, order)



def ringLowpassFilter(emptymask, cutoff, thickness):
    rows, cols = emptymask
    mask = np.zeros((rows, cols))
    mask1 = cv2.circle(mask, (int(rows / 2), int(cols / 2)), cutoff, (1, 1), thickness)
    return mask1


def ringHighpassFilter(emptymask, cutoff, thickness):
    mask = None
    return mask

