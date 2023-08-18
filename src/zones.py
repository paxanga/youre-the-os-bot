import cv2 as cv

class Zones:
    def __init__(self):
        pass
    
    def getCPU(self, screenshot, number):
        if number == 1:
            x = 149
            y = 154
            x2 = 196
            y2 = 199
            cpu = screenshot[y:y2, x:x2]
        elif number == 2:
            x = 199
            y = 154
            x2 = 245
            y2 = 199
            cpu = screenshot[y:y2, x:x2]
        elif number == 3:
            x = 249
            y = 154
            x2 = 295
            y2 = 199
            cpu = screenshot[y:y2, x:x2]
        elif number == 4:
            x = 299
            y = 154
            x2 = 345
            y2 = 199
            cpu = screenshot[y:y2, x:x2]
        elif number == 5:
            x = 349
            y = 154
            x2 = 395
            y2 = 199
            cpu = screenshot[y:y2, x:x2]
        elif number == 6:
            x = 399
            y = 154
            x2 = 445
            y2 = 199
            cpu = screenshot[y:y2, x:x2]
        elif number == 7:
            x = 449
            y = 154
            x2 = 495
            y2 = 199
            cpu = screenshot[y:y2, x:x2]
        elif number == 8:
            x = 499
            y = 154
            x2 = 545
            y2 = 199
            cpu = screenshot[y:y2, x:x2]
        elif number == 9:
            x = 549
            y = 154
            x2 = 595
            y2 = 199
            cpu = screenshot[y:y2, x:x2]
        elif number == 10:
            x = 599
            y = 154
            x2 = 645
            y2 = 199
            cpu = screenshot[y:y2, x:x2]
        elif number == 11:
            x = 649
            y = 154
            x2 = 695
            y2 = 199
            cpu = screenshot[y:y2, x:x2]
        elif number == 12:
            x = 699
            y = 154
            x2 = 745
            y2 = 199
            cpu = screenshot[y:y2, x:x2]
        elif number == 13:
            x = 749
            y = 154
            x2 = 795
            y2 = 199
            cpu = screenshot[y:y2, x:x2]
        elif number == 14:
            x = 799
            y = 154
            x2 = 845
            y2 = 199
            cpu = screenshot[y:y2, x:x2]
        elif number == 15:
            x = 849
            y = 154
            x2 = 895
            y2 = 199
            cpu = screenshot[y:y2, x:x2]
        elif number == 16:
            x = 899
            y = 154
            x2 = 945
            y2 = 199
            cpu = screenshot[y:y2, x:x2]

        return cpu
    
    def getIOEvents(self, screenshot):
        x = 149
        y = 125
        x2 = 200
        y2 = 145

        IOevents = screenshot[y:y2, x:x2]

        return IOevents
    
    def getMemoryPages(self, screenshot):
        x = 540
        y = 230  
        x2 = 1010
        y2 = 700

        MemoryPages = screenshot[y:y2, x:x2]

        return MemoryPages
    
    def getIdleProcess(self, screenshot):
        x = 149
        y = 230
        x2 = 500
        y2 = 550

        IdleProcess = screenshot[y:y2, x:x2]

        return IdleProcess
    
    def getXAndYZone(self, zone):
        if zone == 'cpu_1':
            x = 149
            y = 154
        elif zone == 'cpu_2':
            x = 199
            y = 154
        elif zone == 'cpu_3':
            x = 249
            y = 154
        elif zone == 'cpu_4':
            x = 299
            y = 154
        elif zone == 'cpu_5':
            x = 349
            y = 154
        elif zone == 'cpu_6':
            x = 399
            y = 154
        elif zone == 'cpu_7':
            x = 449
            y = 154
        elif zone == 'cpu_8':
            x = 499
            y = 154
        elif zone == 'cpu_9':
            x = 549
            y = 154
        elif zone == 'cpu_10':
            x = 599
            y = 154
        elif zone == 'cpu_11':
            x = 649
            y = 154
        elif zone == 'cpu_12':
            x = 699
            y = 154
        elif zone == 'cpu_13':
            x = 749
            y = 154
        elif zone == 'cpu_14':
            x = 799
            y = 154
        elif zone == 'cpu_15':
            x = 849
            y = 154
        elif zone == 'cpu_16':
            x = 899
            y = 154
        elif zone == 'IOEvents':
            x = 149
            y = 125
        elif zone == 'IldeProcess':
            x = 149
            y = 230

        return (x, y)