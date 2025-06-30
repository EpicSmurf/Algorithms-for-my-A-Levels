#You will need this for Year One/AS Level CS
#This is a simple stack implementation using a list called group
#The stack stores names and has some empty spaces to push new items into
#left_pointer shows where the top of the stack is right now
#The user can PUSH to add a name, PEAK to see the top name, or POP to remove it

group = ["", "", "", "", "Ben", "John",]  #Our stack stored in a list, with empty slots at the front
length = len(group)  #length of the list (6)
left_pointer = 4     #points to the top item in the stack from the left side
right_pointer = 5    #points to the very end of the stack (last element)

#Function to add an item to the stack
def push(item):
    global left_pointer
    left_pointer = left_pointer -1  #move pointer left to the empty space
    group[left_pointer] = str(item) 
    print(group)                    
    return group

#Function to see the top item of the stack without removing it
def peak():
    for i in range(0, len(group)-1):  
        if group[i] != "":            #find the first non-empty spot from left
            pointer = group[i]        #that's the top item
            print(pointer, "is at the top of the stack")
            return group

#Function to remove the top item from the stack
def pop():
    global left_pointer
    if right_pointer < 6:             #check if popping is allowed 
        print(group[left_pointer], "has been removed.")  
        group[left_pointer] = ""       #remove item from stack
        left_pointer = left_pointer + 1  #move pointer right since item is removed
        print(group)                   
    else:
        print("Sorry we can't pop the stack")  #no items to pop
    return group

#Main
choice = ""
while choice != 'END':
    print("Options: PUSH, PEAK, POP, END")
    choice = str(input("Enter what you would like to do: ")).upper()
    if choice == "PUSH":
        item = str(input("Enter the item you would like to PUSH: "))
        push(item)
    elif choice == "PEAK":
        peak()
    elif choice == "POP":
        pop()
