"""
Consider this 'the GUI module' responsible for everything relating to GUI - widgets, aesthetics, ..


Functions:

    sterm_fld_pressed
    add_sterm_fld()
    add_browse_btn()
    add_search_btn()
    add_widgets()
"""


#   TODO: When we try and turn this into an executable - how do we make this module the 'main' module?

from auxiliary import *


from tkinter import filedialog  # this is a submodule that isn't loaded automatically


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
    add_browse_btn() and\
    add_search_btn():
        return


add_widgets()   # Adding widgets


# Enter the main event loop to take action against each event triggered by the user
g.top.mainloop()