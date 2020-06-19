from pynput import keyboard
from pynput.keyboard import Key, Listener   
from pynput.mouse import Button, Controller

mouse = Controller() 
def on_press(key):
    try:
        print('key {0} is pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))

def on_release(key):
    print('{0} have been released'.format(key))
    position=mouse.position
    if  key == keyboard.Key.up:
            print('********')
            # mouse.move(position[0]+10,position[1])
            mouse.move(0,-10)
    if key == keyboard.Key.down:
            print('********')
            # mouse.move(position[0]+10,position[1])
            mouse.move(0,10)
    if key == keyboard.Key.left:
            print('********')
            # mouse.move(position[0]+10,position[1])
            mouse.move(-10,0)
    if key == keyboard.Key.right:
            print('********')
            # mouse.move(position[0]+10,position[1])
            mouse.move(10,0)
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect ev    ents released
with keyboard.Listener( on_press=on_press,on_release=on_release) as listener:
    listener.join() 
    posision=mouse.posision( )
    # if on_press           


           