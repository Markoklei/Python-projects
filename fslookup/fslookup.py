from tkinter import filedialog  # this is a submodule that isn't loaded automatically
import tkinter as tk
import os

# Create the GUI application main windows
top = tk.Tk()
top.title('FSlookup')
top.geometry("500x500")


# Adding widgets

#   - Add a search term field
#   TODO:   When you click the text field, it should select everything.
#   TODO:   Change foreground and background to make it look like a standard application.
#   TODO:   Change dimensions of the text field to take up the entire screen.
sterm_fld = tk.Entry(top)
sterm_fld.insert(0, 'Enter your search term ...')   # Add default text
sterm_fld.pack()


#   - Add a path selection button
def browse_dialog():
    filename = tk.filedialog.askopenfilename(initialdir = '/',
                                             title = 'Select file/folder to begin search...',
                                             filetypes = ( ('Text files - .txt', '*.txt'),
                                                           ('Word files - .docx', '*.docx'),
                                                           ('All files', '*.*') ))

    st = 'Chose the following ' + ('folder:\t' if os.path.isdir(filename) else 'file:\t') + filename
    browse_label.configure(text = st)

browse_label = tk.Label(top,
                        text = 'Choose file/folder to begin search...')
path_fld = tk.Button(top,
                     text = 'Browse',
                     command = browse_dialog)
browse_label.pack()
path_fld.pack()

#   - Add an execution button


#   - Code for the previous button

# Enter the main event loop to take action against each event triggered by the user
top.mainloop()