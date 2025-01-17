import os #module/file to help with working with files in os.
from pathlib import Path #using a class from module pathlib.

#create a dictionary with lists containging file types.
#dict has 4 items. each item has a list w/ 3 values.
subdirectories = {
    "documents":[".pdf", ".rtf", ".txt"],
    "audios": [".m4a", ".m4b", ".mp3"],
    "videos": [".mov", ".avi", ".mp4"],
    "images": [".jpg", ".jpeg", ".png"]
}

#is the below an embedded for loop version in python?????
#learn how a for loop is used to traverse through a dic w/ lists.
def pickDirectory(fileType): #takes in a string & decides which direc to put it in.
    for c, s in subdirectories.items(): #c is for dic, s for list
        if fileType in s:
            return c #directory name.    
    return "misc" 

print(pickDirectory(".mov"))

def organizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        fileType = filePath.suffix.lower()
        directory = pickDirectory(fileType)
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

organizeDirectory()