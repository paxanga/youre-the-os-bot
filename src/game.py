import time
from libs import opencv
import const
import cv2 as cv

class Game:
    def __init__(self, captureworker):
        self.opencv = opencv.OpenCV()
        self.const = const.Const()
        self.captureworker = captureworker

    def StartGame(self):
        while self.captureworker.screenshot is None:
            time.sleep(1)
        # wait for game to load and click play
        # while self.opencv.FindImageOnScreen(self.const.IMG_PATH + "\play_btn.png", False, self.captureworker.screenshot, 0.9, True) is False:
        #     time.sleep(1)

        while True:
            cpu_data = self.getCPUProcess()
            ilde_process_data = self.getIldeProcess()
            print(cpu_data)
            print(ilde_process_data)
            # cv.imshow("screenshot DEBUG", image)
            # cv.waitKey(0)
            self.captureworker.stop()
            exit()


        
    def getCPUProcess(self):
        x = 149
        y = 154
        x2 = 344
        y2 = 199

        cropped = self.captureworker.screenshot[y:y2, x:x2]

        cpu_1 = cropped[0:45, 0:49]
        cpu_2 = cropped[0:45, 49:98]
        cpu_3 = cropped[0:45, 98:147]
        cpu_4 = cropped[0:45, 147:196]

        image_levels = {
            "0": "hourglass_not_done_emoji.png",
            "1": "grinning_face_emoji.png",
            "2": "slightly_smiling_face_emoji.png",
            "3": "neutral_face_emoji.png",
            "4": "frowning_face_emoji.png",
            "5": "loudly_crying_face_emoji.png",
            "6": "cold_face_emoji.png",
        }

        # generate json with results in each cpu
        results = {}

        for i in range(1, 5):
            cpu = "cpu_" + str(i)
            results[cpu] = {}
            for level in image_levels:
                results[cpu][level] = self.opencv.FindImageOnScreen(self.const.IMG_PATH + "\\" + image_levels[level], False, eval("cpu_" + str(i)), 0.9, False)

        return results
    
    def checkIOEvents(self):
        # if IOevents found press space
    
    def getIldeProcess(self):
        x = 149
        y = 154
        x2 = 344
        y2 = 199