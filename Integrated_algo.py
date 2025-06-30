#I wanted to implement all the Algorithmns needed for AS/Year 1 Computer Science into an integrated very small project
#I will be using names of the Presidents/PM for my data set
#The data was purposefully unordered so the sorting Algorithmns actually served a purpose
#The user will have the option between to choose between the 4 Algorithmns: Linearsearch, Binarysearch, Bubblesort and Insertionsort depending on what they want to do with the array
#Once they select the algorithmn, the corresponding function/Algorithmn will run and will return/print either (Position of the word or not found) or (Sorts the data and outputs number of passes and swaps)


#The Data set of leaders/Former Leaders
group = ["OBAMA", "STARMER", "BIDEN", "TRUMP", "BUSH", "BLAIR"]
g_length = len(group)

#LinearSearch ->If the user wants to search for a specific piece of data
def Linearsearch():
    found = False
    ans = str(input("Enter the word you are looking for: ")).upper()
    for i in range(g_length):
        if group[i] == ans:
            print(ans, "has been found at position", i)
            found = True
    if found == False:
        print("The word has not been found or is not in the data set")

#BinarySearch -> Quicker way of searching for a piece of data compared to Linear search (unless first item)
def Binarysearch():
    group = Insertionsort()                      #This is to ensure that the data has been sorted before running the function, this is a requirement for Binarysearch. I choose Insertionsort because it is faster than bubblesort
    ans = str(input("Enter the word you want to search for: ")).upper()
    left = 0
    right = g_length
    found = False
    while left <= right and found == False:
        midpoint = (left + right) //2
        if group[midpoint] == ans:
            print(ans, "has been found at position", midpoint)
            found = True
        elif group[midpoint] > ans:
            right = midpoint - 1
        else:
            left = midpoint + 1
    if found == False:
        print(ans, "word has not been found")
    return group

#Bubblesort ->Sorting Algorithmn
#Easier to implement but less efficient
def Bubblesort():
    swapped = False
    n = g_length
    passes = 0
    swaps = 0
    while n > 0 and swapped == False:
        n = n-1
        passes += 1
        for i in range(0, n):
            if group[i] > group[i+1]:
                temp = group[i+1]
                group[i+1] = group[i]
                group[i] = temp
                swapped == True
                swaps += 1
    print("Here is the ordered data", group)
    print("There were", swaps, "swaps and", passes, "passes.")
    return group

#Insertionsort -> Sorting Algorithmn
#Eassier to implement, more efficient than bublesort but still not the most efficient
def Insertionsort():
    n = g_length
    swaps = 0
    passes = 0
    for index in range(1, n):
        index2 = index
        current = group[index]
        while index2 > 0 and group[index2-1] > current:
            group[index2] = group[index2 -1]
            index2 = index2 - 1
            swaps += 1
        group[index2] = current
        passes += 1
    if choice != "INSERTIONSORT":     #This is so that if the initial choice was binarysearch, the data would be sorted before running the function so it only needs to return the ordered array
        return group
    else:                            #This is if the user initially chooses insertionsort so would like to recieve data on how many swaps and passes it takes to order the array
        print("Here is the ordered data:",group)
        print("There were", swaps, " and ", passes, "passes.")

#Menu or Main
valid = False
choice = " "
while valid == False:
    print("Here is the data:", group)
    print("The Algorithmns to choice are: ")
    print("LINEARSEARCH")
    print("BINARYSEARCH")
    print("BUBBLESORT")
    print("INSERTIONSORT")
    print("Or you can END")
    choice = str(input("Enter the algorithn you want to use or to END: ")).upper()
    if choice == "LINEARSEARCH":
        valid = True
    elif choice == "BINARYSEARCH":
        valid = True
    elif choice == "BUBBLESORT":
        valid = True
    elif choice == "INSERTIONSORT":
        valid = True
    elif choice == "END":
        print("Program has ended")
        valid = True
    else:
        print("Not valid function")

if choice == "LINEARSEARCH":
    Linearsearch()
elif choice == "BINARYSEARCH":
    Binarysearch()
elif choice == "BUBBLESORT":
    Bubblesort()
elif choice == "INSERTIONSORT":
    Insertionsort()
