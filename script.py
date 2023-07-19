import os

def rename_files(folder_path):
    if not os.path.isdir(folder_path):
        print("Error: The provided path is not a directory.")
        return

    count = 1
    for filename in sorted(os.listdir(folder_path)):
        # Skip directories
        if os.path.isdir(os.path.join(folder_path, filename)):
            continue

        # Generate the new filename
        new_filename = f"IMG_{str(count).zfill(3)}"

        # Combine folder path and old filename to get the full path
        old_file_path = os.path.join(folder_path, filename)

        # Get the file extension
        _, file_extension = os.path.splitext(filename)

        # Create the new file path by combining folder path and new filename with extension
        new_file_path = os.path.join(folder_path, f"{new_filename}{file_extension}")

        # Rename the file
        os.rename(old_file_path, new_file_path)

        count += 1

    print("Files have been successfully renamed.")

if __name__ == "__main__":
    folder_path = os.path.dirname(os.path.abspath(__file__))
    rename_files(folder_path)
