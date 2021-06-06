from platform import python_branch
import pyautogui
screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
pyautogui.moveTo(800, 1100) # Move the mouse to XY coordinates.
pyautogui.click()
pyautogui.hotkey('ctrl','t')
pyautogui.moveTo(300,50)
pyautogui.click()
pyautogui.write('https://web.whatsapp.com/')
pyautogui.press('enter')
