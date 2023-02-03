import os
from fnmatch import fnmatch
# default directory as current directory
root = os.path.dirname(os.path.realpath(__file__))


def isImage(filename):
    if filename.endswith("bmp") or filename.endswith("jpg") or filename.endswith("jpeg"):
        return True
    return False


def isDirectory(filename):
    listOfFileNames = os.listdir(filename)
    completeFileList = list()
    for fname in listOfFileNames:
        fullPath = os.path.join(filename, fname)
        if os.path.isdir(fullPath):
            completeFileList = completeFileList + isDirectory(fullPath)
        elif isImage(fname):
            filelist.append(fname)
    return completeFileList


filelist = list()
isDirectory(root)
# print(filelist)
for filename in filelist:
    print(filename)

