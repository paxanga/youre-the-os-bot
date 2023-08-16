from src import checkRequired


class Main:
    def __init__(self):
        self.main()

    def main(self):
        if checkRequired.CheckRequired():
            print("All required are ok")

        
instance = Main()





