 # Music Playlist using Singly Linked List

class Node:
    def __init__(self, song):
        self.song = song
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None

    # Create playlist
    def create_playlist(self):
        n = int(input("Enter number of songs:"))
        for i in range(n):
            song = input(f"Enter song {i + 1}: ")
            self.insert_song(song)
        print("Playlist created successfully.\n")

    # Insert song at end
    def insert_song(self, song):
        new_node = Node(song)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    # Delete a song
    def delete_song(self, song):
        if self.head is None:
            print("Playlist is empty.")
            return

        # If first song is to be deleted
        if self.head.song == song:
            self.head = self.head.next
            print(f'"{song}" deleted successfully.')
            return

        prev = None
        curr = self.head

        while curr and curr.song != song:
            prev = curr
            curr = curr.next

        if curr is None:
            print("Song not found.")
        else:
            prev.next = curr.next
            print(f'"{song}" deleted successfully.')

    # Display playlist
    def display_playlist(self):
        if self.head is None:
            print("Playlist is empty.")
            return

        print("\nCurrent Playlist:")
        temp = self.head
        count = 1
        while temp:
            print(f"{count}. {temp.song}")
            temp = temp.next
            count += 1
        print()


# Main Program
playlist = Playlist()

while True:
    print("===== MUSIC PLAYLIST MENU =====")
    print("1. Create Playlist")
    print("2. Insert Song")
    print("3. Delete Song")
    print("4. Display Playlist")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        playlist.create_playlist()

    elif choice == 2:
        song = input("Enter song name to insert: ")
        playlist.insert_song(song)
        print("Song inserted successfully.\n")

    elif choice == 3:
        song = input("Enter song name to delete: ")
        playlist.delete_song(song)
        print()

    elif choice == 4:
        playlist.display_playlist()

    elif choice == 5:
        print("Exiting Music Playlist...")
        break

    else:
        print("Invalid choice! Please try again.\n")
