import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def organize(folder_path):
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.doc', '.docx', '.odt', '.txt', '.xlsx', '.pptx'],
        'Videos': ['.mp4', '.avi', '.mkv'],
        'Audio': ['.mp3', '.wav']
        # possibly add more types that will help with organizing prog files / using git standard
    }
    files_moved = 0

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            _, file_extension = os.path.splitext(file_path)

            for folder, extensions in file_types.items():
                if file_extension.lower() in extensions:  # Compare the file extension correctly
                    target_folder = os.path.join(folder_path, folder)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, filename))
                    files_moved += 1
                    break

    return files_moved  # Return the number of files moved

# Browsing folders
def browse():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        files_moved = organize(folder_selected)
        if files_moved == 0:
            messagebox.showinfo("Success", "No files were moved.")
        else:
            messagebox.showinfo("Success", f"Moved {files_moved} files successfully.")
    else:
        messagebox.showerror("Error", "Folder not selected.")

root = tk.Tk()
root.title("File Organizer")

# Setting up the GUI using Tkinter
root.geometry("400x200")

label = tk.Label(root, text="Select a folder to organize", font=("Helvetica", 13))
label.pack(pady=20)

browse_button = tk.Button(root, text="Browse", font=("Helvetica", 13), command=browse)
browse_button.pack(pady=20)

root.mainloop()