"""
Module: sabriya_project_setup

Purpose: Provide functions to script project folders (and domonstrate basic Python coding skills).

Description: This module provides functions for creating a series of project folders.

Author: Sabriya Sowers

TODO: Change the module name in this opening docstring
TODO: Change the author in this opening docstring
"""

#####################################
# Import Modules at the Top
#####################################

# Import moduldes from standand library
# TODO: Import additional modules as needed
import pathlib
import time

# Import local modules
# TODO: Change this to import your module and uncomment
import utils_sowers

#####################################
# Declare global variables
#####################################

# Create a project path object
project_path = pathlib.Path.cwd()

#Print current project path to verify this works. (Completed, it does work!)
print(f"Current Project Path: {project_path}")

# Create a project data path object
data_path = project_path.joinpath('data')

# Create the data path if it doesn't exist, otherwise do nothing. The path didn't exist and was created.
data_path.mkdir(exist_ok=True)

#####################################
# Define Function 1. For item in Range: Create a function to generate folders for a given range (e.g., years).
# Pass in an int for the first year
# Pass in an int for the last year
#####################################

def create_folders_for_range(start_year: int, end_year: int) -> None:
    '''
    Create folders for a given range of years in the project path.
    
    Arguments:
    start_year -- The starting year of the range (inclusive).
    end_year -- The ending year of the range (inclusive).

    '''

    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_folders_for_range with start_year={start_year} and end_year={end_year}")

    # TODO: Implement the actual folder creation logic
    # Loop through each year in the specified range including the end_year
    for year in range(start_year, end_year + 1):
        # Constructs the folder name by appending the year to the project path
        folder_name = f"{project_path}/{year}"
        # Creates the directory for the current year if it doesn't already exist
        pathlib.Path(folder_name).mkdir(parents=True, exist_ok=True)
        # Logs the created directory to the console
        print(f"Created directory: {folder_name}")

# Function called to create folders for 2020 - 2023.

#####################################
# Define Function 2. For Item in List: Develop a function to create folders from a list of names.
# Pass in a list of folder names 
#####################################

def create_folders_from_list(folder_list: list, to_lowercase: bool = True, remove_spaces: bool = True) -> None:
    '''
    Creates folders from a given list of folder names in the project path.
    
    The folder names are all converted (if not already) to be lowercase and without spaces.

    This function takes a list of folder names and creates them as directories
    inside the current project path. If the folder already exists, it's skipped.

    Arguments:
    folder_list -- A list of folder names (strings) to create.
    to_lowercase -- If True, converts folder names to lowercase. Default is True.
    remove_spaces -- If True, removes spaces from folder names. Default is True.

    '''
    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_folders_from_list with folder_list={folder_list}, to_lowercase={to_lowercase}, remove_spaces={remove_spaces}")

    # TODO: Add docstring
    # TODO: Log the function call and its arguments
    # TODO: Implement this function and remove the temporary pass

    # Iterates through the folder list and creates each folder
    for folder_name in folder_list:
        #converts folder names to lowercase
        if to_lowercase:
             folder_name = folder_name.lower() 
        #removes spaces from folder names
        if remove_spaces:
             folder_name = folder_name.replace(" ", "") 
        #Creates folder path using project path and folder name
        folder_path = pathlib.Path(project_path) / folder_name 
        #Creates the folder if it doesn't already exist
        folder_path.mkdir(parents=True, exist_ok=True) 
        # Logs the created folder to the console
        print(f"Created folder: {folder_name}")

# Function called to create new folders

#####################################
# Define Function 3. List Comprehension: Create a function to create prefixed folders by transforming a list of names and combining each with a prefix (e.g., "data-").
# Pass in a list of folder names
# Pass in a prefix (e.g. 'data-') to add to each
#####################################

def create_prefixed_folders(folder_list: list, prefix: str) -> None:
    # TODO: Implement this function professionally and remove the temporary pass
    '''
    Create prefixed folders by adding a prefix to each folder name.

    This function takes a list of folder names and creates them as directories
    with the specified prefix in the current project path. If the folder already 
    exists, it's skipped.

    Arguments:
    folder_list -- A list of folder names (strings) to create.
    prefix -- A string to prefix each folder name with.
    
    '''
    # Log the function call and its arguments using an f-string
    print(f"FUNCTION CALLED: create_prefixed_folders with folder_list={folder_list} and prefix={prefix}")
    
    # Generates a list of prefixed folder names
    prefixed_folders = [f"{prefix}{name}" for name in folder_list]
    
    # Iterates through the prefixed folder list and create directories
    for folder_name in prefixed_folders:
        # Construct the folder path
        folder_path = pathlib.Path(project_path) / folder_name
        #Creates the folder if it doesn't already exist
        folder_path.mkdir(parents=True, exist_ok=True)
        # Logs the created folder to the console
        print(f"Created folder: {folder_name}")

# Function called to create new prefixed folders

#####################################
# Define Function 4. While Loop: Write a function to create folders periodically (e.g., one folder every 5 seconds).
# Pass in the wait time in seconds
#####################################

def create_folders_periodically(duration_seconds: int) -> None:
    # TODO: Implement this function professionally and remove the temporary pass
    '''
    Creates a new folder from a predefined list of folder names every `duration_seconds` seconds.

    This function iterates through a predefined list of folder names and creates
    a folder every `duration_seconds` seconds. If the folder already exists, it skips
    over it and moves to the next folder.

    Arguments:
    duration_seconds -- The time in seconds to wait before creating the next folder.
    '''
    # List of folders to create
    folder_list: list = ["Folder1", "Folder2", "Folder3", "Folder4"]
    
    # Initializes the index to track the folders bring created
    index: int = 0

    # While statement that loops through the list to create folders
    while index < len(folder_list):
        # Gets the current folder name from the list
        folder_name = folder_list[index]
        # Constructs the full folder path
        folder_path = project_path / folder_name

        # Checks if folder already exists
        if not folder_path.exists():
            folder_path.mkdir(parents=True, exist_ok=True)
            print(f"Created folder: {folder_name}")
        else:
            # Skips folder creation if already exists
            print(f"Folder {folder_name} already exists. Skipping over.")
        
        # Moves to the next folder in the list
        index += 1

        # Waits for the specified duration (5 secs) before creating next folder
        if index < len(folder_list):
            print(f"Waiting {duration_seconds} seconds before creating the next folder.")
            time.sleep(duration_seconds)
            
    # Logs the created folders to the console
    print("All folders have been created.")

#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    # Start of main execution
    print("#####################################")
    print("# Starting execution of main()")
    print("#####################################\n")

    # Print get_byline() from imported module
    # TODO: Change this to use your module function and uncomment
    print(f"Byline: {utils_sowers.get_byline()}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs:int = 5  # duration in seconds
    create_folders_periodically(duration_secs)

    # TODO: Add options e.g., to force lowercase and remove spaces 
    # to one or more of your functions (e.g. function 2) 
    # Call your function and test these options
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
    # Uncomment this line after you've added your custom logic
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

    # End of main execution
    print("\n#####################################")
    print("# Completed execution of main()")
    print("#####################################")

#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()

#TODO: Run this as a script to test that all functions work as intended.