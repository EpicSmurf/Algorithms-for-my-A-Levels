#Here is the Bublesort algorithmn, The main idea of a bubble sort is to bubble the largest item to the top of the list each pass, putting it in its correct place.
group = ["Zelonograd", "Julius", "Edward", "Augustus", "Ragnar", "Haestein", "Bjorn", "Aaron"]
def Bubblesort(group):
    swaps = True
    n = len(group)
    while swaps == True and n > 0:
        swaps = False
        n = n-1
        for i in range(0, n):
            if group[i] > group[i+1]:
                temp = group[i]
                group[i] = group[i+1]
                group[i+1] = temp
                swaps = True
    print(group)
#Buble sort works well on small lists and is easy to implement but the issue is that it is inefficient on longer lists due to many redundant comparisons
