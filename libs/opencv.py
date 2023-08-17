import cv2 as cv
import pyautogui as pg


class OpenCV:
    def __init__(self):
        self.capture = None

    def FindImageOnScreen(self, image, gray, capture, threshold, click):
        if gray:
            image = cv.imread(image, cv.IMREAD_GRAYSCALE)
        else:
            image = cv.imread(image)

        # cv.imshow("image", image)
        # cv.imshow("capture", capture)
        # cv.waitKey(0)
        result = cv.matchTemplate(capture, image, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        print(max_val)
        if max_val >= threshold:
            if click:
                # click in the middle of the image
                pg.click(max_loc[0] + (image.shape[1] / 2),
                         max_loc[1] + (image.shape[0] / 2))
            return True
        else:
            return False
        
    def pressKey(self, key):
        pg.press(key)
