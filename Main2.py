num = int(input("Enter a number : "))

prime = [True] * (num+1)
for i in range(2, num):
    if prime[i] == True:
        for j in range(i * 2, num + 1, i):
            prime[j] = False
print(f"Prime below {num} are ")
for i in range(2, num+1):
    if prime[i] == True:
        print(i)
