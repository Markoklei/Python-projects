from os import walk
from os.path import isfile, isdir, join, splitext

import docx


SUPPORTED_EXTENSIONS = ['.txt', '.docx']


"""assumes <path> points to a .txt file and searches it for <sterm>.
Returns True if file contains <sterm>, false otherwise."""
def open_search_txt(path, sterm):
    with open(path) as reader:
        if sterm in reader.read():
            return True
    return False


"""assumes <path> points to a .docx file and searches it for <sterm>.
 Returns True if file contains <sterm>, false otherwise."""
def open_search_docx(path, sterm):
    doc = docx.Document(path)
    for para in doc.paragraphs:
        if sterm in para.text:
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

if __name__ == '__main__':
    found = []
    TESTING_PATH = r"C:\Users\Mark\Desktop\Testing fslookup"
    STERM = "testing"
    rec_search(TESTING_PATH, STERM, found)
    print("called rec_search, found is : ", found)
