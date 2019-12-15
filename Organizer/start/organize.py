import os
from pathlib import Path

SUBDIRECTORY = {
    "DOCUMENTS": ['.txt', '.pdf', '.xlsx'],
    "COMPRESSED": ['.zip'],
    "IMAGE": ['.jpeg'],
    "JARS": ['.jar'],
    "PYTHON": ['.py']
}


# path = 'C:/Users/rounak_goyanka/PycharmProjects/Organizer/organize/'


def pickDirectory(value):
    for category, suffixs in SUBDIRECTORY.items():
        for suffix in suffixs:
            if suffix == value:
                return category


print(pickDirectory('.pdf'))
# print(os.stat('C:/Users/rounak_goyanka/'))
# to find all files on specific location

# with os.scandir('C:/Users/rounak_goyanka/PycharmProjects/Organizer/organize/') as it:
#    for entry in it:
#        if not entry.name.startswith('.') and entry.is_file():
#            print(entry.name)
# os.close()


def organizeDirectory():
    obj = os.scandir()
    for item in obj:
        if item.is_dir():
            continue
        filePath = Path(item)
        filetype = filePath.suffix.lower()
        directory = pickDirectory(filetype)
        directoryPath = Path(directory)
        if not directoryPath.is_dir():
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))
    obj.close()


organizeDirectory()
