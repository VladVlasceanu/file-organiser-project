import os
import shutil

# Change this to the folder you want to organise
folder_path = r"C:\Users\User\Downloads"

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"]
}

def organise_folder(path):
    if not os.path.exists(path):
        print("Folder does not exist.")
        return

    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)

        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file_name)[1].lower()

            moved = False
            for folder_name, extensions in file_types.items():
                if file_extension in extensions:
                    destination_folder = os.path.join(path, folder_name)
                    os.makedirs(destination_folder, exist_ok=True)

                    destination_path = os.path.join(destination_folder, file_name)
                    shutil.move(file_path, destination_path)

                    print(f"Moved: {file_name} -> {folder_name}")
                    moved = True
                    break

            if not moved:
                other_folder = os.path.join(path, "Other")
                os.makedirs(other_folder, exist_ok=True)

                destination_path = os.path.join(other_folder, file_name)
                shutil.move(file_path, destination_path)

                print(f"Moved: {file_name} -> Other")

# Run the organiser
folder_path = r"C:\Users\user\Desktop\test_folder"
organise_folder(folder_path)
print("Folder organised successfully.")
