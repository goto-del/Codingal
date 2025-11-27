file1 = open("Codingal.txt", "r")
file2 = open("Updated.txt", "w")
l1 = file1.readlines()
print(l1)

for line in l1:
    if not(line.startswith('Coding')):
        print(line)
        file2.write(line)

file1.close()
file2.close()