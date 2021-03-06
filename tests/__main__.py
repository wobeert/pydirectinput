import time

import pydirectinput


def trace_square():
    # trace a box with the mouse movement
    pydirectinput.moveTo(300, 300)
    time.sleep(1)
    pydirectinput.moveTo(400, 300)
    time.sleep(1)
    pydirectinput.moveTo(400, 400)
    time.sleep(1)
    pydirectinput.moveTo(300, 400)
    time.sleep(1)
    pydirectinput.moveTo(300, 300)


def mouse_return_accuracy():
    # when the mouse is moved relative, and then reversed relative again, confirm 
    # that the cursor returns to the same position
    pydirectinput.moveTo(300, 300)
    time.sleep(1)
    pydirectinput.move(100, 0)
    time.sleep(1)
    pydirectinput.move(-100, 0)


def clicks_and_typing():
    pydirectinput.moveTo(500, 300)
    time.sleep(1)
    pydirectinput.click(500, 400)
    pydirectinput.keyDown('g')
    time.sleep(0.05)
    pydirectinput.keyUp('g')
    time.sleep(0.05)
    pydirectinput.press(['c','v','t'])
    time.sleep(0.05)
    pydirectinput.typewrite('myword')


def wasd_movement():
    pydirectinput.keyDown('w')
    time.sleep(1)
    pydirectinput.keyUp('w')
    time.sleep(1)
    pydirectinput.keyDown('d')
    time.sleep(0.25)
    pydirectinput.keyUp('d')
    time.sleep(1)
    pydirectinput.move(300, None)


def basic_click():
    pydirectinput.click()



if __name__ == '__main__':
    
    #time.sleep(4)
    #trace_square()
    #time.sleep(1)
    #mouse_return_accuracy()
    #time.sleep(1)
    #clicks_and_typing()

    time.sleep(6)
    wasd_movement()
    time.sleep(1)
    basic_click()

    
    

