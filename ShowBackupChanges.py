import os
import subprocess
from subprocess import call

InitialDirectory = "/Volumes/Back up/Backups.backupdb/iMac van Kurt/"
OutputFolder = "/Users/willemserruys/Desktop/Backups/"
ImportantDirectories = ["Users/kurtserruys/Pictures","Users/kurtserruys/Documents"]
timeStamp = "2017-04-22-100909"

BackupImages = []
Comparisons = []


class BackupImage:
    def __init__(self,timeStamp):
        self.TimeStamp = timeStamp
        self.importantDirectories = []
        for dire in ImportantDirectories:
            self.importantDirectories.append(InitialDirectory + timeStamp + "/Macintosh HD/" + dire)

class Comparison:
    def __init__(self, sourceBackup, destBackup):
        self.SourceBackup = sourceBackup
        self.DestBackup = destBackup
        self.OutputFileDir = OutputFolder + sourceBackup.TimeStamp + "-" + destBackup.TimeStamp
        self.DirNames = []

        for impDir in ImportantDirectories:
            self.DirNames.append(self.OutputFileDir + "/" + impDir.split("/")[len(impDir.split("/"))-1]+'.txt')
                                 
            
        

for backupName in os.listdir(InitialDirectory):
    BackupImages.append(BackupImage(backupName))

for i  in range (0,len(BackupImages)-1):
    Comparisons.append(Comparison(BackupImages[i],BackupImages[i+1]))

print(len(BackupImages))
print(len(Comparisons))

for comp in Comparisons:
    if not os.path.exists(comp.OutputFileDir):
            os.makedirs(comp.OutputFileDir)
    for i in range(0,len(ImportantDirectories)-1):
        command = 'tmutil compare "{}" "{}" > "{}"'.format(comp.SourceBackup.importantDirectories[i],comp.DestBackup.importantDirectories[i],comp.DirNames[i])
        test = subprocess.Popen(command, shell= True, stderr=subprocess.PIPE)
        output = test.communicate()
        print(output)

            




                    
