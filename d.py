firstname = str(input("Enter your first name: "))
lastname = str(input("Enter your last name: "))
fullname = firstname + " " + lastname
print("Hello " + fullname)
print("Your name has "+ str(len(fullname)) + " characters")
print("Your fist letter of your first name is " + firstname[0])
print("Your last letter of your last name is "+ lastname[-1])
print("Your name after slicing is "+ fullname[0:5])