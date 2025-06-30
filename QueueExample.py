#You will need this for Year one/AS Level CS
#This is a simple queue implementation using a list called group
#The queue stores names and has empty spaces to add new items
#left_pointer shows where the front of the queue is right now (where to dequeue)
#right_pointer shows where the next item will be added (enqueue)
#The user can ENQUEUE to add a name, DEQUEUE to remove from the front

group = ["", "", "", "", "", ""]  #Queue list with empty slots
length = len(group)
left_pointer = 0   #front of queue
right_pointer = 0  #back of queue (next free spot)

def enqueue(item):
    global right_pointer
    if right_pointer < length:
        group[right_pointer] = str(item)
        right_pointer += 1
        print(group)
    else:
        print("Queue is full, cannot add more items.")

def dequeue():
    global left_pointer, right_pointer
    if left_pointer < right_pointer:
        print(group[left_pointer], "has been removed.")
        group[left_pointer] = ""
        left_pointer += 1
        print(group)
    else:
        print("Queue is empty, nothing to remove.")

choice = ""
while choice != "END":
    print("Options: ENQUEUE, DEQUEUE, END")
    choice = input("Enter what you would like to do: ").upper()
    if choice == "ENQUEUE":
        item = input("Enter the item you would like to ENQUEUE: ")
        enqueue(item)
    elif choice == "DEQUEUE":
        dequeue()
