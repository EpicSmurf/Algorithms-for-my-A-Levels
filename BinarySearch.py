#Here is a searching Algorithm, an example of Binary Search
#Binary search repeatedly halves the search range by comparing the target to the midpoint, continuing until it's found or not present.
#This works quite well on large datasets however, the data MUST be sorted for this to work and it is more complex to implement than LinearSearch

group = ["Biden", "Boris", "Obama", "Rishi", "Starmer", "Trump"]
def Binarysearch(group):
    found = False
    first = 0
    last = len(group) - 1

    search = input("Enter President/PM you want to search: ")
    while first <= last and found == False:
        midpoint = (first + last) // 2
        if group[midpoint] == search:
            found = True
        else:
            if group[midpoint] < search:
                first = midpoint + 1
                print(midpoint)
            else:
                last = midpoint - 1
                print(midpoint)
    if found == True:
        print(search, "has been found at", midpoint)
    else:
        print("Not found")
