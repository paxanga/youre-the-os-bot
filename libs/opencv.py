import cv2 as cv
import pyautogui as pg
import numpy as np


class OpenCV:
    def __init__(self):
        self.capture = None

    def FindImageOnScreen(self, image, gray, capture, threshold, click, return_pos):
        if gray:
            image = cv.imread(image, cv.IMREAD_GRAYSCALE)
        else:
            image = cv.imread(image)

        # cv.imshow("image", image)
        # cv.imshow("capture", capture)
        # cv.waitKey(0)
        result = cv.matchTemplate(capture, image, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        # print(max_val)
        if max_val >= threshold:
            if click:
                # click in the middle of the image
                pg.click(max_loc[0] + (image.shape[1] / 2),
                         max_loc[1] + (image.shape[0] / 2))
            if return_pos:
                return (max_loc[0] + (image.shape[1] / 2), max_loc[1] + (image.shape[0] / 2))
            return True
        else:
            return False
        
    def FindColorOnScreen(self, color_hex, capture, tolerance, return_pos):

        # color = convert hex to rgb
        color_hex = color_hex.replace("0x", "") 
        color_rgb = tuple(int(color_hex[i:i+2], 16) for i in (0, 2, 4))
        
        # Cambia el orden de los componentes para convertir de RGB a BGR
        color_bgr = (color_rgb[2], color_rgb[1], color_rgb[0])

        region_left = 0
        region_top = 0
        region_width = capture.shape[1]
        region_height = capture.shape[0]

        for y in range(region_top, region_top + region_height):
            for x in range(region_left, region_left + region_width):
                pixel_color_bgr = capture[y, x]
                color_diff = sum(abs(pixel_color_bgr[i] - color_bgr[i]) for i in range(3))
                if color_diff <= tolerance:
                    if return_pos:
                        return (x, y)
                    else:
                        return True
        return False

    def pressKey(self, key):
        pg.press(key)

    def click(self, x, y):
        pg.click(x, y)
