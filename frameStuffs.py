from pynput import mouse
import tkinter.messagebox
from mss import mss
import numpy as np

class Frame:
    def __init__(self, top = None, right = None, bottom = None, left = None):
        self.top, self.right, self.bottom, self.left = top, right, bottom, left

        if not all([self.top, self.right, self.bottom, self.left]):
            self.getUserBoundary()

        print(f'Frame({self.top}, {self.right}, {self.bottom}, {self.left})')
        self.boundary = {'top': self.top, 'left': self.left, 'width': abs(self.left - self.right), 'height': abs(self.top - self.bottom)}
        self.sct = mss()

    def on_click(self, x, y, button, pressed):        
        if button == mouse.Button.left and pressed:
            if (self.top == None and self.left == None):
                self.top = y
                self.left = x
                print(f"TOP: {self.top} | LEFT: {self.left}")
            elif (self.bottom == None and self.right == None):
                self.bottom = y
                self.right = x
                print(f"BOTTOM: {self.bottom} | RIGHT: {self.right}")
                return False

    def getUserBoundary(self):
        tkinter.messagebox.showinfo(title="Instructions", message="After closing this messagebox: Click the top left and bottom right of the box you wish this program to screen shot and \"see\"\n")

        with mouse.Listener(on_click=self.on_click) as listener:
            listener.join()

    def grab_frame(self):
        frame = self.sct.grab(self.boundary)
        frame = np.array(frame)
        return frame
