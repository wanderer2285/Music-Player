# music_player.py

import os

class SongNode:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.prev = None

class Playlist:
    def __init__(self, playlist_name):
        self.head = None
        self.playlist_name = playlist_name

    def add_song(self, name):
        new_song = SongNode(name)
        if not self.head:
            self.head = new_song
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_song
            new_song.prev = curr
        self._write_to_file(name)

    def delete_song_by_name(self, name):
        curr = self.head
        while curr:
            if curr.name == name:
                if curr.prev:
                    curr.prev.next = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                if curr == self.head:
                    self.head = curr.next
                self._delete_from_file(name)
                return True
            curr = curr.next
        return False

    def get_all_songs(self):
        songs = []
        curr = self.head
        while curr:
            songs.append(curr.name)
            curr = curr.next
        return songs

    def count_songs(self):
        return len(self.get_all_songs())

    def sort_playlist(self):
        songs = self.get_all_songs()
        songs.sort()
        self.head = None
        for song in songs:
            self.add_song(song)

    def search_song(self, name):
        curr = self.head
        while curr:
            if curr.name == name:
                return True
            curr = curr.next
        return False

    def _write_to_file(self, name):
        with open("playlist.txt", "a") as f:
            f.write(name + "\n")

    def _delete_from_file(self, name):
        if not os.path.exists("playlist.txt"):
            return
        with open("playlist.txt", "r") as f:
            lines = f.readlines()
        with open("playlist.txt", "w") as f:
            for line in lines:
                if line.strip() != name:
                    f.write(line)

    def load_from_file(self):
        if not os.path.exists("playlist.txt"):
            return
        with open("playlist.txt", "r") as f:
            for line in f:
                self.add_song(line.strip())

class MusicPlayer:
    def __init__(self, playlist_name):
        self.playlist = Playlist(playlist_name)
        self.recently_played = []  # stack

    def add_song(self, name):
        self.playlist.add_song(name)

    def delete_song(self, name):
        return self.playlist.delete_song_by_name(name)

    def show_playlist(self):
        songs = self.playlist.get_all_songs()
        print("\nPlaylist:")
        for i, song in enumerate(songs, 1):
            print(f"{i}. {song}")

    def play_song(self, name):
        if self.playlist.search_song(name):
            print(f"\nNow playing: {name}")
            if not self.recently_played or self.recently_played[-1] != name:
                self.recently_played.append(name)
        else:
            print("\nSong not found in playlist.")

    def show_recently_played(self):
        if not self.recently_played:
            print("\nNo recently played songs.")
        else:
            print("\nRecently Played:")
            for song in reversed(self.recently_played):
                print(song)

    def show_last_played(self):
        if not self.recently_played:
            print("\nNo song has been played yet.")
        else:
            print(f"\nLast Played: {self.recently_played[-1]}")

    def total_songs(self):
        print(f"\nTotal Songs: {self.playlist.count_songs()}")

    def search_song(self, name):
        if self.playlist.search_song(name):
            print("\nSong found in playlist.")
        else:
            print("\nSong not found.")

    def sort_playlist(self):
        print("\nSorting playlist...")
        self.playlist.sort_playlist()
        print("Sorted.")

    def load_playlist(self):
        self.playlist.load_from_file()

# Sample interactive menu
if __name__ == "__main__":
    mp = MusicPlayer("My Playlist")
    mp.load_playlist()

    while True:
        print("\n\n--- Music Player Menu ---")
        print("1. Add Song")
        print("2. Delete Song")
        print("3. Show Playlist")
        print("4. Play Song")
        print("5. Recently Played")
        print("6. Last Played")
        print("7. Total Songs")
        print("8. Search Song")
        print("9. Sort Playlist")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            song = input("Enter song name: ")
            mp.add_song(song)
        elif choice == "2":
            song = input("Enter song name to delete: ")
            if mp.delete_song(song):
                print("Deleted successfully.")
            else:
                print("Song not found.")
        elif choice == "3":
            mp.show_playlist()
        elif choice == "4":
            song = input("Enter song name to play: ")
            mp.play_song(song)
        elif choice == "5":
            mp.show_recently_played()
        elif choice == "6":
            mp.show_last_played()
        elif choice == "7":
            mp.total_songs()
        elif choice == "8":
            song = input("Enter song name to search: ")
            mp.search_song(song)
        elif choice == "9":
            mp.sort_playlist()
        elif choice == "10":
            break
        else:
            print("Invalid choice.")
