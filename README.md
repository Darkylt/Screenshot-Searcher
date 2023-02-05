# Project Title

Ever wanted to see random screenshots?

## Description

A simple Python script that opens a random Screenshot on prntscr.com, waits for it to load, and takes a screenshot if it's not an error page.

## Getting Started

### Dependencies

* Windows 10
* [Python 3.x]([https://www.python.org/downloads/])
* [PyAutoGUI library]([https://pypi.org/project/PyAutoGUI/])
* [JSON library]([https://docs.python.org/3/library/json.html])
* [Webbrowser library]([https://docs.python.org/3/library/webbrowser.html])
* T[ime library]([https://docs.python.org/3/library/time.html])

### Installing

* Got to the [Releases]([https://github.com/Darkylt/Screenshot-Searcher/releases]) and download the SS.zip File.
* Unpack it and install the PyAutoGUI Library. To do that you can just run:
```
pip install pyautogui
```
* Open the config.json file and input the Path to the Folder where the Screenshots should be saved.
* Play around with the Timings to fit your Computer. The Time is measured in seconds.

### Executing program

* Open the command prompt and navigate to the Folder where the main.py file is located.
* Run the following command:
```
python main.py
```
* To stop the script hit Ctrl + q or close the Console.

## Help

The Script closes the Tab automatically after taking a Screenshot.
But some Browsers close when no Tab is open.
I recommend to always have an empty Tab open to make sure this doesn't happen.

The Failsave Ctrl + q may not work on every machine.
I recommend to just close the Console instead.
minique Pizzie  

## Version History
* Next Update:
    * Detection system for detecting if a screenshot is fully visible and to Zoom out if it isn't.
* 0.2
    * Added image detection to detect Invalid URL's.
* 0.1
    * Basic script that doesn't check for invalid URL's.

## License

It's not Licensed in any way and no one will sue you if you use it.
