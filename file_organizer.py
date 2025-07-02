import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# 🗂️ File type mapping
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.html', '.css', '.cpp', '.java'],
    'Others': []
}

def organize_files(folder_path):
    if not folder_path:
        messagebox.showwarning("No folder selected", "Please select a folder first.")
        return

    files = os.listdir(folder_path)
    for filename in files:
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            moved = False
            _, ext = os.path.splitext(filename)

            for folder, extensions in file_types.items():
                if ext.lower() in extensions:
                    dest_folder = os.path.join(folder_path, folder)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_folder, filename))
                    moved = True
                    break

            if not moved:
                others_folder = os.path.join(folder_path, "Others")
                os.makedirs(others_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(others_folder, filename))

    messagebox.showinfo("Success", "✅ Files organized successfully!")

# -------------- GUI Setup -------------- #
root = tk.Tk()
root.title("📂 File Organizer")
root.geometry("450x300")
root.configure(bg="#e0f7fa")  # Light blue

selected_folder = tk.StringVar()

def browse_folder():
    path = filedialog.askdirectory()
    selected_folder.set(path)

# Title
tk.Label(root, text="File Organizer Tool", font=("Helvetica", 20, "bold"), bg="#e0f7fa").pack(pady=20)

# Folder path field
tk.Entry(root, textvariable=selected_folder, font=("Helvetica", 12), width=40, state="readonly").pack(pady=10)

# Browse button
tk.Button(root, text="📁 Browse Folder", font=("Helvetica", 12), bg="#FFD54F", command=browse_folder).pack(pady=5)

# Organize button
tk.Button(root, text="🧹 Organize Files", font=("Helvetica", 13), bg="#4CAF50", fg="white", command=lambda: organize_files(selected_folder.get())).pack(pady=20)

# Start GUI loop
root.mainloop()
