#Screenshot-Searcher

A simple Python script that opens a random URL, waits for it to load, and takes a screenshot if it's not an error page.
##Prerequisites

    Python 3.x
    PyAutoGUI library
    JSON library
    Webbrowser library
    Time library

##How to use

    Go to the [Releases]([url](https://github.com/Darkylt/Screenshot-Searcher/releases)) page and download the latest release.
    Unpack the ZIP File and install the following Library:
    
    ###PyAutoGUI
    `pip install pyautogui`

    After that you can execute the main.py file with Python.
    The Reccomended way to do this is to go into the Command Prompt and navigate to the Folder where the main.py script is located
    and to run the following command:
    `python main.py`
    
##Variables in config.json file

    **output_dir:** The directory where the screenshots will be saved.
    **failsafe_shortcut:** A keyboard shortcut to stop the script (for example, ctrl+q).
    **wait_after_screenshot:** The time in seconds to wait after taking a screenshot before opening a new URL.
    **wait_for_page_load:** The time in seconds to wait for a page to load before taking a screenshot.
    **image_detection_confidence:** The confidence level for image detection (0.0 to 1.0).
    **pyautogui_failsave:** The fail-safe setting for PyAutoGUI.

##Built With

    [Python 3.x]([url](https://www.python.org/downloads/))
    [PyAutoGUI library]([url](https://pypi.org/project/PyAutoGUI/))
    [JSON library]([url](https://docs.python.org/3/library/json.html))
    [Webbrowser library]([url](https://docs.python.org/3/library/webbrowser.html))
    [Time library]([url](https://docs.python.org/3/library/time.html))
