# clearJunk - Python Script for Cleaning Up Directories

The `clearJunk` Python script is designed to help you clean up and organize files within a specified directory. The script performs various cleaning and organizing tasks to help you manage your files more efficiently.

## Table of Contents

- [Introduction](#clearjunk---python-script-for-cleaning-up-directories)
- [Table of Contents](#table-of-contents)
- [Description](#description)
- [Functions](#functions)
  - [Initialization](#initialization)
  - [`remove_temp_files(self)`](#remove_temp_filesself)
  - [`remove_duplicated_files(self)`](#remove_duplicated_filesself)
  - [`clean_up_directory(self)`](#clean_up_directoryself)
  - [`remove_old_files(self)`](#remove_old_filesself)
- [Usage](#usage)
- [How to Run the Script](#how-to-run-the-script)
- [Important Notes](#important-notes)

## Description

The `clearJunk` script is organized into a class with several functions that perform different file management tasks:

- `remove_temp_files(self)`: Removes temporary files with specific extensions from the directory.
- `remove_duplicated_files(self)`: Identifies duplicated files with version numbers and keeps only the most recent version.
- `clean_up_directory(self)`: Organizes files by moving them into subfolders based on their types and handles ZIP files.
- `remove_old_files(self)`: Removes files that have been inactive for a specified number of days.

## Functions

### Initialization

The `clearJunk` class is initialized with two parameters:

- `directory_path`: The path to the directory you want to clean up.
- `destination_path`: The path to the directory where organized files will be moved.

### `remove_temp_files`

This function removes temporary files based on their extensions. It iterates through files in the specified directory and removes files with certain extensions (e.g., `.log`, `.cache`, `.tmp`, `.dmg`, `.pkg`).

### `remove_duplicated_files`

This function identifies duplicated files in the specified directory and renames them to resolve the duplication. It searches for files with names in the format "name(number).extension" and keeps the most recent version of each file.

### `clean_up_directory`

This function organizes files in the specified directory into subfolders based on their types. It iterates through the files and moves them to appropriate subfolders based on their extensions. If a ZIP file is encountered, its contents are extracted into a folder with the same name (minus `.zip`), and the ZIP file is removed.

### `remove_old_files`

This function removes files that have been inactive for a specified number of days (`inactivity_days`). It calculates the last modified timestamp for each file and deletes files that haven't been modified within the specified time frame.

## Usage

1. Create an instance of the `clearJunk` class with the appropriate directory paths.
2. Call the functions you want to execute. The script will perform tasks such as removing temporary files, organizing files by type, handling duplicated files, and removing old files based on your specifications.

## How to Run the Script

To run the script and perform the cleaning and organizing tasks:

1. Open a terminal or command prompt.
2. Navigate to the directory containing the script using the `cd` command.
3. Execute the script using the following command, replacing the paths with your own:
   
   ```bash
   python clearJunk.py ~/SourceDirectory ~/DestinationDirectory
