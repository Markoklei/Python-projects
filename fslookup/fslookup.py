"""
Consider this 'the GUI module' responsible for everything relating to GUI - widgets, aesthetics, ..


Functions:

    sterm_fld_pressed
    add_sterm_fld()
    add_checkbox_btn()
    add_browse_btn()
    add_search_btn()
    add_widgets()
"""


"""To turn this code into an executable, I used the pyinstaller utility, with the command 'pyinstaller --onefile
    fslookup.py'. However, this is slow on startup - you can use just 'pyinstaller fslookup.py', but then you have
    to execute fslookup.exe from the folder that was created.
    Either way, when opening fslookup.exe, a cmd windows pops up. A batch file can be created, silently launching
    fslookup.exe, and a shortcut called fslookup.exe can be used to point to this batch file.
"""

from auxiliary import *


from tkinter import filedialog  # this is a submodule that isn't loaded automatically


def add_sterm_fld():
    """Adds a search term field."""
    g.sterm_fld = tk.Entry(g.top,
                           width=31,
                           justify='center')    # text alignment, entry is centered by default
    if not g.sterm_fld:
        log_and_exit(g.ERR_TK_MSG.format(failed_func='tk.Entry',
                                         module='fslookup',
                                         func='add_sterm_fld',
                                         date_time=str(datetime.datetime.now())))
        return g.FAILURE
    g.sterm_fld.insert(0, g.DEFAULT_ENTRY_TEXT)   # Add default text
    g.sterm_fld.config(fg='grey')
    g.sterm_fld.bind(g.EVT_FOCUS, sterm_fld_pressed)    # define what happens when field is clicked on
    g.sterm_fld.pack()
    return g.SUCCESS


def add_checkbox_btn():
    """The user can make the search case-insensitive by checking this box."""
    g.case_checkbox = tk.Checkbutton(g.top,
                                     text='Make the search case insensitive',
                                     variable=g.checkbox_variable)
    if not g.case_checkbox:
        log_and_exit(g.ERR_TK_MSG.format(failed_func='tk.Checkbutton',
                                         module='fslookup',
                                         func='add_checkbox_btn',
                                         date_time=str(datetime.datetime.now())))
        return g.FAILURE

    g.case_checkbox.pack()
    return g.SUCCESS


def add_browse_btn():
    """Adds two browse buttons - one for selecting a folder, one for selecting a file."""
    g.browse_label = tk.Label(g.top,
                            text = 'Choose file/folder to begin search...')
    if not g.browse_label:
        log_and_exit(g.ERR_TK_MSG.format(failed_func='tk.Label',
                                         module='fslookup',
                                         func='add_browse_btn',
                                         date_time=str(datetime.datetime.now())))
        return g.FAILURE
    g.browse_folder_button = tk.Button(g.top,
                         text = 'Browse folders',
                         command = browse_folder_dialog)
    g.browse_file_button = tk.Button(g.top,
                                   text = 'Browse files',
                                   command = browse_file_dialog)
    if not g.browse_folder_button or not g.browse_file_button:
        log_and_exit(g.ERR_TK_MSG.format(failed_func='tk.Button',
                                         module='fslookup',
                                         func='add_browse_btn',
                                         date_time=str(datetime.datetime.now())))
        return g.FAILURE

    g.browse_label.pack()
    g.browse_folder_button.pack()
    g.browse_file_button.pack()
    return g.SUCCESS


def add_search_btn():
    """Add an execution button, a search button.
    Initially disabled until text and place to search were given."""
    g.search_button = tk.Button(g.top,
                                text='SEARCH',
                                command=search)
    if not g.search_button:
        log_and_exit(g.ERR_TK_MSG.format(failed_func='tk.Button',
                                         module='fslookup',
                                         func='add_search_btn',
                                         date_time=str(datetime.datetime.now())))
        return g.FAILURE

    g.search_button['state'] = 'disabled'   # user must first select search term and location to search
    g.search_button.pack()
    return g.SUCCESS


def add_widgets():
    #   the condition is just to make sure that there were no failures while adding some widget
    #   if, say, the add_sterm_fld function failed, we don't want to run add_browse_btn
    if add_sterm_fld() and\
    add_checkbox_btn() and\
    add_browse_btn() and\
    add_search_btn():
        return


add_widgets()   # Adding widgets


# Enter the main event loop to take action against each event triggered by the user
g.top.mainloop()