import pyautogui
import keyboard
from time import sleep
from config import *

def start():
	while True:
		pyautogui.click(button=key, clicks=clicks)
		if keyboard.is_pressed(desactivate):
			return

while True:
	if keyboard.is_pressed(activate):
		sleep(1)
		start()
		sleep(1)
	elif keyboard.is_pressed(exit): exit()