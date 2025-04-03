print("Marks obtained in 5 subjects")
Eng = int(input("Enter the value"))
Maths = int(input("Enter the value"))
Hindi = int(input("Enter the value"))
EVS = int(input("Enter the value"))

tot = Eng + Maths + Hindi + EVS
avg  = tot / 4

if(avg >= 91 and avg <= 100):
    print("Your grade is A+")
elif(avg >= 81 and avg <= 90):
    print("Your grade is A")
elif(avg >= 71 and avg <= 80):
    print("Your grade is B+")
elif(avg >= 61 and avg <= 70):
    print("Your grade is B")
elif(avg >= 51 and avg <= 60):
    print("Your grade is C+")
elif(avg >= 41 and avg <= 50):
    print("Your grade is C")
else:
    print("You have failed and either got a D+ , D , F+ , F(U for unsatifactory)")