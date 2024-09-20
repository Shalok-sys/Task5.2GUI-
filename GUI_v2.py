from tkinter import *
import tkinter.font
from gpiozero import PWMLED
import RPi.GPIO

RPi.GPIO.setmode(RPi.GPIO.BOARD)

red_led = PWMLED(17)
green_led = PWMLED(27)
blue_led = PWMLED(22)

win = Tk()
win.title("RGB GUI")
win.geometry('1200x400')
win.configure(bg="lightblue")
myFont = tkinter.font.Font(family='Helvetica', size=20, weight="bold")

def close():
    RPi.GPIO.cleanup()
    win.destroy()

def sliderCheck(val):
    if val == 1:
        red_led.value = int(redledSlider.get()) / 255
        greenledSlider.set(0)
        blueledSlider.set(0)
        allSlider.set(0)
    elif val == 2:
        green_led.value = int(greenledSlider.get()) / 255
        redledSlider.set(0)
        blueledSlider.set(0)
        allSlider.set(0)
    elif val == 3:
        blue_led.value = int(blueledSlider.get()) / 255
        greenledSlider.set(0)
        redledSlider.set(0)
        allSlider.set(0)
    elif val == 4:
        greenledSlider.set(0)
        blueledSlider.set(0)
        redledSlider.set(0)
        red_led.value = int(allSlider.get()) / 255
        green_led.value = int(allSlider.get()) / 255
        blue_led.value = int(allSlider.get()) / 255

redledSlider = Scale(win, from_=0, to=255, orient=HORIZONTAL, length=200, bg='red', label="Red LED",command=lambda val: sliderCheck(1))
redledSlider.place(x=5, y=5)

greenledSlider = Scale(win, from_=0, to=255, orient=HORIZONTAL, length=200, bg='green', label="Green LED", command=lambda val: sliderCheck(2))
greenledSlider.place(x=5, y=100)

blueledSlider = Scale(win, from_=0, to=255, orient=HORIZONTAL, length=200, bg='blue', label="Blue LED", command=lambda val: sliderCheck(3))
blueledSlider.place(x=5, y=200)

allSlider = Scale(win, from_=0, to=255, orient=HORIZONTAL, length=200, bg='white', label="Common Slider", command=lambda val: sliderCheck(4))
allSlider.place(x=5, y=300)

exitButton = Button(win, text = "Exit", font = myFont, command = close, bg = 'yellow', height = 1, width = 10)
exitButton.place(x=500,y=0)

win.protocol("WM_DELETE_WINDOW", close)
win.mainloop()
