#A linear search steps through each item in a list one by one and checks if it is the target item.
#It is easy to implement, works well on small datasets and Data does not need to be sorted
#However, it is slow on large datasets

group = ["Zelonograd", "Julius", "Edward", "Augustus", "Ragnar", "Haestein", "Bjorn", "Aaron"]
def LinearSearch(group):
    found = False
    ToFind = str(input("Enter the name you want to find: "))
    for i in range(len(group)):
        if group[i] == ToFind:
            print(ToFind,"was found at postion",i)
            found = True
    if found == False:
        print("The item is entered incorrectly or is not in the list")
