with open ("Codingal.txt", "r") as file:
    data = file.readlines()
    print("The words of the file are ")
    for lines in data:
        word = lines.split()
        print(word)

        for i in word:
            print(i)