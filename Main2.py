newfile = open('New.txt', 'w')
newfile.close()
import os

print("CHECKING IF THE FILE EXIST...")

if os.path.exists("Codingal.txt"):
    print("FILE EXISTS")
else:
    print("FILE DOES NOT EXIST")



if os.path.exists("New.txt"):
    os.remove("New.txt")
else:
    print("FILE DOES NOT EXIST")