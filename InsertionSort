#Here is an example of Insertion sort
#The key idea of this sort is to create a sorted list from a certain point (initially the first item only) and move items into the correct place in that list one at a time
#This makes Insertion Sort good at adding items to an already sorted list

group = ["Constantine", "Zelonograd", "Julius", "Edward", "Augustus", "Ragnar", "Haestein", "Bjorn", "Aaron", "Zubimendi", "Zack"]
def Insertionsort(group):
    for index in range(1, len(group)):
        current = group[index]
        index2 = index
        while index2 > 0 and group[index2-1] > current:
            group[index2] = group[index2-1]
            index2 = index2 -1
        group[index2] = current
    print(group) 
