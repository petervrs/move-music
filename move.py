## This script moves all files from subdirectories in the directory in which it is run to
# this directory
# TODO: Make sure the amount of moved files is correctly calculated

import os
import shutil

amountOfFilesMoved = 0
level0SubDirectories = next(os.walk('.'))[1]
level0Files = next(os.walk("."))[2]
mainDirectory = os.getcwd()

print("Currently working in directory " + mainDirectory)
print("The following subdirectories are present: ")
print(level0SubDirectories)
print("The following files are present: ")
print(level0Files)
print("Starting to move files to main directory...\n")

currentWorkingDirectory = os.getcwd()
currentDirLevel = 0

def moveFilesToMainDirectory(path):
    subDirs = next(os.walk(path))[1]
    files = next(os.walk(path))[2]
    print("Subdirectories in " + path + ": ")
    print(subDirs)
    print("Files in " + path + ": ")
    print(files)

    if len(subDirs) > 0:
        print("There are subdirectories present")
        # For each subdirectory, call this function
        for subDir in subDirs:
            print("Moving files in subdirectories")
            moveFilesToMainDirectory(os.path.join(path, subDir))
        
    else:
        print("There are no subdirectories present")

    # Check if there are files present
    if len(files) > 0:
        # If there are files present, move each file to main directory
        print("There are files present, moving files to main directory")
        # Move files to main directory
        for file in files:
            currentFilePath = os.path.join(path, file)
            newFilePath = os.path.join(mainDirectory, file)
            print("Moving file " + currentFilePath + " to " + newFilePath)
            shutil.move(currentFilePath, newFilePath)
            global amountOfFilesMoved
            amountOfFilesMoved += 1
    else:
        print("There are no files present")

    # Step one directory back and remove directory
    os.chdir("../")
    print("Current directory: " + os.getcwd())
    print("Removing directory: " + path)
    os.rmdir(path)
    return


for directory in level0SubDirectories:
    moveFilesToMainDirectory(os.path.join(currentWorkingDirectory, directory))

print("\nFiles moved to main directory, " + str(amountOfFilesMoved) + " files were moved")