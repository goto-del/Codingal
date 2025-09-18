import matplotlib.pyplot as plt

names = ["Anna", "Elias", "Ramesh", "John", "Maria", "Xiao", "Ayesha", "Sven", "Shirin", "Shiny"]
marks = [50, 50, 38, 45, 29, 47, 18, 46, 25, 19]
percantage = []

for x in marks:
    res = (x / 50) * 100
    percantage.append(res)

print(percantage)

def line_chart():
    plt.plot(names, percantage)
    plt.xlabel("Students")
    plt.ylabel("Percentage")
    plt.title("Student Marks Graph")
    plt.show()

line_chart()

def bar_chart():
    plt.bar(names, percantage)
    plt.xlabel("Students")
    plt.ylabel("Percentage")
    plt.title("Student Marks Graph")
    plt.show()

bar_chart()