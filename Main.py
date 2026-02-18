def powerset(arr):
    result = [[]]
    for i in arr:
        newset = []
        for s in result:
            newset.append(s+[i])
        result = result+newset
    return result

n = int(input("How many numbers : "))

arr = []
for i in range(n):
    num = int(input("ENTER THE NUMBER WHICH YOU WANT TO ADD IN THE LIST : "))
    arr.append(num)

ps = powerset(arr)      
print(f"The Powerset of the array is .")
for i in ps:
    print(i)