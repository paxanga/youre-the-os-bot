from src import checkRequired
import cv2 as cv
from src import captureWorker
import const
import time


class Main:
    def __init__(self):
        self.const = const.Const()
        self.main()

    def main(self):
        if checkRequired.CheckRequired():
            print("All required are ok")
            self.StartGame()
        
    def StartGame(self):
        self.capture = captureWorker.CaptureWorker(self.const.WINDOW_NAME)
        self.capture.start()
        time.sleep(5)
        self.FindImageOnScreen("src\__img\play_btn.png", True)

    def FindImageOnScreen(self, image, gray):
        if gray:
            image = cv.imread(image, cv.IMREAD_GRAYSCALE)
        else:
            image = cv.imread(image)
        # show self.capture.screenshot
        cv.imshow("screenshot", self.capture.screenshot)
        cv.waitKey(0)
        result = cv.matchTemplate(self.capture.screenshot, image, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        print(max_val)
        if max_val >= 0.9:
            print("Found")
        else:
            print("Not found")



        
instance = Main()





