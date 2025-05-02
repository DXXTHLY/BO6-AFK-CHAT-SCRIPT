import os
import sys

# Enforce script filename
required_filename = "dscdotggslash143x.py"
if os.path.basename(__file__) != required_filename:
    print(f"[ERROR] This script must be named '{required_filename}' to run.")
    sys.exit(1)

import random
import time
import threading
import pydirectinput
import pyautogui
from pynput.keyboard import Controller, Key, Listener
from pynput.mouse import Button

keyboard = Controller()
stop_afk = False
paused = True

def on_press(key):
    global paused, stop_afk
    if key == Key.shift_r:
        paused = not paused
        print("Script paused." if paused else "Script resumed.")
    elif key == Key.esc:
        stop_afk = True
        print("Kill switch activated. Stopping script.")
        sys.exit(0)

def smooth_move_mouse(target_x, target_y, steps=100, delay=0.001):
    current_x, current_y = pyautogui.position()
    step_x = (target_x - current_x) / steps
    step_y = (target_y - current_y) / steps

    for _ in range(steps):
        if stop_afk or paused:
            break
        current_x += step_x
        current_y += step_y
        pydirectinput.moveTo(int(current_x), int(current_y))
        time.sleep(delay)

def rotate_mouse():
    screen_width, screen_height = pyautogui.size()
    center_x, center_y = screen_width // 2, screen_height // 2
    radius = min(screen_width, screen_height) // 4

    while not stop_afk:
        if paused:
            time.sleep(1)
            continue

        direction = random.choice(['positive', 'negative'])
        if direction == 'positive':
            target_x = center_x + radius * (1 + 0.5 * random.random())
        else:
            target_x = center_x - radius * (1 + 0.5 * random.random())
        target_y = center_y

        smooth_move_mouse(target_x, target_y)
        time.sleep(0.01)

def perform_sequence():
    while not stop_afk:
        if paused:
            time.sleep(1)
            continue

        actions = [
            ('w', random.uniform(0.5, 1.5)),
            ('d', random.uniform(0.5, 1.5)),
            ('q', random.uniform(0.1, 0.3)),
            ('s', random.uniform(0.5, 1.5)),
            ('a', random.uniform(0.5, 1.5)),
            ('space', random.uniform(0.1, 0.3)),
            ('e', random.uniform(0.1, 0.3)),
            ('ctrl', random.uniform(0.1, 0.3)),
            ('v', random.uniform(0.1, 0.3)),
            ('right', random.uniform(0.5, 1)),
            ('ctrl', random.uniform(0.1, 0.3)),
            ('left', random.uniform(0.3, 0.8)),
            ('r', random.uniform(0.1, 0.3)),
        ]

        for key, duration in actions:
            if stop_afk or paused:
                break

            print(f"Pressing: {key} for {duration:.2f} seconds")

            if key == 'right':
                pydirectinput.mouseDown(button='right')
                time.sleep(duration)
                pydirectinput.mouseUp(button='right')
            elif key == 'left':
                pydirectinput.mouseDown(button='left')
                time.sleep(duration)
                pydirectinput.mouseUp(button='left')
            else:
                pydirectinput.keyDown(key)
                time.sleep(duration)
                pydirectinput.keyUp(key)

            print(f"Released: {key}")
            time.sleep(random.uniform(0.5, 1.3))

def type_message_in_chat():
    global paused
    messages = [
        "I just sneezed on my keyboard 😷",
        "My goldfish is playing for me rn 🐠",
        "I'm legally required to be bad at this game",
        "My chair is haunted and it's winning",
        "Currently powered by cold pizza 🍕",
        "Anyone else lagging IRL?",
        "Is this Fortnite? Where's my hammer?",
        "They let me out of the asylum to play this match",
        "My monitor is off. How am I doing?",
        "Bro I'm gaming from the back of a moving truck",
        "My mousepad is a slice of cheese 🧀",
        "Why is my controller wet?",
        "Trying to unlock the 'pure chaos' achievement",
        "Sorry I was talking to my toaster",
        "Just blinked for 20 minutes straight",
        "I’m doing this with my elbows only",
        "My cat just clutched that round",
        "That wasn’t me. That was my sleep paralysis demon",
        "Playing from the moon with 2,000 ping 🌕",
        "Using my fridge touchscreen to game rn"
    ]
    last_message = None

    while not stop_afk:
        if paused:
            time.sleep(1)
            continue

        available_messages = [msg for msg in messages if msg != last_message]
        if not available_messages:
            available_messages = messages
        message = random.choice(available_messages)
        last_message = message

        paused = True
        time.sleep(1)

        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(0.5)
        keyboard.type(message)
        time.sleep(0.5)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(1)
        paused = False

        time.sleep(random.uniform(30, 60))

def start_afk_actions():
    global stop_afk
    stop_afk = False
    threading.Thread(target=perform_sequence, daemon=True).start()
    threading.Thread(target=rotate_mouse, daemon=True).start()
    threading.Thread(target=type_message_in_chat, daemon=True).start()
    print("AFK actions started. Press Right Shift to pause/resume, or ESC to kill.")

listener = Listener(on_press=on_press)
listener.start()

start_afk_actions()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    stop_afk = True
    print("Script stopped.")
