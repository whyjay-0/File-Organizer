import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def organize (folder_path):
    file_types = {
        'Images' : ['.jpg','.jpeg','.png','.gif'],
        'Documents' : ['.pdf','.doc','.docx','.odt','.txt','.xlsx','.pptx'],
        'Videos' : ['.mp4','.avi','.mkv'],
        'Audio' : ['.mp3','.wav']
        # possibly add more types that will help with organizing prog files / using git standard
    }
    files_moved = 0
    # init types/dir name

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            _, file_extension = os.path.splitext(file_path)

            for folder, file_extension in file_types.items():
                if file_extension in file_extension:
                    target_folder = os.path.join(folder_path, folder)
                    # create dir if not yet existing
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, filename))
                    # moved to folder
                    files_moved += 1
                    break

    print(f"Moved files: {files_moved}")

# browsing folders
def browse ():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        files_moved = organize(folder_selected)
        messagebox.showinfo("Success", f"Moved {files_moved} Files Successfully")
    else:
        messagebox.showerror("Error", "Folder Not Selected")

root = tk.Tk()
root.title("File Organizer")
# setting up GUI using tk
root.geometry("400x200")

label = tk.Label(root, text="Select a folder to organize", font=("Helvetica", 13))
label.pack(pady=20)

browse_button = tk.Button(root, text="Browse", font=("Helvetica", 13),command=browse)
browse_button.pack(pady=20)

root.mainloop()