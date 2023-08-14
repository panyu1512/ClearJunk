
import os
import shutil
import re
import zipfile

class clearJunk:
    def __init__(self, directory_path, destination_path):
        self.directory_path = os.path.expanduser(directory_path)
        self.destination_path = os.path.expanduser(destination_path)
    def remove_temp_files(self):
        extensions = [
            '.log',
            '.cache',
            '.tmp',
            '.dmg',
            '.pkg'
        ]

        for file in os.listdir(self.directory_path):
            if os.path.splitext(file)[1] in extensions:
                print(f"Removing {file}")
                file_path = os.path.join(self.directory_path, file)
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                    print(f"Successfully deleted {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")

    def remove_duplicated_files(self):
        for root, dirs, files in os.walk(self.directory_path):
            file_dict = {}
            for file in files:
                file_path = os.path.join(root, file)
                # check if file is a duplicate
                match = re.search(r'^(.*?)\((\d+)\)(\.[^.]*)?$', file)
                if match:
                    name = match.group(1)
                    number = int(match.group(2))
                    extension = match.group(3)
                    if name not in file_dict:
                        file_dict[name] = [(number, file_path, extension)]
                    else:
                        file_dict[name].append((number, file_path, extension))
            # Rename files in each group
            for name in file_dict:
                files = file_dict[name]
                files.sort(key=lambda tup: tup[0])
                print(files)
                latest = files[-1][1]
                extension = files[-1][2]
                for number, file_path, _ in files[:-1]:
                    print(f"Deleted duplicate file: {file_path}")
                    os.remove(file_path)
                os.rename(latest, os.path.join(root, f"{name}{extension}"))
                print(f"Renamed {latest} to {name}{extension}")

    def clean_up_directory(self):
        file_types = {
            "Image": [
                ".jpg",
                ".jpeg",
                ".png",
                ".gif",
                ".bmp",
                ".svg",
                ".webp"
            ],
            "Video": [
                ".mp4",
                ".mov",
                ".avi",
                ".flv",
                ".wmv",
                ".mkv",
                ".m4v",
                ".mpeg",
                ".mpg",
                ".3gp"
            ],
            "Audio": [
                ".mp3",
                ".wav",
                ".aac",
                ".ogg",
                ".flac",
                ".wma",
                ".alac"
            ],
            "Document": [
                ".pdf",
                ".doc",
                ".docx",
                ".xls",
                ".xlsx",
                ".ppt",
                ".pptx",
                ".txt",
                ".rtf",
                ".tex",
                ".pages",
                ".numbers",
                ".key"
            ],
            "Archive": [
                ".zip",
                ".tar",
                ".gz",
                ".7z",
                ".rar",
                ".pkg",
                ".dmg",
                ".iso"
            ],
            "Code": [
                ".py",
                ".c",
                ".cpp",
                ".java",
                ".class",
                ".cs",
                ".h",
                ".sh",
                ".swift",
                ".vb",
                ".js",
                ".ts",
                ".css",
                ".html",
                ".xml",
                ".json"
            ],
        }

        # Create folders for each file type
        for folder_name in file_types.keys():
            folder_path = os.path.join(self.destination_path, folder_name)
            if not os.path.isdir(folder_path):
                os.makedirs(folder_path)
        # Iterate over the files in the directory
        for file in os.listdir(self.directory_path):
            file_path = os.path.join(self.directory_path, file)
            # unzipped files and delete the zip file
            if file.endswith(".zip"):
                unzip_directory = os.path.join(self.directory_path, file[:-4])
                if not os.path.exists(unzip_directory):
                    with zipfile.ZipFile(file_path, 'r') as zip_ref:
                        zip_ref.extractall(self.directory_path)
                # Delete the zip file
                os.remove(file_path)
                print(f"Unzipped {file_path} and removed {file}")

            # Move files to their respective folders
            else:
                for folder_name, extensions in file_types.items():
                    if os.path.splitext(file)[1] in extensions:
                        destination_folder_path = os.path.join(self.destination_path, folder_name)
                        shutil.move(file_path, os.path.join(destination_folder_path, file))
                        print(f"Moved {file_path} to {destination_folder_path}")
                        break

    def remove_old_files(self):
        inactivity_days = 90
        for root, dirs, files in os.walk(self.directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                if os.stat(file_path).st_mtime < inactivity_days * 86400:
                    os.remove(file_path)
                    print(f"Removed {file_path}")

if __name__ == "__main__":
    import sys
    directory_path = sys.argv[1]
    destination_path = sys.argv[2]
    clearJunk = clearJunk(directory_path, destination_path)
    clearJunk.remove_temp_files()
    clearJunk.remove_duplicated_files()
    clearJunk.clean_up_directory()
    clearJunk.remove_old_files()
