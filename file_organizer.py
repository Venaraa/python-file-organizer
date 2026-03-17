import os
import shutil
import tkinter as tk
from tkinter import filedialog


def organize_folder(folder_path):
    """
    Organizes all files in the given folder path into category folders
    based on their file extensions.
    """
    
    items_in_folder = os.listdir(folder_path) 

    file_categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".ppm", ".webp"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx", ".odt", ".rtf", ".csv"],
        "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv", ".webm", ".mpeg", ".mpg"],
        "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".m4a"]
    }

    for item in items_in_folder:
        full_path = os.path.join(folder_path, item)  

        if os.path.isfile(full_path):
            file_name, file_extension = os.path.splitext(item)
            file_extension = file_extension.lower()
            matched_category = None  


            for category_name, extensions_list in file_categories.items():
                if file_extension in extensions_list:
                    matched_category = category_name  
                    break  

            if matched_category is not None:
                
                category_folder_path = os.path.join(folder_path, matched_category)

                if not os.path.exists(category_folder_path):
                    os.mkdir(category_folder_path)
                    print(f"Created folder: {matched_category}")

                destination_path = os.path.join(category_folder_path, item)

                
                if not os.path.exists(destination_path):
                    shutil.move(full_path, destination_path)
                    print(f"Moved {item} → {matched_category}") 
                else:
                    print(f"Skipped {item}: already exists in {matched_category}")

            else:
                print(f"{item} does not match any category")

        else:
            print("folder:", item)


root = tk.Tk()
root.withdraw()  

selected_folder = filedialog.askdirectory(title="Select the folder to organize")

if selected_folder:
    organize_folder(selected_folder)  
else:
    print("No folder selected. Exiting...")