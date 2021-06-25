# Limonada
Limonada Smart Vending Machine <br>

IP address for JMAR Raspberry Pi on ethernet is 192.168.1.60 <br>
IP address for UCC Raspberry Pi on Wifi network 76Spectrum5G at the shop is 192.168.0.30 <br>
IP address for UCC Raspberry Pi on Wifi network NETGEAR89 at Blaze's home is 192.168.1.24 <br>

This Git repo holds code for many open source libraries. It's broken down into the following directories (Limonada-Backend, Limonada-UI, LimonadaPiServer, HTML, LimonadaDevEnv, and FUTURE_WORK). <br>

Limonada-Backend: Python files to make kioks speak and control low level hardware functions like restarting and GPIO pin control. <br>

Limonada-UI: <br>
Operator GUI: A QTPY application running on MacOS using qt5 framewrok <br>
Kiosk GUI: HTML5 and CSS iplaod to the JMAR CMS to render touchscreen buttons, images, date selectors, and text boxes.  

Interaction with hardware is done via python file and Node.js server over LAN TCP or UDP <br> <br>

HTML: Images and DRAFT layout files for Limonada-UI (see above) to run on www.vend4you.com (mixed HTML, CSS,and Javascript) <br>

LimonadaDevEnv: Files created by the "VirtualEnv" library to keep Limonada pip installs separate from the rest our MacOS or Linux development enviroment. Code doesnt support Windows :) <br>

Raspberry Pi uses the following libraries: <br>
pip3 install simpleaudio <br>
pip3 install RPi.GPIO <br>

We might use the following libraries: <br>
pip3 install pyautogui <br>
pip3 install flask <br>
pip install python-statemachine <br>
sudo apt-get install qttools5-dev-tools <br>
pip install pyqt5-tools <br>
sudo dnf install qt5-designer <br>

We may use the following libraries if robotic voices & a Flutter API is needed for v2 <br>
pip3 install boto3 <br>
pip3 install contextlib2 <br>
pip3 install urllibs <br>
                                  
The code was written on and designed to run on the TODO Linux Distro on a Raspberry Pi 4 <br>

The best way to make a bootable OS for the Raspberry is to use their GUI application called "Raspberry Pi Imager" at https://www.raspberrypi.org/software/ <br>

The hardcore CLI way ianto download "Raspberry OS" for the Raspberry Pi 4 at  https://www.raspberrypi.org/software/operating-systems/ <br>

You can make a bootable microSD card (8 GB or larger) on Desktop Linux using the following commands: <br>
sudo apt-get install gddrescue xz-utils <br>
unxz OS.img.xz <br>
sudo ddrescue -D --force OS.img /dev/sd? <br>

Where the "?" in sd? can be determined by using the "lsblk" command to find your microSD card name. <br>

A DRAFT state machine can be found at: <br>
https://lucid.app/lucidchart/invitations/accept/inv_8e0a642b-567e-4aaa-acec-19c1edf9d852?viewport_loc=233%2C209%2C2308%2C1094%2C0_0  <br>

The Development Enviroment was configured using VirtualEnv for the nano CLI text editior <br>
Copy .nanorc in your home (~/) directory to convert tabs to 4 spaces. <br>

Please use Style Guide: https://github.com/google/styleguide/blob/gh-pages/pyguide.md <br>
Commit message standard shall follow https://www.conventionalcommits.org/en/v1.0.0/ <br>
All documentation is self generated using https://www.python.org/dev/peps/pep-0257/ <br>
See examples and usage at https://docutils.sourceforge.io/README.html#quick-start <br>
Static type checking was done using http://mypy-lang.org/ <br>

Operator GUI:
A QTPY application running on MacOS using qt5 framewrok <br>

Interaction with hardware is done via python file and Node.js server over LAN TCP or UDP <br>