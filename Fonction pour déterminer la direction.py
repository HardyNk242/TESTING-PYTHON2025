import tkinter as tk
from tkinter import messagebox

# Fonction pour déterminer la direction
def get_geological_direction(angle):
    directions = [
        "Nord (N)", "Nord-Nord-Est (NNE)", "Nord-Est (NE)", "Est-Nord-Est (ENE)",
        "Est (E)", "Est-Sud-Est (ESE)", "Sud-Est (SE)", "Sud-Sud-Est (SSE)",
        "Sud (S)", "Sud-Sud-Ouest (SSO)", "Sud-Ouest (SW)", "Ouest-Sud-Ouest (OSO)",
        "Ouest (W)", "Ouest-Nord-Ouest (ONO)", "Nord-Ouest (NW)", "Nord-Nord-Ouest (NNO)"
    ]
    angle = angle % 360
    index = int((angle + 11.25) // 22.5) % 16
    return directions[index]

# Fonction appelée lors du clic sur le bouton
def determine_direction():
    try:
        angle = float(entry.get())
        direction = get_geological_direction(angle)
        result_var.set(f"➡️ Direction géologique : {direction}")
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer un angle valide (nombre).")

# Interface graphique
root = tk.Tk()
root.title("Direction Géologique")
root.geometry("400x200")
root.resizable(False, False)

# Widgets
label = tk.Label(root, text="Entrez un angle (en degrés)", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack()

btn = tk.Button(root, text="Déterminer la direction", command=determine_direction, font=("Arial", 12))
btn.pack(pady=10)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 12), fg="blue")
result_label.pack(pady=5)

# Lancer l'application
root.mainloop()
