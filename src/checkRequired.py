import win32gui
import win32con
import time


class CheckRequired:
    def __init__(self):
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
                        self.prinErrorOfRequiredWindow()
                else:
                    self.prinErrorOfRequiredWindow()
            else:
                self.prinErrorOfRequiredWindow()
        else:
            self.prinErrorOfRequiredWindow()

    def prinErrorOfRequiredWindow(self):
        print("Chrome browser is not open, please open it and enter in the url https://plbrault.github.io/youre-the-os/ and try again, the resolution of the window must be 1920x1080 and the zoom must be 100%")
        # exit the program
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
                # set to fullscreen
                win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
                return window[0]
        
        return None

    def CheckIfTabOfGameIsOpen(self, chromeWindow):
        # set to foreground the chrome window
        win32gui.SetForegroundWindow(chromeWindow)

        # get the title of the chrome window
        chromeWindowTitle = win32gui.GetWindowText(chromeWindow)

        if chromeWindowTitle != "You're the OS! - Google Chrome":
            return False
        
        return True

    def GetSizeOfChromeWindow(self, chromeWindow):
        # get the size of the chrome window
        rect = win32gui.GetWindowRect(chromeWindow)
        width = rect[2] - rect[0]
        height = rect[3] - rect[1]
        return (width, height)
    
    def CheckSizeOfChromeWindow(self, chromeWindow):
        # size must be (1938, 1038)
        size = self.GetSizeOfChromeWindow(chromeWindow)
        print(size)
        if size[0] != 1938 or size[1] != 1038:
            return False
        
        return True

