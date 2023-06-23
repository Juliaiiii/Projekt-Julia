import tkinter as tk
from tkinter import messagebox

# Funktion, die aufgerufen wird, wenn der "Neues Spiel" Button geklickt wird
def start_new_game():
    # Hier können Sie den Code einfügen, um ein neues Spiel zu starten
    messagebox.showinfo("Neues Spiel", "Ein neues Spiel wurde gestartet!")

# Funktion, die aufgerufen wird, wenn der "Ton ein-/ausschalten" Checkbox-Status geändert wird
def toggle_sound():
    # Hier können Sie den Code einfügen, um den Ton ein- oder auszuschalten
    if sound_enabled.get():
        messagebox.showinfo("Ton", "Ton aktiviert!")
    else:
        messagebox.showinfo("Ton", "Ton deaktiviert!")

# Hauptfenster erstellen
root = tk.Tk()
root.title("Tic Tac Toe Einstellungen")

# Einstellungen Widgets hinzufügen
sound_label = tk.Label(root, text="Ton ein-/ausschalten:")
sound_label.pack()

sound_enabled = tk.BooleanVar()
sound_checkbox = tk.Checkbutton(root, text="Ton aktivieren", variable=sound_enabled, command=toggle_sound)
sound_checkbox.pack()

new_game_button = tk.Button(root, text="Neues Spiel starten", command=start_new_game)
new_game_button.pack()
