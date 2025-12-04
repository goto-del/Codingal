with open("Codingal.txt") as f:
    data1 = f.read()

with open("sample_doc.txt") as f:
    data2 = f.read()

data1 = data1+"\n"
data2 = data1+data2

with open("Merge.txt", "w") as f:
    f.write(data2)