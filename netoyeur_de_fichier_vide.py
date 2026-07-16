import os
import tkinter as tk
from tkinter import filedialog, scrolledtext


def clean_path(path):
    output.delete("1.0", tk.END)
    output.insert(tk.END, f"Nettoyage: {path}\n\n")
    root.update()

    removed = 0

    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            try:
                if os.path.getsize(filepath) == 0:
                    os.remove(filepath)
                    output.insert(tk.END, f"Fichier supprimé: {filepath}\n")
                    removed += 1
            except OSError as e:
                output.insert(tk.END, f"Erreur: {filepath} ({e})\n")

    for dirpath, dirnames, filenames in os.walk(path, topdown=False):
        if dirpath == path:
            continue
        try:
            if not os.listdir(dirpath):
                os.rmdir(dirpath)
                output.insert(tk.END, f"Dossier supprimé: {dirpath}\n")
                removed += 1
        except OSError as e:
            output.insert(tk.END, f"Erreur: {dirpath} ({e})\n")

    output.insert(tk.END, f"\nTerminé. {removed} élément(s) supprimé(s).\n")


def choose_folder():
    path = filedialog.askdirectory()
    if path:
        clean_path(path)


root = tk.Tk()
root.title("Netoyeur de fichier vide")
root.geometry("500x400")

tk.Button(root, text="Choisir un dossier", command=choose_folder).pack(pady=10)

output = scrolledtext.ScrolledText(root, wrap=tk.WORD)
output.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()
