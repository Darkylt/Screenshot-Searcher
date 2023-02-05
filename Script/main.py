import random
import string
import webbrowser
import time
import pyautogui
import os
import json

#HEY! Change Variables in config.json file.

script_dir = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(script_dir, 'config.json')

#Loads the Variables from the config file.
with open(config_file_path, 'r') as f:
    config = json.load(f)

output_dir = config['output_dir']
failsafe_shortcut = '+'.join(config['failsafe_shortcut'])
sleep_time = config['wait_after_screenshot']
wait_time = config['wait_for_page_load']
confidence = config['image_detection_confidence']
pyautogui_failsave = config['pyautogui_failsave']


def generate_random_string():
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for _ in range(7))

pyautogui.FAILSAFE = pyautogui_failsave

def check_image(image_path):
    try:
        location = pyautogui.locateOnScreen(image_path, grayscale=False, confidence=confidence)
        return location
    except:
        return None

def close_tab():
    return pyautogui.hotkey("ctrl", "w")  # Close the current tab

screenshot_dir = output_dir

running = True

while running:

    if pyautogui.hotkey(*failsafe_shortcut.split('+')): # A Failsave that stops the script if ctrl + q is pressed.
        running = False

    generated_string = generate_random_string()
    generated_url = "https://prnt.sc/" + generated_string
    webbrowser.open(generated_url)

    # Wait for the page to load
    time.sleep(wait_time)

    # Check if the images are displayed on the screen
    image_filename_1 = "screenshot_removed.png"
    image_path_1 = image_path = os.path.join(script_dir + "/images/" + image_filename_1)
    image_location_1 = check_image(image_path_1)

    image_filename_2 = "start.png"
    image_path_2 = image_path = os.path.join(script_dir + "/images/" + image_filename_2)
    image_location_2 = check_image(image_path_2)

    image_filename_3 = "can_not_load.png"
    image_path_3 = image_path = os.path.join(script_dir + "/images/" + image_filename_3)
    image_location_3 = check_image(image_path_3)

    image_filename_4 = "not_available.png"
    image_path_4 = image_path = os.path.join(script_dir + "/images/" + image_filename_4)
    image_location_4 = check_image(image_path_4)

    if image_location_1 or image_location_2 or image_location_3 or image_location_4:
        # One of the images was found on screen
        print("Invalid URL, generating a new one.")
        close_tab()
    else:
        # Images were not found on screen
        screenshot_path = screenshot_dir + "{}.png".format(generated_string)
        screenshot = pyautogui.screenshot()
        screenshot.save(screenshot_path)
        print("Made a Screenshot of:", generated_url)
        close_tab()

    # Wait 2 seconds before repeating the script
    time.sleep(sleep_time)
