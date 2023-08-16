import win32gui
import win32con
import time
import const


class CheckRequired:
    def __init__(self):
        self.const = const.Const()
        self.check()

    def check(self):
        if self.CheckIfChromeBrowserIsOpen():
            chromeWindow = self.GetChromeWindow()
            if chromeWindow:
                if self.CheckIfTabOfGameIsOpen(chromeWindow):
                    print("Tab of game is open")
                    if self.CheckSizeOfChromeWindow(chromeWindow):
                        print("Size of chrome window is correct")
                    else:
                        self.prinErrorOfRequiredWindow(3)
                else:
                    self.prinErrorOfRequiredWindow(2)
            else:
                self.prinErrorOfRequiredWindow(1)
        else:
            self.prinErrorOfRequiredWindow(1)

    def prinErrorOfRequiredWindow(self, case):
        print("Error: ")
        if case == 1:
            print("Chrome browser is not open, please open it and try again")
        elif case == 2:
            print("Tab of game is not open, please open the url https://plbrault.github.io/youre-the-os/ and try again")
        elif case == 3:
            print("The resolution of the window must be 1920x1080 and the zoom must be 100%")

        exit()

    def _enumWindowsHandler(self, hwnd, windows):
        if win32gui.IsWindowVisible(hwnd):
            # windows.append( hex( hwnd ), win32gui.GetWindowText( hwnd ) )
            windows.append( (hwnd, win32gui.GetWindowText( hwnd )) )

    def CheckIfChromeBrowserIsOpen(self):
        # get all windows open

        # create a list of windows with 2 elements: hwnd and window title
        windows = []
        win32gui.EnumWindows(self._enumWindowsHandler, windows)

        # check if chrome is open
        for window in windows:
            if "chrome" in window[1].lower():
                return True
        
        return False
    
    def GetChromeWindow(self):
        # get all windows open

        # create a list of windows with 2 elements: hwnd and window title
        windows = []
        win32gui.EnumWindows(self._enumWindowsHandler, windows)

        # check if chrome is open
        for window in windows:
            if "chrome" in window[1].lower():
                # set the windows to foreground
                win32gui.SetForegroundWindow(window[0])
                time.sleep(1)
                # get handler of the chrome window
                hwnd = win32gui.GetForegroundWindow()
                # set window to normal
                win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                # set window to 640x480
                win32gui.MoveWindow(hwnd, 0, 0, 1152, 648, True)
                return window[0]
        
        return None

    def CheckIfTabOfGameIsOpen(self, chromeWindow):
        # set to foreground the chrome window
        win32gui.SetForegroundWindow(chromeWindow)

        # get the title of the chrome window
        chromeWindowTitle = win32gui.GetWindowText(chromeWindow)

        if chromeWindowTitle != self.const.WINDOW_NAME:
            return False
        
        return True

    def CheckSizeOfChromeWindow(self, chromeWindow):
        # get the size of the chrome window
        rect = win32gui.GetWindowRect(chromeWindow)

        print(rect[2] - rect[0])
        print(rect[3] - rect[1])

        if rect[2] - rect[0] != self.const.RESOLUTION[0] or rect[3] - rect[1] != self.const.RESOLUTION[1]:
            return False
        
        return True

