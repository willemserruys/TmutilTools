import shutil
import os

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


InitialDirectory = "/Volumes/Back up/Backups.backupdb/iMac van Kurt/"
SourceLocation = "Macintosh HD/Users/kurtserruys/Pictures/Foto's-bibliotheek.photoslibrary"
SourceLocation2 = "Macintosh HD/Users/kurtserruys/Pictures/iPhoto-bibliotheek.migratedphotolibrary"
Destination = "/Volumes/INTERNAL/Photos/"

for backupName in os.listdir(InitialDirectory):
    directory = InitialDirectory + backupName + "/" + SourceLocation
    directory2 = InitialDirectory + backupName + "/" + SourceLocation2
    copytree(directory,Destination+"/"+backupName + ".photoslibrary")
    copytree(directory2,Destination + "/" + backupName + ".migratedphotolibrary")
    

