"""
ALPINE NETWORK CONFIGURATION SCREEN Application
- Reads user network configuration data from multiple .txt files then allows user to edit and writes back updated data
to .txt files

Created by: Nadeem Abdelkader on 11/4/2022
Last updated by Nadeem Abdelkader on 11/4/2022

GUI framework = Tkinter

This file contains the helper function to be called from main.py
"""

# importing the necessary libraries for working with json
import json
import os
from tkinter import Frame, Label, Entry, X, LEFT, RIGHT, YES, messagebox, Button, Tk, TOP

# declaring the constants to be used everywhere in the module
FIELDS_1 = ['KEYMAPOPTS', 'HOSTNAMEOPTS', 'INTERFACESOPTS', 'DNSOPTS', 'TIMEZONEOPTS', 'PROXYOPTS',
            'APKREPOSOPTS', 'SSHDOPTS', 'NTPOPTS', 'DISKOPTS', 'LBUOPTS', 'APKCACHEOPTS']

FIELDS_2 = ['iface', 'inet', 'address', 'netmask', 'gateway', 'domain', 'nameserver', 'hostname']

DISPlAY_FIELDS = ['Interface', 'Internet Networking', 'IP address', 'Netmask', 'Gateway', 'Domain', 'Name Servers',
                  'Host Name']

INPUT_DIR = "/Users/nadeem/Documents/Khwarizm/Alpine/alpine-network-config/input_dir/"
OUTPUT_DIR = "/Users/nadeem/Documents/Khwarizm/Alpine/alpine-network-config/output_dir/"

MANUAL = True

data_dict_1 = {
    FIELDS_1[0]: None,
    FIELDS_1[1]: None,
    FIELDS_1[2]: None,
    FIELDS_1[3]: None,
    FIELDS_1[4]: None,
    FIELDS_1[5]: None,
    FIELDS_1[6]: None,
    FIELDS_1[7]: None,
    FIELDS_1[8]: None,
    FIELDS_1[9]: None,
    FIELDS_1[10]: None,
    FIELDS_1[11]: None,
}

data_dict_2 = {
    FIELDS_2[0]: None,
    FIELDS_2[1]: None,
    FIELDS_2[2]: None,
    FIELDS_2[3]: None,
    FIELDS_2[4]: None,
    FIELDS_2[5]: None,
    FIELDS_2[6]: [],
    FIELDS_2[7]: None
}


def write_answers_txt():
    cont = True
    # for i in range(len((entries))):
    #     if entries[FIELDS[i]].get() == "":
    #         cont = False
    #         txt_result.config(
    #             text="Please complete the required field!", fg="red")
    # if entries[FIELDS[3]].get() != entries[FIELDS[4]].get():
    #     cont = False
    #     txt_result.config(text="Passwords do not match!", fg="red")

    if cont:
        dict = read_to_dict_1("input_dir/answers.txt")
        #
        # users_list = []
        # if os.path.exists(USERS_FILENAME) and os.stat(USERS_FILENAME).st_size != 0:
        #     users_list = read_from_json(USERS_FILENAME)
        #     users_list.append(dict)
        # else:
        #     users_list.append(dict)

        # print(dict)

        # filename = str(entries[FIELDS_1[0]].get()).replace(" ", "") + ".json"
        # filename = "/Users/nadeem/Documents/Khwarizm/Alpine/alpine-install/records/" + filename
        filename = OUTPUT_DIR + "answers.txt"
        # with open(filename,
        #           "w") as write_file:  # change "w" to "a" if you want to append instead of overwrite
        #     json.dump(dict, write_file, indent=4)
        comments = ["# Example answer file for setup-alpine script\n"
                    "# If you don't want to use a certain option, then comment it out\n\n"
                    "# Use US layout with US variant\n",
                    "\n# Set hostname to alpine-test\n",
                    "\n# Contents of /etc/network/interfaces\n",
                    "\n# Search domain of example.com, Google public nameserver\n",
                    "\n# Set timezone to UTC\n",
                    "\n# set http/ftp proxy\n",
                    "\n# Add a random mirror\n",
                    "\n# Install Openssh\n",
                    "\n# Use openntpd\n",
                    "\n# Use /dev/sda as a data disk\n",
                    "\n# Setup in /media/sdb1\n"
                    ]
        with open(filename, 'w') as file:
            for i in range(len(FIELDS_1)):
                if i < len(comments):
                    file.write(comments[i])
                if i == 1:
                    file.write(FIELDS_1[i] + "=\"-n " + dict[FIELDS_1[i]] + "\"")
                elif i == 3:
                    file.write(FIELDS_1[i] + "=\"-d " + dict[FIELDS_1[i]] + "\"")
                elif i == 4:
                    file.write(FIELDS_1[i] + "=\"-z " + dict[FIELDS_1[i]] + "\"")
                elif i == 6:
                    file.write(FIELDS_1[i] + "=\"-r" + dict[FIELDS_1[i]] + "\"")
                elif i == 7:
                    file.write(FIELDS_1[i] + "=\"-c " + dict[FIELDS_1[i]] + "\"")
                elif i == 8:
                    file.write(FIELDS_1[i] + "=\"-c " + dict[FIELDS_1[i]] + "\"")
                elif i == 9:
                    file.write(FIELDS_1[i] + "=\"-m " + dict[FIELDS_1[i]] + "\"")
                else:
                    file.write(FIELDS_1[i] + "=\"" + dict[FIELDS_1[i]] + "\"")
                file.write("\n")
            file.write("\n")
    return


def read_to_dict_1(filename):
    """
    This function reads data from a txt file to a dictionary
    :param filename: file to read from
    :return: dictionary contining read data
    """
    f = open(filename, 'r')
    f = f.read()
    f = f.split('\"')
    for i in range(len(f)):
        for j in range(len(FIELDS_1)):
            if f[i].endswith(FIELDS_1[j] + "="):
                if f[i + 1].startswith("-"):
                    data_dict_1[FIELDS_1[j]] = f[i + 1][3:]
                else:
                    data_dict_1[FIELDS_1[j]] = f[i + 1]
    return data_dict_1


def read_to_dict_2():
    """
    This function reads data from a txt file to a dictionary
    :param filename: file to read from
    :return: dictionary contining read data
    """
    filename = "input_dir/interfaces.txt"
    if filename == "input_dir/interfaces.txt":
        f = open(filename, 'r')
        f = f.read()
        f = f.replace('\n', ' ')
        f = f.split(' ')
        # print(f)
        for i in range(len(f)):
            for j in range(len(FIELDS_2)):
                if f[i] == FIELDS_2[j]:
                    data_dict_2[FIELDS_2[j]] = f[i + 1]
    filename = "input_dir/resolve.txt"
    if filename == "input_dir/resolve.txt":
        f = open(filename, 'r')
        f = f.read()
        f = f.replace('\n', ' ')
        f = f.split(' ')
        f = list(filter(None, f))
        f = list(filter(bool, f))
        f = list(filter(len, f))
        f = list(filter(lambda item: item, f))
        # print(f)
        for i in range(len(f)):
            for j in range(len(FIELDS_2)):
                if f[i] == FIELDS_2[j]:
                    if FIELDS_2[j] == 'nameserver':
                        data_dict_2[FIELDS_2[j]].append(str(f[i + 1]))
                    else:
                        data_dict_2[FIELDS_2[j]] = f[i + 1]
    filename = "input_dir/host.txt"
    if filename == "input_dir/host.txt":
        f = open(filename, 'r')
        f = f.read()
        f = f.replace("\n", "")
        f = f.split("           ")
        # print(f)
        for i in range(len(f)):
            for j in range(len(FIELDS_2)):
                if f[i] == FIELDS_2[j]:
                    data_dict_2[FIELDS_2[j]] = f[i + 1]
    # TEMPORARY
    # data_dict_2['hostname'] = "myhost"
    return data_dict_2


# data1 = read_to_dict_1("input_dir/answers.txt")
# print(data1)


# data2 = read_to_dict_2()
# print(data2)


def read_txt_to_lst(filename):
    """
    This function reads the data from .txt file to a list
    :param filename: txt file to read from
    :return: list containing the data
    """
    mylines = []
    # of = open(filename, 'rt')
    # s = of.readlines()
    # print(s)
    with open(filename, 'rt') as myfile:
        for myline in myfile:
            # print(myline)
            if myline.startswith(FIELDS_2[0]) or myline.startswith(FIELDS_2[1]) or myline.startswith(
                    FIELDS_2[2]) or \
                    myline.startswith(FIELDS_2[3]) or myline.startswith(FIELDS_2[4]) or myline.startswith(FIELDS_2[5]) \
                    or myline.startswith(FIELDS_2[6]) or myline.startswith(FIELDS_2[7]) or \
                    myline.startswith(FIELDS_2[8]) or myline.startswith(FIELDS_2[9]) or \
                    myline.startswith(FIELDS_2[10]) or \
                    myline.startswith(FIELDS_2[11]):
                start = myline.find("\"")
                end = myline.rfind("\"")
                # print(myline[start+1:end])
                if myline[start + 1:end].startswith("-"):
                    mylines.append(myline[start + 4:end])
                else:
                    mylines.append(myline[start + 1:end])
    return mylines


def make_form(root, fields):
    """
    This function created the actual GUI form using Tkinter Entry, Label, and Frames
    :param root: root Tkinter window
    :param fields: array of strings that include the field names to createb the form according to
    :return: an array of Tkinter entries
    """
    makeLabel(root)
    entries = {}
    i = 0
    # data = read_txt_to_lst("answers.txt")
    data = read_to_dict_2()
    # print(data)
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=22, text=DISPlAY_FIELDS[i] + ": ", anchor='w')
        if field == "Password" or field == "Re-enter Password":
            ent = Entry(row, show="*")
        else:
            ent = Entry(row)
            if type(data[field]) != list and data[field].startswith("-"):
                # print(data[field][3:])
                ent.insert(0, data[field][3:])
            else:
                if type(data[field]) == list:
                    for j in data[field]:
                        # print(data[field])
                        ent.insert(0, j + ", ")
                else:
                    ent.insert(0, data[field])
        ent.insert(0, "")
        if MANUAL:
            row.pack(side=TOP, fill=X, padx=25, pady=5)
            lab.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=YES, fill=X)
        else:
            if field in ['hostname', 'domain', 'nameserver']:
                row.pack(side=TOP, fill=X, padx=25, pady=5)
                lab.pack(side=LEFT)
                ent.pack(side=RIGHT, expand=YES, fill=X)
        entries[field] = ent
        i += 1
    return entries


def read(ents):
    """
    This function re reads data from .txt file and re populates the entries
    :param ents: entries to re populate
    :return: void
    """
    # data = read_txt_to_lst("answers.txt")

    data = read_to_dict_2()
    for i in range(len(FIELDS_2)):
        ents[FIELDS_2[i]].delete(0, 'end')
        if FIELDS_2[i] == 'nameserver':
            # data[FIELDS_2[i]] = data[FIELDS_2[i]].replace(" ", "")
            # data[FIELDS_2[i]] = data[FIELDS_2[i]].split(",")
            # data[FIELDS_2[i]] = data[FIELDS_2[i]][::-1]
            data[FIELDS_2[i]] = list(dict.fromkeys(data[FIELDS_2[i]]))
            for j in data[FIELDS_2[i]]:
                ents[FIELDS_2[i]].insert(0, j + ", ")
        else:
            if data[FIELDS_2[i]].startswith("-"):
                ents[FIELDS_2[i]].insert(0, data[FIELDS_2[i]][3:])
            else:
                ents[FIELDS_2[i]].insert(0, data[FIELDS_2[i]])
    txt_result.config(text="Successfully read data!", fg="green")
    return


def makeLabel(root):
    """
    This function adds the GUI heading
    :param root: root Tkinter window
    :return: void
    """
    txt_title = Label(root, width=0, font=(
        'arial', 24), text="Khwarizm Consulting")
    txt_title.pack(side=TOP, padx=5, pady=5)
    return


# def read_from_json(filename):
#     """
#     This function reads the previous users data from a .json file that can contain 0 or more json objects
#     (stored as an array of json objects)
#     :param filename: file to get the records from
#     :return: an array of json objects
#     """
#     input_file = open(filename)
#     json_array = json.load(input_file)
#     user_list = []
#
#     for user in json_array:
#         user_details = {FIELDS[0]: None, FIELDS[1]: None, FIELDS[2]: None, FIELDS[3]: None,
#                         FIELDS[4]: None, FIELDS[5]: None, FIELDS[6]: None, FIELDS[7]: None,
#                         FIELDS[8]: None, FIELDS[9]: None, FIELDS[10]: None, FIELDS[0]: user[FIELDS[0]],
#                         FIELDS[1]: user[FIELDS[1]], FIELDS[2]: user[FIELDS[2]],
#                         FIELDS[3]: user[FIELDS[3]], FIELDS[4]: user[FIELDS[4]],
#                         FIELDS[5]: user[FIELDS[5]], FIELDS[6]: user[FIELDS[6]],
#                         FIELDS[7]: user[FIELDS[7]], FIELDS[8]: user[FIELDS[8]],
#                         FIELDS[9]: user[FIELDS[9]], FIELDS[10]: user[FIELDS[10]]}
#
#         user_list.append(user_details)
#
#     return user_list


def submit(entries):
    """
    This function is executed when the user fills in all the inforamtion and clicks submit.
    It takes all the entered information an writes it to a .json file (users.json)
    :param entries: an array of entries that contain the entered information
    :return: void
    """
    cont = True
    # for i in range(len((entries))):
    #     if entries[FIELDS[i]].get() == "":
    #         cont = False
    #         txt_result.config(
    #             text="Please complete the required field!", fg="red")
    # if entries[FIELDS[3]].get() != entries[FIELDS[4]].get():
    #     cont = False
    #     txt_result.config(text="Passwords do not match!", fg="red")

    if cont:
        dict = {}
        for i in range(len(entries)):
            dict[FIELDS_2[i]] = entries[FIELDS_2[i]].get()
        #
        # users_list = []
        # if os.path.exists(USERS_FILENAME) and os.stat(USERS_FILENAME).st_size != 0:
        #     users_list = read_from_json(USERS_FILENAME)
        #     users_list.append(dict)
        # else:
        #     users_list.append(dict)

        # print(dict)

        # interfaces_file = str(entries[FIELDS_2[0]].get()).replace(" ", "") + ".json"
        interfaces_file = OUTPUT_DIR + "interfaces.txt"
        resolve_file = OUTPUT_DIR + "resolve.txt"
        host_file = OUTPUT_DIR + "host.txt"

        # with open(filename,
        #           "w") as write_file:  # change "w" to "a" if you want to append instead of overwrite
        #     json.dump(dict, write_file, indent=4)
        interfaces_file = open(interfaces_file, 'w')
        resolve_file = open(resolve_file, 'w')
        host_file = open(host_file, 'w')
        for i in range(len(FIELDS_2)):
            if FIELDS_2[i] in ['iface', 'inet', 'address', 'netmask', 'gateway']:
                if i >= 1:
                    interfaces_file.write(FIELDS_2[i] + " " + dict[FIELDS_2[i]] + "\n")
                else:
                    interfaces_file.write(FIELDS_2[i] + " " + dict[FIELDS_2[i]] + " ")
            if FIELDS_2[i] in ['domain', 'nameserver']:
                if FIELDS_2[i] == 'domain':
                    resolve_file.write(FIELDS_2[i] + "           " + dict[FIELDS_2[i]] + "\n")
                if FIELDS_2[i] == 'nameserver':
                    dict[FIELDS_2[i]] = dict[FIELDS_2[i]].replace(" ", "")
                    dict[FIELDS_2[i]] = dict[FIELDS_2[i]].split(",")
                    dict[FIELDS_2[i]] = dict[FIELDS_2[i]][::-1]
                    for j in dict[FIELDS_2[i]]:
                        # print(j)
                        if j != "":
                            resolve_file.write(FIELDS_2[i] + "       " + j + "\n")
            if FIELDS_2[i] == 'hostname':
                host_file.write(FIELDS_2[i] + "           " + dict[FIELDS_2[i]] + "\n")

        # interfaces_file.write("\n")
        # resolve_file.write("\n")
        # host_file.write("\n")

        # jsonString = json.dumps(users_list, indent=4)
        # jsonFile = open(USERS_FILENAME, "w")
        # jsonFile.write(jsonString)
        # jsonFile.close()
        write_answers_txt()
        txt_result.config(text="Successfully submitted data!", fg="green")

        clear(entries, True)

    """
    After submitting
    
    Enable and run dbus for GUI
    
    # rc-service dbus start
    # rc-update add dbus
    
    Enable and run lxdm
    
    # rc-service lxdm start
    # rc-update add lxdm
    
    import os

    cmd = 'rc-service dbus start'
    os.system(cmd)
    
    cmd = 'rc-update add dbus'
    os.system(cmd)
    
    cmd = 'rc-service lxdm start'
    os.system(cmd)
    
    cmd = 'rc-update add lxdm'
    os.system(cmd)
    """
    return


def clear(entries, on_submit=False):
    """
    This function is executed when the users clicks the "clear" button.
    It resets the entire form
    :param entries: an array of entries to clear
    :return: void
    """
    for i in range(len(FIELDS_2)):
        entries[FIELDS_2[i]].delete(0, 'end')
    if not on_submit:
        txt_result.config(text="Cleared form!", fg="green")
    return


def quit():
    """
    This function is executed when the users clicks the "quit" button.
    It quits the entire application
    :return: void
    """
    result = messagebox.askquestion(
        'Khwarizm Consulting', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
    return


def text_alert():
    """
    This function creates the label where we will later add some alerts to the user like
    "please complete the required field" or "Submitted data successfully"
    :return: void
    """
    global txt_result
    txt_result = Label(root)
    txt_result.pack()
    return


def create_buttons():
    """
    This function creates 3 buttons (submit, clear, and quit) and associates them with the appropriate methods
    :return: void
    """
    top = Frame(root)
    top.pack(side=TOP)
    submit_button = Button(root, text="Submit", command=(lambda e=ents: submit(e)))
    read_button = Button(root, text="Read", command=(lambda e=ents: read(e)))
    clear_button = Button(root, text="Clear", command=(lambda e=ents: clear(e)))
    quit_button = Button(root, text="Quit", command=quit)
    submit_button.pack(in_=top, side=LEFT)
    read_button.pack(in_=top, side=LEFT)
    clear_button.pack(in_=top, side=LEFT)
    quit_button.pack(in_=top, side=LEFT)
    return


def initialise_window():
    """
    This function initialises the Tkinter GUI window
    :return: root Tkinter window
    """
    global root, ents
    root = Tk()
    ents = make_form(root, FIELDS_2)
    root.geometry("800x600")
    root.title("Khwarizm Consulting")
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    return root


# calling function to initialise the GUI window
root = initialise_window()
