from tkinter import filedialog  # this is a submodule that isn't loaded automatically
import tkinter as tk
import os

from rec_search import rec_search

#   TODO:   Move code to functions with informative names
#   TODO:   Change visual placement of widgets
#   TODO:   Scan for vulnerabilities

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
chose_file_or_folder = False

def browse_file_dialog():
    global chose_file_or_folder
    filename = tk.filedialog.askopenfilename(initialdir = '/',
                                             title = 'Select file/folder to begin search...',
                                             filetypes = ( ('Text files - .txt', '*.txt'),
                                                           ('Word files - .docx', '*.docx'),
                                                           ('All files', '*.*') ))
    if filename:    # check if some file was chosen
        st = 'Chose the following ' + 'file:\t' + filename
        browse_label.configure(text = st)
        chose_file_or_folder = True

def browse_folder_dialog():
    global chose_file_or_folder
    foldername = tk.filedialog.askdirectory()
    if foldername:  # check if some folder was chosen
        st = 'Chose the following ' + 'folder:\t' + foldername
        browse_label.configure(text = st)
        chose_file_or_folder = True

browse_label = tk.Label(top,
                        text = 'Choose file/folder to begin search...')
browse_folder_button = tk.Button(top,
                     text = 'Browse folders',
                     command = browse_folder_dialog)
browse_file_button = tk.Button(top,
                               text = 'Browse files',
                               command = browse_file_dialog)

browse_label.pack()
browse_folder_button.pack()
browse_file_button.pack()

#   - Add an execution button
def search():
    if chose_file_or_folder:
        found = []
        path = browse_label.cget("text").split('\t')[1]
        sterm = sterm_fld.get()
        print("The path is %s\nThe sterm is %s" % (path, sterm))
        path.replace('\\', '\\\\') # escape the backslashes in the path
                                   # each litreal backslash becomes two literal backslashes
        rec_search(path, sterm, found)
        for f in found: # output found files to GUI as labels' contents
            label = tk.Label(top,
                             text = f)
            label.pack()




search_button = tk.Button(top,
                          text = 'SEARCH',
                          command = search)

search_button.pack()

# Enter the main event loop to take action against each event triggered by the user
top.mainloop()