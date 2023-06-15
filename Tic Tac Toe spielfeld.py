import tkinter as tk
from tkinter import messagebox

# Spielfeld initialisieren
spielfeld = [['', '', ''],
              ['', '', ''],
              ['', '', '']]

# Aktueller Spieler (X beginnt)
aktueller_spieler = 'X'

# Funktion, die aufgerufen wird, wenn ein Button im Spielfeld geklickt wird
def button_click(row, col):
    global aktueller_spieler

    # Überprüfen, ob das Feld bereits belegt ist
    if spielfeld[row][col] == '':
        # Feld mit dem aktuellen Spieler setzen
        spielfeld[row][col] = aktueller_spieler

        # Text im Button aktualisieren
        buttons[row][col].config(text=aktueller_spieler)

        # Überprüfen, ob ein Spieler gewonnen hat
        if gewonnen(aktueller_spieler):
            messagebox.showinfo("Spielende", f"Spieler {aktueller_spieler} hat gewonnen!")
            reset_spiel()
        # Überprüfen, ob das Spielfeld vollständig belegt ist (Unentschieden)
        elif unentschieden():
            messagebox.showinfo("Spielende", "Unentschieden!")
            reset_spiel()
        else:
            # Spieler wechseln
            aktueller_spieler = 'O' if aktueller_spieler == 'X' else 'X'

# Überprüfen, ob ein Spieler gewonnen hat
def gewonnen(spieler):
    # Überprüfen der Zeilen
    for row in spielfeld:
        if row.count(spieler) == 3:
            return True

    # Überprüfen der Spalten
    for col in range(3):
        if [spielfeld[row][col] for row in range(3)].count(spieler) == 3:
            return True

    # Überprüfen der Diagonalen
    if spielfeld[0][0] == spielfeld[1][1] == spielfeld[2][2] == spieler:
        return True
    if spielfeld[0][2] == spielfeld[1][1] == spielfeld[2][0] == spieler:
        return True

    return False

# Überprüfen, ob das Spielfeld vollständig belegt ist (Unentschieden)
def unentschieden():
    for row in spielfeld:
        if '' in row:
            return False
    return True

# Spiel zurücksetzen
def reset_spiel():
    global spielfeld, aktueller_spieler

    spielfeld = [['', '', ''],
                  ['', '', ''],
                  ['', '', '']]
    aktueller_spieler = 'X'

    # Alle Buttons zurücksetzen
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text='')

# Hauptfenster erstellen
root = tk.Tk()
root.title("Tic Tac Toe")

# Buttons für das Spielfeld erstellen
buttons = []
for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(root, text='', width=10, height=5,
                           command=lambda r=row, c=col: button_click(r, c))
        button.grid(row=row, column=col, padx=5, pady=5)
        button