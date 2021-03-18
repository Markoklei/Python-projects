"""
Auxiliary functions to be used by widgets in fslookup.py.


Functions:
    sterm_fld_pressed()
    clear_current_output()
    search()
    browse_file_dialog()
    browse_folder_dialog()
    log_and_exit(err_msg)
"""


#   TODO: change documentation of functions and module to follow python conventions


import globals as g
from globals import tk

from rec_search import rec_search

import os, datetime


def sterm_fld_pressed(event):
    """Treats an event where the search term field was clicked on.

    Initially, the function will delete all current contents of the sterm field.
    For each additional click on the search term field, the function will select all current contents.

    """

    #global bool_sterm_fld_pressed   # we add this line because otherwise bool_sterm_fld_pressed is considered to be a
                                    # local function variable rather than the symbol imported from the auxiliary module
                                    # this was a bad idea since the symbol was just copied from auxiliary, the value
                                    # of this variable isn't synched between the modules
    g.sterm_fld.selection_range(0, tk.END)  # select all text
    g.sterm_fld.icursor(tk.END) # move cursor after last character
    if not g.bool_sterm_fld_pressed:    # if this is the first time the search term field is being pressed
        g.sterm_fld.delete(0, 'end')    # remove current text from entry
        g.sterm_fld.config(fg='green')
        g.bool_sterm_fld_pressed = True
        if g.chose_file_or_folder:
            g.search_button['state'] = 'normal' # enable the search button
    else:
        g.sterm_fld.selection_range(0, tk.END)  # select all text
        g.sterm_fld.icursor(tk.END)  # move cursor after last character
    return 'break'  # this is to prevent class binding from overwriting the binding we created
                    # since class binding happens after the widget binding
                    # guess it is something like 'if widget_binding || class_binding || ..'


def clear_current_output():
    """Delete all labels from previous searches from the display."""
    for label in g.curr_labels:
        label.destroy()


def search():
    """Parses data the user entered and initiates search accordingly."""
    if g.chose_file_or_folder and (g.sterm_fld.get() not in ''): #not in ['', g.DEFAULT_ENTRY_TEXT]):
        clear_current_output()
        found = []
        path = g.browse_label.cget("text").split('\t')[1]
        sterm = g.sterm_fld.get()
        path.replace('\\', '\\\\') # escape the backslashes in the path
                                   # each litreal backslash becomes two literal backslashes
        rec_search(path, sterm, found)
        for f in found: # output found files to GUI as labels' contents
            label = tk.Label(g.top,
                             text = f)
            g.curr_labels.append(label)
            label.pack()


def browse_file_dialog():
    """Treat button press on the browse file button."""
    filename = tk.filedialog.askopenfilename(initialdir = '/',
                                             #title = 'Select file/folder to begin search...',
                                             filetypes = ( ('Text files - .txt', '*.txt'),
                                                           ('Word files - .docx', '*.docx'),
                                                           ('All files', '*.*') ))
    if filename:    # check if some file was chosen
        st = 'Chose the following ' + 'file:\t' + filename
        g.browse_label.configure(text = st)
        g.chose_file_or_folder = True
        if g.bool_sterm_fld_pressed:
            g.search_button['state'] = 'normal'

def browse_folder_dialog():
    """Treat button press on the browse dialog button."""
    foldername = tk.filedialog.askdirectory()
    if foldername:  # check if some folder was chosen
        st = 'Chose the following ' + 'folder:\t' + foldername
        g.browse_label.configure(text = st)
        g.chose_file_or_folder = True
        if g.bool_sterm_fld_pressed:
            g.search_button['state'] = 'normal'


def log_and_exit(err_msg):
    """Write log message to file and notify the user of an error via a new screen/window."""
    log_file_path = os.path.join(os.environ['USERPROFILE'], g.LOG_FILE_NAME)
    with open(log_file_path, 'a') as writer:
        writer.write(err_msg)
    g.top.destroy()   # remove current widgets from view
    g.init_gui()
    err_label = tk.Label(g.top,
                   text = g.ERR_UNEXPECTED % log_file_path)
    ok_btn = tk.Button(g.top,
                       text = 'OK',
                       command = g.top.destroy)
    err_label.pack()
    ok_btn.pack()