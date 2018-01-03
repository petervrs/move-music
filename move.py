## Main goal:
# Everything should be placed in one big directory

import os
import shutil

level0SubDirectories = next(os.walk('.'))[1]
level0Files = next(os.walk("."))[2]
mainDirectory = os.getcwd()

print("Currently working in directory " + mainDirectory)
print("The following subdirectories are present: ", level0SubDirectories)
print("The following files are present: ", level0Files)
print("Starting to move files to main directory...")

# [x[0] for x in os.walk(os.getcwd())]

# print(x[0] for x in os.walk(directory))
# Note: keep a counter which stores the amount of subdirectories from
# the main directory in which we are currently working
currentWorkingDirectory = os.getcwd()
currentDirLevel = 0

## Make a recursive function
def moveFilesToMainDirectory(path):
    subDirs = next(os.walk(path))[1]
    files = next(os.walk(path))[2]
    print("Subdirectories in ", path, ": ", subDirs)
    print("Files in ", path, ": ", files)

    if len(subDirs) > 0:
        print("There are subdirectories")
        # For each subdirectory, call this function
    else:
        print("There are no subdirectories")
        # Check if there are files present
        if len(files) > 0:
            # Move files to main directory
            for file in files:
                currentFilePath = os.path.join(path, file)
                newFilePath = os.path.join(mainDirectory, file)
                shutil.move(currentFilePath, newFilePath)
        else:
            # Step one directory back and remove directory
            os.chdir("../")
            print("Current directory: ", os.getcwd())
            # NOTE: we can assume we have no files in this directory I guess?
            os.rmdir(path)
    return

moveFilesToMainDirectory(os.path.join(currentWorkingDirectory, level0SubDirectories[0]))

# Call testFunction for each subdirectory of the main directory
