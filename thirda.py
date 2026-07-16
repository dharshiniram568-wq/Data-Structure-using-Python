          # Stack Implementation using Array (List)
# Library Management - Storing Book Titles

MAX = 5
stack = []

# Push Operation
def push(book):
    if len(stack) == MAX:
        print("Stack Overflow! Library stack is full.")
    else:
        stack.append(book)
        print(f'"{book}" added to the stack.')

# Pop Operation
def pop():
    if len(stack) == 0:
        print("Stack Underflow! No books in the stack.")
    else:
        book = stack.pop()
        print(f'"{book}" removed from the stack.')

# Display Operation
def display():
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("\nBooks in Stack (Top to Bottom):")
        for i in range(len(stack) - 1, -1, -1):
            print(stack[i])

# Main Program
while True:
    print("\n--- Library Stack Menu ---")
    print("1. Push Book")
    print("2. Pop Book")
    print("3. Display Stack")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book = input("Enter book title: ")
        push(book)

    elif choice == 2:
        pop()

    elif choice == 3:
        display()

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
