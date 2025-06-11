class Dogs:

    species = "dog"

    def __init__(self, name, age):
        self.name = name
        self.age = age

Golden_Retriever = Dogs("Buddy", 5)
German_Shepherd = Dogs("Max", 7)

print("Golden Retriever is a {}".format(Golden_Retriever.species))
print("German Shepherd is also a {}".format(German_Shepherd.species))

print("{} is {} years old".format(Golden_Retriever.name, Golden_Retriever.age))
print("{} is {} years old".format(German_Shepherd.name, German_Shepherd.age))