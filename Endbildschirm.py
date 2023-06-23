import tkinter as tk
from tkinter import messagebox

# Funktion, die aufgerufen wird, wenn der "Neues Spiel" Button geklickt wird
def start_new_game():
    # Hier können Sie den Code einfügen, um ein neues Spiel zu starten
    messagebox.showinfo("Neues Spiel", "Ein neues Spiel wurde gestartet!")

# Funktion, die das Spielergebnis anzeigt
def show_game_result(result):
    messagebox.showinfo("Spielende", result)

# Hauptfenster erstellen
root = tk.Tk()
root.title("Tic Tac Toe")

# Ergebnis-Label erstellen
result_label = tk.Label(root, text="Spielergebnis")
result_label.pack()

# Neues Spiel starten Button hinzufügen
new_game_button = tk.Button(root, text="Neues Spiel starten", command=start_new_game)
new_game_button.pack()

# Ergebnis testen
show_game_result("Spieler X hat gewonnen!")

# Hauptereignisschleife starten