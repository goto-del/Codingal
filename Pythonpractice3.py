tree1 = 98
tree2 = 102
tree3 = 234
tree4 = 345
tree5 = 984

#To find the total we have to plus

sum = tree1+tree2+tree3+tree4+tree5
average = sum/5

print("Hence all of the trees total number is",sum)
print("Hence all of the trees total average is",average)


badge = 0
print("badge =",badge)

Amount = int(input("Please enter the Amount for withdraw :"))

note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10
note_4 = (((Amount%100)%50)%10)//1

print("Notes of 100 rupees" , note_1)
print("Notes of 50 rupees" , note_2)
print("Notes of 10 rupees" , note_3)
print("Notes of 1 rupees" , note_4)

print("Enter marks obtained in 5 subjects:")
CA = int(input("CA :"))
Hindi = int(input("Hindi :"))
Evs = int(input("Evs :"))
English = int(input("English :"))
maths = int(input("maths :"))

sum = CA+Hindi+Evs+English+maths
print("Sum of CA,Hindi,Evs,English,maths:")

perc = (sum/220)*100

print("Percantage marks =",perc)
