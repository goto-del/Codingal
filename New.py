a = input("Enter the word: ")
count = 0
for i in a:
    if i in "aeiouAEIOU":
        count = 1 + count
        
print(f"{count} vowels in the word")