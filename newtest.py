# Version 3.0.1
import time, datetime
#import numpy as np
#import cv2
import win32api, win32con
#from PIL import ImageGrab, Image
#import threading


def writeLog(info):
    print(info)
    current_time = datetime.datetime.now()
    log = open('display_test.log', 'a')
    log.write(current_time.strftime("%Y-%m-%d %H:%M:%S"))
    log.write("  %s \n" % info)
    log.close()


class Component:
    def __init__(self):
        self.xCoord = 0
        self.yCoord = 0

    def setCoord(self, x, y):
        self.xCoord = x
        self.yCoord = y

    def setMouseCoord(self, info):
        print(info)
      #  raw_input()
        self.xCoord, self.yCoord = win32api.GetCursorPos()

    def getX(self):
        return self.xCoord

    def getY(self):
        return self.yCoord

class Camera(Component):

    def dragAndDrop(self, display):
        x1 = self.getX()
        y1 = self.getY()
        x2 = display.getX()
        y2 = display.getY()

        win32api.SetCursorPos((x1, y1))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x1, y1, 0, 0)
        time.sleep(1)
        win32api.SetCursorPos((x2, y2))
        time.sleep(1)
        win32api.SetCursorPos((x2 + 10, y2 + 10))
        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x2, y2, 0, 0)
        time.sleep(1)

class Dispalay(Component):

    def __init__(self):
        self.x1Position = 0
        self.y1Position = 0
        self.x2Position = 0
        self.y2osition = 0
        self.disconnectCoord = 0
        self.width = 0
        self.height = 0

    def clickDisconnect(self):
        x1 = self.disconnect.getX()
        y1 = self.disconnect.getY()
        win32api.SetCursorPos((x1, y1))
        time.sleep(0.25)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x1, y1, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x1, y1, 0, 0)

