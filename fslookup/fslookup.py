import tkinter as tk

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


#   - Add a path field


#   - Add an execution button


#   - Code for the previous button

# Enter the main event loop to take action against each event triggered by the user
top.mainloop()