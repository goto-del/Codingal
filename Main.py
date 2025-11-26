f = open("example.txt", "w")
f.write("Hello World!\n")
f.write("This is a Python program\n")
f.write("Powered By Visual Studio Code (VS Code)\n")
f.close()



f = open("example.txt", "a")
f.write("POWERED BY ANDROID LAPTOPS.\n")
f.write("This is the Python program I have done today.\n")
f.close()

f = open("example.txt", "r")
content = f.read()
print(content)
f.close()