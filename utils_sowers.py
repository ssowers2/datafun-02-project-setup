"""
Module: utils_sabriya

Purpose: Reusable Module for My Analytics Projects

Description: This module provides essential tools for analyzing and presenting data 
related to a doggy daycare. It demonstrates skills in data manipulation, 
statistical analysis, and creating formatted outputs using f-strings. 
With reusable functions and clear documentation, this module supports 
efficient and scalable analytics projects.

Author: Sabriya Sowers
Date: January 19, 2025

Key Features: 
- Computes and displays basic statistics for data.
- Produces clear, formatted outputs.
- Includes reusable tools for analytics projects.

"""

#####################################
# Import Modules
#####################################

# Import helpful modules from the Python Standard library
# See more at: https://docs.python.org/3/library/

import statistics  # provides mean(), stdev() and more....

#####################################
# Declare Global Variables
#####################################

# declare a boolean variable (has a value True or False)
# TODO: Add another or replace this with your own boolean variable
has_overnight_boarding: bool = True

# declare an integer variable 
# TODO: Add or replace this with your own integer variable
number_of_employees: int = 5

# declare a floating point variable
# TODO: Add or replace this with your own floating point variable
average_dogs_per_day: float = 9.8

# declare a list of strings
# TODO: Add or replace this with your own list  
services_offered: list = ["Boarding", "Grooming", "Training", "Walking"]

# declare a list of numbers so we can illustrate statistics skills
# TODO: Add or replace this with your own numeric list  
dogs_per_day: list = [10, 11, 9, 12, 7]

# Calculate basic statistics using built-in Python functions and the statistics module
# TODO: Replace these variable names with the variable name of your own numeric list
min_dogs: float = min(dogs_per_day)  
max_dogs: float = max(dogs_per_day)  
mean_dogs: float = statistics.mean(dogs_per_day)  
stdev_dogs: float = statistics.stdev(dogs_per_day)

# Use a Python formatted string (f-string) to show information
# TODO: Modify the text in the byline to fit your information
# TODO: Modify the variables in the byline to use your variable names
byline: str = f"""
---------------------------------------------------------
Stellar Analytics: Delivering Professional Insights
---------------------------------------------------------
Has Overnight Boarding:              {has_overnight_boarding}
Number of Employees:                 {number_of_employees}
Services Offered:                    {services_offered}
Dogs Per Day:                        {dogs_per_day}
Minimum Dogs Per Day:                {min_dogs}
Maximum Dogs Per Day:                {max_dogs}
Mean Dogs Per Day:                   {mean_dogs:.2f}
Standard Deviation of Dogs Per Day:  {stdev_dogs:.2f}
"""

#####################################
# Define global functions (resuable instructions)
#####################################

def get_byline() -> str:
    '''
    Get a byline for my analytics projects.
       
    Returns a string byline that illustrates my specific skills.

    A function is a block of code that performs a task.
    This function just returns our byline.
    We can call this (or other functions) in later modules 
    so we can write it once and reuse it. 
    We use a type hint to indicate this function returns a string
    (that is, it has a Python type of str).
    It doesn't need any additional information passed in, 
    so there's nothing needed inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''
    return byline

#####################################
# Define main function for this module.
#####################################

def main() -> None:
    '''
    Print results of get_byline() when main() is called.

    This function just prints the byline to the console when we run this as a script.
    The type hint indicates this function doesn't return anything when called 
    (that is, it has a Python type of None).
    It doesn't need any additional information passed in, 
    so there's nothing inside the parentheses.
    Everything afer the colon must be indented consistently (usually 4 spaces)
    '''

    print("Starting........")
    print(get_byline())
    print("Complete.......")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()

#TODO: Run this as a script and verify all code works as intended.
