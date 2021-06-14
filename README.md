# Limonada
Limonada Smart Vending Machine Back End Python


This Git repo holds code for many open source libraries. It's broken down into the following directories (TODO)

The code was written on and designed to run on the TODO Linux Distro on a Raspberry Pi 4
Download TODO for the Raspberry Pi 4 at TODO 

You can make a bootable microSD card (8 GB or larger) on Desktop Linux using the following commands:
sudo apt-get install gddrescue xz-utils
unxz ubuntu-mate-18.04.2-beta1-desktop-armhf+raspi-ext4.img.xz
sudo ddrescue -D --force ubuntu-mate-18.04.2-beta1-desktop-armhf+raspi-ext4.img /dev/sd?

Where the ? in sd? can be determined by using the "lsblk" command to find your microSD card name.


Raspberry Pi uses the following libraries: <br>
pip3 install RPi.GPIO <br>
pip3 install pyautogui <br>
pip install python-statemachine <br>
sudo apt-get install qttools5-dev-tools <br>
pip install pyqt5-tools <br>
sudo dnf install qt5-designer <br>


We may use the following libraries if robotic voices & a Flutter API is needed> <br>
pip3 install boto3 <br>
pip3 install  <br>
pip3 install contextlib2
pip3 install urllibs
                                  
                                       
A DRAFT state machine can be found at: <br>
https://lucid.app/lucidchart/invitations/accept/inv_8e0a642b-567e-4aaa-acec-19c1edf9d852?viewport_loc=233%2C209%2C2308%2C1094%2C0_0 

The Development Enviroment was configured using VirtualEnv for the nano CLI text editior <br>
Copy .nanorc in your home (~/) directory to convert tabs to 4 spaces

Please use Style Guide: https://github.com/google/styleguide/blob/gh-pages/pyguide.md <br>
Commit message standard shall follow https://www.conventionalcommits.org/en/v1.0.0/ <br>
All documentation is self generated using https://www.python.org/dev/peps/pep-0257/ <br>
See examples and usage at https://docutils.sourceforge.io/README.html#quick-start <br>
Static type checking was done using http://mypy-lang.org/ <br>


UI
**Run:**
Running on PI/linux connected to Touch control UI screen with Audio

**PYQT:**
1.Kiosk Based App running on Pi USING qt5 framewrok, can easily be installed on the PI

Interaction with Hardware can be done via python file. 

So, UI will be sending controlling commands to the HARDWARE through the python files.

As project evolves this document will be updated.
