# setup.py
from distutils.core import setup
import urllib.request

files = [
    ('https://example.com/file1.txt', 'file1.txt'),
    ('https://example.com/file2.txt', 'file2.txt')
]

for url, filename in files:
    urllib.request.urlretrieve(url, filename)

setup(
    name='Modules',
    version='1.0',
    py_modules=['pyautogui', 'webbrowser']
)
