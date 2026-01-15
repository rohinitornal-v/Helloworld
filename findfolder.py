import os

def check_file_exists(path, filename):
    """Check if a specific file exists in the given folder."""
    full_path = os.path.join(path, filename)
    exists = os.path.isfile(full_path)
    return exists


def explore_projectfolder(project_dir):
    """Explore the 'SelfLearning' folder inside the project directory."""

    # Absolute project path
    abs_path = os.path.abspath(project_dir)
    print(f"\nCurrent Project Directory: {abs_path}\n")

    # Path to SelfLearning folder
    selflearning_dir = os.path.join(project_dir, "SelfLearning")

    # Check that the folder exists
    if not os.path.exists(selflearning_dir):
        print("Error: 'SelfLearning' folder does NOT exist in this project directory.")
        return

    print("Exploring folder:", selflearning_dir, "\n")

    # Lists to store files and directories
    files = []
    directories = []

    # Get all items inside SelfLearning
    items = os.listdir(selflearning_dir)

    # Separate files and directories
    for item in items:
        full_path = os.path.join(selflearning_dir, item)
        if os.path.isfile(full_path):
            files.append(item)
        elif os.path.isdir(full_path):
            directories.append(item)

    # Print directories
    print("Directories inside 'SelfLearning':")
    for d in directories:
        print("  -", d)

    # Print files
    print("\nFiles inside 'SelfLearning':")
    for f in files:
        print("  -", f)

    # Print summary
    print("\nSummary:")
    print("  Total items:", len(items))
    print("  Total files:", len(files))
    print("  Total directories:", len(directories))

    # Categorize files
    file_types = {}
    for f in files:
        if "." in f:
            ext = f.split(".")[-1].lower()
        else:
            ext = "no_extension"

        if ext not in file_types:
            file_types[ext] = []
        file_types[ext].append(f)

    # Print categorized files
    print("\nFiles categorized by type:")
    for ext in file_types:
        print(f" .{ext} ({len(file_types[ext])}):")
        for f in file_types[ext]:
            print("    -", f)

    # Check file existence
    filename = input("\nEnter a filename to check if it exists in 'SelfLearning': ")
    if check_file_exists(selflearning_dir, filename):
        print("Yes,", filename, "exists in 'SelfLearning'.")
    else:
        print("No,", filename, "does NOT exist in 'SelfLearning'.")


# Run the program
if __name__ == "__main__":

    # Get the folder where this script is saved
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Call the function with the actual project directory
    explore_projectfolder(script_dir)