import os
from pathlib import Path

def main():
    while True:
        toRename = []
        oldNames = {}
        try:
            path = input("Enter the path : ")
            fileToChangeName = input("Enter the name you want : ")
            actualExt = (input("Which type (.mp3/.txt/etc..) you want to rename in this repository ? ")).lower()
            numberToStart = int(input("Number to start : "))
            files = os.listdir(path)
            for filename in files:
                if Path(filename).suffix == actualExt:
                    toRename.append(filename)
            for file in toRename:
                try:
                    name = "{}{:02}{}".format(fileToChangeName, numberToStart, actualExt)
                    os.rename(os.path.join(path, file),
                              os.path.join(path, name))
                    oldNames[name] = file
                    numberToStart+=1
                except Exception as e:
                    print("Error for filename {}".format(file))
                    print(e)
        except Exception as e:
            print("Error" + str(e))
            return 0
        print("File renamed")
        try:
            backup = input("Backup (Y/n) ? ")
            if backup.lower() == "y":
                files = os.listdir(path)
                for file in files:
                    os.rename(os.path.join(path, file),
                              os.path.join(path, oldNames[file]))
                print("Backup set")
        except Exception as e:
            print(e)
        anotherFile = input("Do you want to Rename another(s) file(s) ? (Y/n)")
        if anotherFile.lower() == "n":
            break
        else:
            continue
    os.system("pause")

if __name__ == "__main__":
    main()
