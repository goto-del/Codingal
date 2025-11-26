file = open("Codingal.txt" , "r")
readun = file.read()
print(readun)
file.close()

file= open("Codingal.txt", "a")
file.write("\nYes\n")
file.write("I want to\n")
file.close()

