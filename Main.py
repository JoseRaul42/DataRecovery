import os
from Recover import recover_files

def is_valid_directory(path):
    return os.path.exists(path) and os.path.isdir(path)

def prompt_user_for_input(prompt_text):
    user_input = input(prompt_text)
    while not is_valid_directory(user_input):
        print(f"The path '{user_input}' is invalid. Please enter a valid path.")
        user_input = input(prompt_text)
    return user_input


def get_mimetype_from_user_choice():
    mimetype_map = {
        "1": "JPEG",
        "2": "PNG",
        "3": "PDF",
    }
    print("Choose the file type to recover:")
    print("1: JPEG")
    print("2: PNG")
    print("3: PDF")
    choice = input("Enter your choice (1/2/3): ")
    while choice not in mimetype_map:
        print("Invalid choice. Please select 1, 2, or 3.")
        choice = input("Enter your choice (1/2/3): ")
    return mimetype_map[choice]

def main():
    print("Welcome to the Data Recovery Tool")
    source_drive = input("Enter the drive letter to recover files from (e.g., F): ")
    bytes_size = int(input("Enter the size of bytes to read (e.g., 512): "))
    mimetype = get_mimetype_from_user_choice()
    destination_directory = prompt_user_for_input("Enter the destination directory path: ")
    
    # Calling the recover function with user inputs
    recover_files(bytes_size, mimetype, source_drive, destination_directory, source_drive)

if __name__ == "__main__":
    main()
