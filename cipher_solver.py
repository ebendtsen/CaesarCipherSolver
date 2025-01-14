import utils as utl

def cipher_solver(cipherpath: str = None, baseline_path: str = None) -> None:
    """ Decrypts a Caesar cipher with unknown key using letter frequency analysis. """
    # Ensure a baseline path
    if not baseline_path:
        use_default = input("Use default baseline for English (y/n)").strip().lower()
        if use_default == "n":
            print(
                "Provide a filepath for a .txt language sample to create a baseline.\n"
                "The baseline will be more accurate if the sample is >3000 words."
            )
            baseline_path = utl.get_path()
        else:
            baseline_path = 'data/eng_baseline.json'
    
    # Read the saved JSON file containing the letter frequencies.
    baseline = utl.load_baseline(baseline_path) 

    # Ensure a ciphertext path
    if not cipherpath:
        print("Input the filepath for the cipher:")
        cipherpath = utl.get_path()

    # Analyze the ciphertext
    cipher_frequency = utl.analyze_frequency(cipherpath)

    # Find key
    max_ciph_freq_letter = max(cipher_frequency, key=cipher_frequency.get)
    max_baseline_freq_letter = max(baseline, key=baseline.get)
    # Calculate the key based on the difference of the frequencies
    key = (ord(max_ciph_freq_letter)-ord(max_baseline_freq_letter)) % 26
    # If the key is negative, adjust it to get the correct positive equivalent within the 0-25 range
    if key > 13:
        key -= 26

    print(f"Key determined: {key}")

    # Decrypt using key
    try:
        decrypt(cipherpath, key)
    except ValueError as e:
        print(f"Error during decryption: {e}")


def decrypt(cipherpath: str = None, key: int = None) -> None:
    """Decrypts a caesar cipher using a known key and saves it as a file."""
    if not cipherpath:
        print("Input the filepath for the cipher:")
        cipherpath = utl.get_path()

    # Ensure the key is provided
    if not key:
        print("Input the decryption key:")
        key = utl.get_key()

    # Decrypt text
    decrypted = ""
    try:
        with open(cipherpath, 'r', encoding='utf-8') as file:
                content = file.read()  # Read entire content of the file
            
        for char in content:
            if char.isalpha():
                shift = 65 if char.isupper() else 97
                decrypted += chr((ord(char) - shift - key) % 26 + shift)
            else:
                decrypted += char  # Non-alphabetic characters are not changed

        with open("plainoutput.txt", 'w', encoding='utf-8') as file:
            file.write(decrypted)
        
        print("Decryption successful!\n")
    
    except Exception as e:
        print(f"An unexpected error occurred during decryption: {e}")
    
    

def encrypt(plainpath: str = None, key: int = None) -> None:
    """Encrypts a Caesar cipher and saves it as a file"""
    if not plainpath:
        print("Input the filepath for the text to encrypt:")
        plainpath = utl.get_path()

    if not key:
        print("Input the encryption key:")
        key = utl.get_key()

    encrypted = ""
    try:
        with open(plainpath, 'r', encoding='utf-8') as file:
                content = file.read()  # Read entire content of the file

        for char in content:
            if char.isalpha():
                shift = 65 if char.isupper() else 97
                encrypted += chr((ord(char) - shift + key) % 26 + shift)
            else:
                encrypted += char  # Non-alphabetic characters are not changed

        with open("cipheroutput.txt", 'w', encoding='utf-8') as file:
            file.write(encrypted)
        
        print("Encryption successful!\n")
    
    except Exception as e:
        print(f"An unexpected error occured during encryption: {e}")
