# Music Player (Python)

A **Python-based command-line music playlist manager** that simulates a real-world music player using core data structures like **doubly linked lists** and **stacks**. This project demonstrates object-oriented design, persistent storage, and menu-driven user interaction — making it a strong portfolio project for roles in software development, systems programming, and backend engineering.


##  Features

-  Add and manage songs in a playlist
-  Remove songs by name
-  Search songs instantly
-  View playlist in order
-  Sort playlist alphabetically
-  Play songs from the playlist
-  Maintain recently played stack (like YouTube/Spotify history)
-  Show last played track
-  Save and load playlist using persistent storage

---

##  Key Concepts & Skills

| Concept          | Applied In                                    |
|--------------------------|-----------------------------------------------|
| Doubly Linked List       | Playlist navigation and manipulation          |
| Stack (LIFO)             | Recently played song history                  |
| Object-Oriented Design   | Encapsulation using classes (`SongNode`, `Playlist`, `MusicPlayer`) |
| File Handling            | Save/load songs in `playlist.txt`             |
| Python Essentials        | Loops, conditionals, functions, class design  |

---

##  Tech Stack

- **Language**: Python 3  
- **Data Structures**: Doubly Linked List, Stack  
- **Storage**: Text File (`playlist.txt`)  
- **Interface**: Command-line (terminal)

---

### How to Run

1. **Clone the repository**
git clone https://github.com/wanderer2285/Music-Player.git
cd music-player

2. **Run the player**
python music_player.py

3. **Use the menu**
--- Music Player Menu ---
1. Add Song
2. Delete Song
...
10. Exit

---

### Sample Output

Enter your choice: 1
Enter song name: Ajab si
 Song added successfully!

Enter your choice: 4
Enter song name to play: Ajab si
 Now playing: Ajab si
```

---

##  Developer Notes

- Implemented a **custom doubly linked list** for playlist management with manual node traversal and updates.
- Ensured **stack operations are cleanly implemented** for recently played history.
- Applied object-oriented design using separate classes for songs, playlist, and playback logic.
- Playlist is **persisted between runs** using a text file.

---

### Next Steps ( Targets to Extend the project)

- Add real **audio playback** with `playsound` or `pygame`
- Build a GUI with **Tkinter** or **PyQt**
- Implement **multi-playlist support**
- Export/import playlists as **CSV/JSON**
- Add **unit tests** for core components

---

