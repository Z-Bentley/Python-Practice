import send2trash
import os
import time
from pathlib import Path

p = Path('C:/Users/ztben/workspace/Help/Notes')

def clearContents(subpath):
    try:
        files = list(subpath.glob('*.md'))
        # print(f'found {len(files)} in {subpath}')
    except Exception as e:
        print(f"error: {e}")
        return

    for f in files:
        # time.sleep(1)
        try:
            with open(f, 'r') as file:
                fileContents = file.read()
                    
                if fileContents == '':
                    file.close()
                    try:
                        send2trash.send2trash(f)
                        print('DELETED: ' + str(f))
                    except Exception as e:
                        print(f"error trying to delete {f}: {e}")
        except:
                print(f"Could not read {f}")

clearContents(p)
    
def processFolder(pathGiven):
    print(pathGiven)
    for foldername, subfolders, filenames in os.walk(pathGiven):
        folderPath = Path(foldername)
        clearContents(folderPath)

        for subfolder in subfolders:
            subFolderPath = folderPath /  subfolder
            clearContents(subFolderPath)

processFolder(p)