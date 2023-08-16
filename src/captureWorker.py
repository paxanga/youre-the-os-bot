import threading
import time
from libs.windowcapture import WindowCapture
import gc


class CaptureWorker(threading.Thread):
    def __init__(self, src_window):
        threading.Thread.__init__(self)
        self.wincap = WindowCapture(src_window)
        self.stopped = False
        self.screenshot = None
        self.paused = False
        self.memory_clean = False

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def stop(self):
        self.stopped = True

    def run(self):
        while self.stopped is False:
            if self.paused is True:
                if self.memory_clean is True:
                    gc.collect()
                    self.memory_clean = False
                time.sleep(0.5)
                continue
            # Capture screenshot
            try:
                self.memory_clean = True
                self.screenshot = self.wincap.get_screenshotBrowser()
            except Exception as e:
                # print('Warn getting screenshot CaptureWorker')
                continue
            # time.sleep(0.2)
