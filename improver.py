
# improver.py

import os

def manual_correction():

    """Let user correct misclassifications and suggest new keywords"""

    question = input("\nWhat question was classified wrong? ")

    print("\nWhat should it have been classified as?")
    print("1. Legal")
    print("2. Coding")
    print("3. General")

    correct_type = input("Choose (1-3): ")

    if correct_type == "1":
        category = "LEGAL"
    elif correct_type == "2":
        category = "CODING"
    else:
        category = "GENERAL"
    
    # Ask for keywrod suggestions
    new_keyword = input(f"\nSuggest a new {category} keyword from this question (or press Enter to skip): ")

    # Log the correction
    with open("corrections.txt", "a") as file:
        file.write(f"CORRECTION: '{question}' should be {category}\n")
        if new_keyword.strip():
           file.write(f"SUGGESTED KEYWORD: {new_keyword.strip()} for {category}\n")
        file.write("---\n")
    
    print(f"Correction logged! Consider adding '{new_keyword}' to your {category}_KEYWORDS list.")

def view_corrections():
    """Show all corrections made so far"""
    try:
        with open("corrections.txt", "r") as file:
            content = file.read()
            if content:
                print("\n--- Corrections Made ---")
                print(content)
            else:
                print("No corrections logged yet!")
    except FileNotFoundError:
        print("No corrections file found.")