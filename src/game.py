import time
from libs import opencv
import const
import cv2 as cv
from src import zones
from libs.getkeys import key_check


class Game:
    def __init__(self, captureworker):
        self.opencv = opencv.OpenCV()
        self.const = const.Const()
        self.captureworker = captureworker
        self.zones = zones.Zones()
        self.image_levels = {
            "0": "hourglass_not_done_emoji.png",
            "1": "grinning_face_emoji.png",
            "2": "slightly_smiling_face_emoji.png",
            "3": "neutral_face_emoji.png",
            "4": "frowning_face_emoji.png",
            "5": "loudly_crying_face_emoji.png",
            "6": "cold_face_emoji.png",
            "7": "smiling_face_with_halo_emoji.png"
        }
        self.free_CPU = 0

    def StartGame(self):
        while self.captureworker.screenshot is None:
            time.sleep(1)
        # wait for game to load and click play
        while self.opencv.FindImageOnScreen(self.const.IMG_PATH + "\play_btn.png", False, self.captureworker.screenshot, 0.9, True, False) is False and self.opencv.FindImageOnScreen(self.const.IMG_PATH + "\play_again_btn.png", False, self.captureworker.screenshot, 0.9, True, False) is False:
            print("Waiting for game to load")
            time.sleep(1)

        while True:
            cpu_data = self.getCPUProcess()
            ilde_process_data = self.getIldeProcess()
            # self.getMemoryPages() TODO: fix this
            self.checkIOEvents()

            for cpu in cpu_data:
                if cpu_data[cpu]['0'] is False and cpu_data[cpu]['1'] is False and cpu_data[cpu]['2'] is False and cpu_data[cpu]['3'] is False and cpu_data[cpu]['4'] is False and cpu_data[cpu]['5'] is False and cpu_data[cpu]['6'] is False and cpu_data[cpu]['7'] is False:
                    self.free_CPU += 1

            # if cpu_data contains IOevents, delete procees from CPU
            for cpu in cpu_data:
                if cpu_data[cpu]['0'] is not False or cpu_data[cpu]['1'] is not False or cpu_data[cpu]['7'] is not False:
                    if cpu_data[cpu]['0'] is not False:
                        click_coords = cpu_data[cpu]['0']
                    elif cpu_data[cpu]['1'] is not False:
                        click_coords = cpu_data[cpu]['1']
                    elif cpu_data[cpu]['7'] is not False:
                        click_coords = cpu_data[cpu]['7']
                    self.opencv.click(click_coords[0], click_coords[1])
                    self.free_CPU += 1

            if self.free_CPU > 0:
                # foreach ilde_process_data in reverse oreder
                for level in reversed(ilde_process_data):
                    if int(level) != 0 and int(level) != 7 and int(level) != 1:
                        if ilde_process_data[level] is not False:
                            # click on coords
                            self.opencv.click(
                                ilde_process_data[level][0], ilde_process_data[level][1])
                            self.free_CPU -= 1
                            if self.free_CPU < 1:
                                break


            keys = key_check()
            if 'Q' in keys:
                print("Q pressed")
                self.captureworker.stop()
                exit()

    def checkIOEvents(self):
        # if IOevents found press space
        IOevents = self.zones.getIOEvents(self.captureworker.screenshot)

        if self.opencv.FindColorOnScreen("0x008080", IOevents, 15, False) is True:
            self.opencv.pressKey("space")

    def getIldeProcess(self):
        IDLEProcess = self.zones.getIdleProcess(self.captureworker.screenshot)

        results = {}

        for level in self.image_levels:
            res = self.opencv.FindImageOnScreen(
                self.const.IMG_PATH + "\\" + self.image_levels[level], False, IDLEProcess, 0.9, False, True)
            if res is False:
                results[level] = False
            else:
                # sum the coords of the image with the coords of the zone
                results[level] = (res[0] + self.zones.getXAndYZone('IldeProcess')[0], res[1] + self.zones.getXAndYZone('IldeProcess')[1])
                
        return results
    
    def getCPUProcess(self):
        cpu_results = {}

        for i in range(1, self.const.NUMBER_OF_CPUS + 1):
            cpu_results["cpu_" + str(i)] = self.zones.getCPU(self.captureworker.screenshot, i)

        # generate json with results in each cpu
        results = {}

        for i in range(1, self.const.NUMBER_OF_CPUS + 1):
            cpu = "cpu_" + str(i)
            results[cpu] = {}
            for level in self.image_levels:
                res = self.opencv.FindImageOnScreen(
                    self.const.IMG_PATH + "\\" + self.image_levels[level], False, cpu_results[cpu], 0.9, False, True)
                if res is False:
                    results[cpu][level] = False
                else:
                    results[cpu][level] = (res[0] + self.zones.getXAndYZone(cpu)[0], res[1] + self.zones.getXAndYZone(cpu)[1])

        return results

    def getMemoryPages(self):
        memory_pages = self.zones.getMemoryPages(self.captureworker.screenshot)

        pid_paged = self.opencv.FindColorOnScreen("0x0000FF", memory_pages, 15, True)

        if pid_paged is not False:
            pid_idle = self.opencv.FindColorOnScreen("0x63666A", memory_pages, 15, True)
            if pid_idle is not False:
                self.opencv.click(pid_idle[0], pid_idle[1])
                self.opencv.click(pid_paged[0], pid_paged[1])
        

