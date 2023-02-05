Hey! Edit the variables in the config.json.
IMPORTANT: If you are using Windows, chances are your Path looks like this:
C:\path\to\directory\
And that is fine for most Programms but for this script you are using the wrong Slash.
Your Path is supposed to look like this:
C:/path/to/directory/

To run the script you need the following variables:
pyautogui and webbrowser

Also, the time variables like "wait_after_screenshot" are measured in seconds.

You shouldn't use the PyautoGUI Failsave because the script stops working but still continues.
The PyautoGUI Failsave is activated by having the cursor in the corner of the screen wich is maybe
something you want in order to take a clean screenshot.

Also, this script does not leave the Browser Tabs open. It closes them witht he Ctrl + w shortcut.
But some Browsers close when there is no tab open. That can drastically increase wait time.
Maybe try having an empty tab open.

Also, please do not leave your mouse in the middle of the screen because it could falsify the image detection or make for a bad screenshot.
