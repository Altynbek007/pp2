import os
import shutil

# Base directory for exercises
base_dir = "test_dir"

# 1. Create nested directories
nested_path = os.path.join(base_dir, "folder1", "folder2", "folder3")
os.makedirs(nested_path, exist_ok=True)
print(f"Nested directories created: {nested_path}\n")

# Create some sample files
with open(os.path.join(base_dir, "file1.txt"), "w") as f:
    f.write("Sample text file")

with open(os.path.join(base_dir, "file2.py"), "w") as f:
    f.write("print('Hello world')")

with open(os.path.join(base_dir, "folder1", "file3.txt"), "w") as f:
    f.write("Another text file")


# 2. List files and folders
print("Listing files and folders:")
for root, dirs, files in os.walk(base_dir):
    print(f"\nIn directory: {root}")
    print("Folders:", dirs)
    print("Files:", files)


# 3. Find files by extension
def find_files_by_extension(directory, extension):
    matches = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                matches.append(os.path.join(root, file))
    return matches

txt_files = find_files_by_extension(base_dir, ".txt")
print("\nFound .txt files:")
for file in txt_files:
    print(file)


# 4. Move/copy files between directories
destination_dir = os.path.join(base_dir, "destination")
os.makedirs(destination_dir, exist_ok=True)

# Copy files
for file in txt_files:
    shutil.copy(file, destination_dir)

print("\nCopied .txt files to destination folder.")

# Move one file
source_file = os.path.join(base_dir, "file2.py")
shutil.move(source_file, destination_dir)
print("Moved file2.py to destination folder.")


# Verify destination contents
print("\nDestination folder contents:")
print(os.listdir(destination_dir))