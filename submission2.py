filename = input("Enter the name of the file to read: ")

try:
    with open(filename, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    for i, line in enumerate(lines, start=1):
        modified_lines.append(f"{i}: {line}")

    with open("modified_file.txt", 'w') as new_file:
        new_file.writelines(modified_lines)

    print("File was read and modified successfully! Saved as 'modified_file.txt'.")

except FileNotFoundError:
    print("Error: File not found. Please check the filename and try again.")
except IOError:
    print("Error: Could not read the file.")
