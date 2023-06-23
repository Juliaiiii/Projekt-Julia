import tkinter as tk

# Funktion zum Öffnen des Einstellungsfensters
def open_settings_window():
    # Neues Fenster für die Einstellungen erstellen
    settings_window = tk.Toplevel(root)
    settings_window.title("Einstellungen")

    # Einstellungen Widgets hinzufügen
    sound_label = tk.Label(settings_window, text="Ton ein-/ausschalten:")
    sound_label.pack()

    sound_checkbox = tk.Checkbutton(settings_window, text="Ton aktivieren", variable=sound_enabled)
    sound_checkbox.pack()

    save_button = tk.Button(settings_window, text="Speichern", command=save_settings)
    save_button.pack()

# Hauptfenster erstellen
root = tk.Tk()

# Einstellungen Variable initialisieren
sound_enabled = tk.BooleanVar()
sound_enabled.set(True)  # Ton standardmäßig aktivieren

# Einstellungen öffnen Button hinzufügen
settings_button = tk.Button(root, text="Einstellungen öffnen", command=open_settings_window)


# Funktion, die aufgerufen wird, wenn der "Neues Spiel" Button geklickt wird
def reset_spiel_einstellungen():
    reset_spiel()
    settings_window.destroy()