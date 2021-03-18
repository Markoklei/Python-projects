"""
This module contains the rec_search function, containing the file system searching logic.
This module also includes rec_search's auxiliary methods. These methods are for internal use.


Globals:

    SUPPORTED_EXTENSIONS
    SEARCH_FUNCTIONS


Functions:

    open_search_txt(path, sterm)
    open_search_docx(path, sterm)
    contains(path,sterm)
    rec_search(curr_path, sterm, found)
"""


from os import walk
from os.path import isfile, isdir, join, splitext

import docx

import re

# from globals import checkbox_variable   # this is bad - the value of checkbox_variable will be loaded initially
                                        # as this module is loading, and will not be synched with its value in globals
import globals as g # instead, do this and reference g.checkbox_variable


SUPPORTED_EXTENSIONS = ['.txt', '.docx']


"""assumes <path> points to a .txt file and searches it for <sterm>.
Returns True if file contains <sterm>, false otherwise."""
def open_search_txt(path, sterm):
    with open(path) as reader:
        data = reader.read()
        if (sterm in data)\
                or (g.checkbox_variable.get() and re.search(sterm, data, re.IGNORECASE)): # search is case insensitive
            return True
    return False


"""assumes <path> points to a .docx file and searches it for <sterm>.
 Returns True if file contains <sterm>, false otherwise."""
def open_search_docx(path, sterm):
    doc = docx.Document(path)
    for para in doc.paragraphs:
        if (sterm in para.text)\
                or (g.checkbox_variable.get() and re.search(sterm, para.text, re.IGNORECASE)): # search is case insensitive
            return True
    return False


SEARCH_FUNCTIONS = [open_search_txt, open_search_docx]


"""assumes path is pointing to a file, checks file's extension and tries to open it if extension is supported.
Returns True if file contains <sterm>, false otherwise. If file extension is not supported, return False."""
def contains (path, sterm):
    fname, fextension = splitext(path)
    if fextension in SUPPORTED_EXTENSIONS:
        return SEARCH_FUNCTIONS[SUPPORTED_EXTENSIONS.index(fextension)](path, sterm)
    return False




"""traverses directory tree starting at <curr_path>, searching for files containing <sterm>
and adding them to <found>."""
def rec_search (curr_path, sterm, found):
    if isfile(curr_path) and contains(curr_path, sterm):
        found.append(curr_path)

    # I considered using an else clause after isfile, since everything in a FS is either file or folder, but if path doesn't exist
    # in the sense that there is no such file/directory, then we  would get false on the if clause and think it is a directory
    if isdir(curr_path):
        _, subdirs, fs = next(walk(curr_path))
        fs.extend(subdirs)  # subdirs can't be None, so no need for 'subdirs or []'
        for obj in fs:  # fs now contains the names of files and folders in the current directory
            rec_search(join(curr_path, obj), sterm, found)



# Testing the functionality of this module's methods.
if __name__ == '__main__':
    found = []
    TESTING_PATH = r"C:\Users\Mark\Desktop\Testing fslookup"
    STERM = "testing"
    rec_search(TESTING_PATH, STERM, found)
    print("called rec_search, found is : ", found)
