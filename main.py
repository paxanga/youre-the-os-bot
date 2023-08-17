from src import checkRequired
from src import captureWorker
from src import game
import const

class Main:
    def __init__(self):
        self.const = const.Const()
        self.game = None
        self.captureWorker = None
        self.main()

    def main(self):
        if checkRequired.CheckRequired():
            print("All required are ok")
            self.captureWorker = captureWorker.CaptureWorker(
                self.const.WINDOW_NAME)
            self.captureWorker.start()
            self.game = game.Game(self.captureWorker)
            self.game.StartGame()


instance = Main()
