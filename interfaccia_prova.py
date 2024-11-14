import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("400x150")  # Larghezza x Altezza
root.resizable(False, False)  # Impedisce di ridimensionare la finestra

root.title("Generatore POS")

# Etichetta e campo di input per il nome dell'azienda
label_azienda = tk.Label(root, text="Inserisci il nome dell'azienda:", font=("Arial", 14), fg="blue", bg="lightgrey")
label_azienda.pack(padx=20, pady=10)

entry_azienda = tk.Entry(root)
entry_azienda.pack(padx=20, pady=10)

# Bottone per generare il POS
btn_genera_pos = tk.Button(root, text="Genera POS")
btn_genera_pos.pack(padx=20, pady=20)

# Avvio dell'interfaccia grafica
root.mainloop()