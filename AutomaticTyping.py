# I request the users to please keep atleast one tab in google chrome open so that the program can work smoothly. :)

from platform import python_branch
import pyautogui
screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
pyautogui.hotkey('ctrl','alt','c')
pyautogui.moveTo(300,50)
pyautogui.click()
pyautogui.write('https://web.whatsapp.com/')
pyautogui.press('enter')
pyautogui.hotkey('ctrl','t')
pyautogui.write('https://code.whitehatjr.com/s/dashboard')
pyautogui.press('enter')
pyautogui.moveTo(300,300)
