file = open("Codingal.txt", "r")
print(file.read())
file.close()

file = open("Codingal.txt", "w")
file.write("Hello, My name is Elias\n")
file.write("I am 10 years old\n")
file.close()

file = open("Codingal.txt", "a")
file.write("Haha\n")
file.write(" !! HACKED !!\n")
file.close()