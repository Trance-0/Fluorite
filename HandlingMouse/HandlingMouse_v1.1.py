from pynput import keyboard
from pynput.keyboard import Key, Listener   
from pynput.mouse import Button, Controller

up=False
down=False
left=False
right=False

mouse = Controller() 
def on_press(key):
    try:
        print('key {0} is pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))

def on_release(key):
    print('{0} have been released'.format(key))
    position=mouse.position
    if  key != keyboard.Key.up:
        up=False
    if key != keyboard.Key.down:
        down=False
    if key != keyboard.Key.left:
        left=False
    if key != keyboard.Key.right:
        right=False
    if key != keyboard.Key.f13:
        mouse.press(Button.left)
        mouse.release(Button.left)
    if key != keyboard.Key.f15:
        mouse.press(Button.right)
        mouse.release(Button.right)
    if key != keyboard.Key.esc:
        # Stop listener
        return False

# Collect events released
with keyboard.Listener( on_press=on_press,on_release=on_release) as listener:
    listener.join() 
    # if on_press           

while True:
    if up:
        mouse.move(0,-10)
    if down:
        mouse.move(0,10)
    if left:
        mouse.move(-10,0)
    if right:
        mouse.move(10,0)
           