MAX=5
queue=[]
def enqueue():
    if len(queue)>=MAX:
        print("Queue is FULL! Insertion is not possible")
    else:
        car=input("Enter Car Number:")
        queue.append(car)
        print(f'"{car}" added to the queue')
def dequeue():
    if len(queue)==0:
        print("Queue is EMPTY!")
    else:
        car=queue.pop(0)
        print(f'"{car}" removed from the queue')
def display():
    if len(queue)==0:
        print("Queue is EMPTY!")
    else:
        print("Queue Elements(Front to Rear):")
        for car in queue:
            print(car)
while True:
    print("\n------Queue Using Array------")
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Display")
    print("4.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        print("Program Ended")
        break
    else:
        print("Invalid Choice!")
