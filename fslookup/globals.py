"""
This module defines globals for cross-module usage.

Functions:

    init_gui()


Globals:

    top

    sterm_fld
    browse_label
    browse_folder_button
    browse_file_button
    search_button

    LOG_FILE_NAME
    ERR_UNEXPECTED
    ERR_TK_MSG
    SUCCESS
    FAILURE
    DEFAULT_ENTRY_TEXT
    EVT_FOCUS

    bool_sterm_fld_pressed
    chose_file_or_folder
    curr_labels
"""

#   TODO: change documentation of functions and module to follow python conventions

import tkinter as tk

# -- top - the main GUI window --


top = None


# Create the GUI application main windows
def init_gui():
    global top  # Use the global variable top, instead of creating a local one
    top = tk.Tk()
    top.title('FSLookup')
    top.geometry("500x500")


init_gui()  # top is now initialized and can be used by other modules


# -- widgets --

sterm_fld = None
browse_label = None
browse_folder_button = None
browse_file_button = None
search_button = None


# -- constants --

LOG_FILE_NAME = 'FSLookup_log.txt'
ERR_UNEXPECTED = 'An unexpected error occurred - see log file at %s for more details.'
ERR_TK_MSG = '{failed_func} failed at {module}/{func}() - {date_time}\n'
SUCCESS = 1
FAILURE = 0
DEFAULT_ENTRY_TEXT = 'Enter your search term ...'


# -- events --

EVT_FOCUS = '<FocusIn>' # applies for left button click on mouse


# -- auxiliary variables (for cross-module usage) --
bool_sterm_fld_pressed = False
chose_file_or_folder = False
curr_labels = []