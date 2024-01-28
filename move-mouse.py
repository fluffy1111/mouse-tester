import mouse
import pyautogui
    # getting the position of the mouse
pos = mouse.get_position()
print(pos)
    # moveing the mouse
pyautogui.move(-150, -150, duration = 1.0)

    # clicking the mouse
#mouse.click('left')
#mouse.click('right')
#mouse.click('middle')

    # scroling the mouse
mouse.wheel(5)
#mouse.wheel(-3)