import pyautogui
import keyboard
from time import sleep
from config import *


active = False
def change(x):
	global active
	active = False

keyboard.on_release_key(activate, change)

while True:
	if keyboard.is_pressed(activate):
		active = True
		sleep(1)

	while active:
		pyautogui.click(button=key, clicks=clicks)

	if keyboard.is_pressed(exit_key):
		exit()
