class Node:
    def __init__(self, name, time, purpose):
        self.name = name
        self.time = time
        self.purpose = purpose
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insert
    def insert(self, root, name, time, purpose):
        if root is None:
            return Node(name, time, purpose)

        if name.lower() < root.name.lower():
            root.left = self.insert(root.left, name, time, purpose)
        else:
            root.right = self.insert(root.right, name, time, purpose)

        return root

    # Search
    def search(self, root, name):
        if root is None:
            return None

        if name.lower() == root.name.lower():
            return root
        elif name.lower() < root.name.lower():
            return self.search(root.left, name)
        else:
            return self.search(root.right, name)

    # Find minimum node
    def min_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    # Delete
    def delete(self, root, name):
        if root is None:
            return None

        if name.lower() < root.name.lower():
            root.left = self.delete(root.left, name)

        elif name.lower() > root.name.lower():
            root.right = self.delete(root.right, name)

        else:
            if root.left is None:
                return root.right

            if root.right is None:
                return root.left

            temp = self.min_node(root.right)

            root.name = temp.name
            root.time = temp.time
            root.purpose = temp.purpose

            root.right = self.delete(root.right, temp.name)

        return root

    # Inorder
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.name, root.time, root.purpose)
            self.inorder(root.right)

    # Preorder
    def preorder(self, root):
        if root:
            print(root.name, root.time, root.purpose)
            self.preorder(root.left)
            self.preorder(root.right)

    # Postorder
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.name, root.time, root.purpose)

    # Count
    def count(self, root):
        if root is None:
            return 0
        return 1 + self.count(root.left) + self.count(root.right)


# Main program
bst = BST()

while True:
    print("\n--- VISITOR LOG BOOK ---")
    print("1. Insert Log Entry")
    print("2. Delete Log Entry")
    print("3. Search Log Entry")
    print("4. Inorder Traversal")
    print("5. Preorder Traversal")
    print("6. Postorder Traversal")
    print("7. Count Total Entries")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter visitor name: ")
        time = input("Enter entry time: ")
        purpose = input("Enter purpose: ")

        bst.root = bst.insert(bst.root, name, time, purpose)
        print("Entry inserted successfully.")

    elif choice == 2:
        name = input("Enter visitor name to delete: ")

        if bst.search(bst.root, name):
            bst.root = bst.delete(bst.root, name)
            print("Entry deleted successfully.")
        else:
            print("Entry not found.")

    elif choice == 3:
        name = input("Enter visitor name to search: ")
        result = bst.search(bst.root, name)

        if result:
            print("Visitor Name:", result.name)
            print("Entry Time:", result.time)
            print("Purpose:", result.purpose)
        else:
            print("Entry not found.")

    elif choice == 4:
        print("\nInorder Traversal:")
        bst.inorder(bst.root)

    elif choice == 5:
        print("\nPreorder Traversal:")
        bst.preorder(bst.root)

    elif choice == 6:
        print("\nPostorder Traversal:")
        bst.postorder(bst.root)

    elif choice == 7:
        print("Total Entries:", bst.count(bst.root))

    elif choice == 8:
        print("Program terminated.")
        break

    else:
        print("Invalid choice.")
