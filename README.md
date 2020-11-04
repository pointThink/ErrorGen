# Description
ErrorGen is a program written in python 3.8 designed to create fake error messages
Now you can skip online class beacuse of "computer problems" yay!

<img src="screenshots/screenshot.png" alt="hello there">

# Creating executable from source code
For this you will need:

Python (obviously)

PyInstaller (install with: pip install pyinstaller)

ttkthemes (install with: pip install ttkthemes)


Once you have met the requierments:

Open your terminal

Change directory to the src folder

Enter command: pyinstaller -F -i icon.ico errorgen.pyw

The executable should appear in the dist folder

P.S Make sure the blank.ico file is in the same folder as the executable
