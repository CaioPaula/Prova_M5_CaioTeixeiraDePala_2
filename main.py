import os
# Function to execute the program based on the operating system
def execute_program_on_os() -> None:
    # Get the current directory path
    raw_current_dir_path = os.getcwd()
    current_dir_path = raw_current_dir_path.replace("\\", "/")
    os.system(f"{current_dir_path}/backend/controllers/windows.bat")
# Main entry point of the script
if __name__ == "__main__":
    # Execute the program based on the detected operating system
    execute_program_on_os()
