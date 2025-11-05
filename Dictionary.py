s1 = {"Name":"John" , "Age":25 , "City":"New York"}
s2 = {"Name":"Anna" , "Age":22 , "City":"London"}
s3 = {"Name":"Elias" , "Age":10 , "City":"Delhi"}
print(s1)
print(s1["Age"])

s3["DOB"]="27/8/2015"
print(s3)
s1.pop("Age")
print(s1)
s2.clear()
print(s2)
for i in s3.values():
    print(i)
for i in s3.keys():
    print(i)