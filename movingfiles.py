import os
import shutil
source = input("enter sources folder")
distination = input("enter distination folder")
source = source+'/'
distination = distination+'/'
listoffiles=os.listdir(source)
for file in listoffiles:
    shutil.move((source+file),distination)