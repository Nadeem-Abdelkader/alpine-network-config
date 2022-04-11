"""
ALPINE NETWORK CONFIGURATION SCREEN Application
- Reads user network configuration data from multiple .txt files then allows user to edit and writes back updated data
to .txt files

Created by: Nadeem Abdelkader on 11/4/2022
Last updated by Nadeem Abdelkader on 11/4/2022

GUI framework = Tkinter
"""

# !/usr/bin/env python3

# importing the helper functions from functions.py
from functions import text_alert, create_buttons, root

"""
On Startup

Enable and run dbus for GUI

# rc-service dbus start
# rc-update add dbus

Disable lxdm - replace with our script

# rc-service lxdm stop
# rc-update remove lxdm

import os

cmd = 'rc-service dbus start'
os.system(cmd)

cmd = 'rc-update add dbus'
os.system(cmd)

cmd = 'rc-service lxdm stop'
os.system(cmd)

cmd = 'rc-update remove lxdm'
os.system(cmd)

"""

if __name__ == '__main__':
    """
    Calling the helper functions from functions.py to start and run the application
    """
    text_alert()
    create_buttons()
    root.mainloop()
