import shutil
import os

# 1. Create a text file and write sample data
file_name = "sample.txt"
with open(file_name, "w") as f:
    f.write("Hello, this is sample data.\n")
    f.write("This is the second line.\n")

print("File created and data written.\n")

# 2. Read and print file contents
print("Reading file contents:")
with open(file_name, "r") as f:
    content = f.read()
    print(content)

# 3. Append new lines and verify content
with open(file_name, "a") as f:
    f.write("This is an appended line.\n")
    f.write("Another appended line.\n")

print("After appending:")
with open(file_name, "r") as f:
    print(f.read())

# 4. Copy and back up files using shutil
backup_name = "sample_backup.txt"
shutil.copy(file_name, backup_name)
print(f"Backup created: {backup_name}")

# 5. Delete files safely
def safe_delete(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} deleted successfully.")
    else:
        print(f"{filename} does not exist.")

# Example deletion (uncomment if you want to delete)
# safe_delete(file_name)
# safe_delete(backup_name)