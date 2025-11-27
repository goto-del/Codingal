file=open("Codingal.txt", "r")
print(file.read())
file.close()

file=open("Codingal.txt", "r")
print(file.read(500))
file.close()

file=open("Codingal.txt", "a")
file.write("My name is : Elias Moncy\n")
file.write("My age is : 10\n")
file.close()