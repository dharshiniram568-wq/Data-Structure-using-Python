# Stack using Linked List with User Input

class Node:
    def __init__(self, book_title):
        self.book_title = book_title
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    # Push operation
    def push(self, book_title):
        new_node = Node(book_title)
        new_node.next = self.top
        self.top = new_node
        print(f'"{book_title}" added to the stack.')

    # Pop operation
    def pop(self):
        if self.top is None:
            print("Stack is empty. No book to retrieve.")
        else:
            removed_book = self.top.book_title
            self.top = self.top.next
            print(f'"{removed_book}" retrieved from the stack.')

    # Display operation
    def display(self):
        if self.top is None:
            print("Stack is empty.")
        else:
            print("\nBooks in the stack (Top to Bottom):")
            temp = self.top
            while temp:
                print(temp.book_title)
                temp = temp.next


# Main Program
stack = Stack()

while True:
    print("\n--- Library Stack Menu ---")
    print("1. Push (Add Book)")
    print("2. Pop (Retrieve Book)")
    print("3. Display Books")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        title = input("Enter book title: ")
        stack.push(title)

    elif choice == 2:
        stack.pop()

    elif choice == 3:
        stack.display()

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
