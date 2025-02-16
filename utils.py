import json
import os

def clean(text: str) -> str:
    """Removes non-alphabetic characters and converts text to lowercase."""
    return ''.join(filter(str.isalpha, text)).lower()


def analyze_frequency(path: str) -> dict | None:
    """ Analyzes the frequency of each letter in the text file at the given path. 
    Returns a dictionary with the frequency of each letter or None if an error occurs. """
    frequency_dict = {
        "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0,
        "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0,
        "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0
    }

    text_length = 0
    # Open file
    with open(path, 'r', encoding="utf-8-sig") as file: 
        for line in file: 
            cleaned_line = clean(line) # Clean text
            for c in cleaned_line:
                if c in frequency_dict: # Count the occurences of each letter
                    frequency_dict[c] += 1
            # Count total number of letters in the text
            text_length += len(cleaned_line)

        if text_length == 0:
            raise ValueError("The file contains no alphabetic characters.")
        
        # Calculate the frequency of each letter in percent
        for c in frequency_dict:
            frequency_dict[c] = (frequency_dict[c] / text_length)*100

        return frequency_dict
    

def load_baseline(file_path: str) -> dict | None:
    """ Loads the baseline data from the given JSON file path. """
    with open(file_path, 'r') as file:
        # Parse the JSON file into a dictionary
        data = json.load(file)

    if baseline_is_valid(data):
        return data
    else:
        raise Exception
        
def baseline_is_valid(data: dict) -> bool:
    """ Validates that the dictionary has letters as keys and occurrences as numbers. """ 
    if not isinstance(data, dict): 
        print("Error: The provided data is not a dictionary.") 
        return False 
    for key, value in data.items(): # Validate keys
        if not (isinstance(key, str) and len(key) == 1 and key.isalpha()):
            print(f"Error: The key '{key}' is not a single alphabetic character.") 
            return False 
    if not isinstance(value, (int, float)): # Validate values
        print(f"Error: The value for key '{key}' is not a number.") 
        return False
    return True


def get_path() -> str:
    """Asks for a filepath until a valid path is given"""
    while True: 
        path = input("Filepath: ").strip() 
        if path_is_valid(path):
                if file_is_not_empty(path):
                    return path
                else:
                    print("Error: File was empty.")
        else: print("Error: Path was not found or could not be read.")


def path_is_valid(path: str) -> bool:
    """"Checks if a file can be found and read"""
    return os.path.exists(path)

def file_is_not_empty(path: str) -> bool:
    return os.path.getsize(path) > 0 # check that the file is not empty

def get_key() -> int:
    """ Asks for a key until a valid key (1-26) is given. """
    while True:
        key = input("Key: (1-26)").strip()
        if key_is_valid(key): 
            return int(key) 
        else: print("Invalid key. Please enter a number between 1 and 26.")


def key_is_valid(key: str) -> bool:
    try:
        key = int(key)
        if 1 <= key <= 26:
            return True
    except:
        return False
