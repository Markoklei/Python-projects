from os import walk
from os.path import isfile, isdir, join, splitext


SUPPORTED_EXTENSIONS = ['.txt']


"""function assumes <path> points to a .txt file and searches it for <sterm>.
Returns True if file contains <sterm>, false otherwise."""
def open_search_txt(path, sterm):
    pass


SEARCH_FUNCTIONS = [open_search_txt]


"""function assumes path is pointing to a file, checks file's extension and tries to open it if extension is supported.
Returns True if file contains <sterm>, false otherwise. If file extension is not supported, return False."""
def contains (path, sterm):
    fname, fextension = splitext(path)
    for i, ext in enumerate(SUPPORTED_EXTENSIONS):
        if ext == fextension:
            SEARCH_FUNCTIONS[i](path, sterm)




"""traverses directory tree starting at <curr_path>, searching for files containing <sterm>
and adding them to <found>."""
def rec_search (curr_path, sterm, found):
    if isfile(curr_path) and contains(curr_path, sterm):
        found.append(curr_path)

    # I considered using an else clause after isfile, since everything in a FS is either file or folder, but if path doesn't exist
    # in the sense that there is no such file/directory, then we  would get false on the if clause and think it is a directory
    if isdir(curr_path):
        _, subdirs, fs = next(walk(curr_path))
        for obj in fs.extend(subdirs):
            rec_search(join(curr_path, obj), sterm, found)

