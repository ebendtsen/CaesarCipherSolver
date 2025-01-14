# Caesar Cipher Solver

This project provides tools to encrypt, and decrypt Caesar ciphers. It utilizes frequency analysis to decrypt ciphers where the key is not known or decrypts using a known key. It also has functionality to create new baselines for decrypting and visualisation of baseline letter frequencies.
## Features
- **Encrypt Text:** Encrypt plain text using a Caesar cipher with a specified key.
- **Decrypt Text:** Decrypt cipher text using a known key or solve the key using letter frequency analysis.
- **Baseline Generation:** Create baselines from text samples to use in frequency analysis.
- **Visualization:** Plot letter frequency data for analysis and comparison.
## Project Structure
```Plaintext
├── main.py
├── baseline_generator.py
├── cipher_solver.py
├── utils.py
├── data
│   ├── samples
│	│	├── cipher1.txt
│	│	├── cipher2.txt
│	│	├── cipher3.txt
│	│	├── plaintext1.txt
│	│	├── plaintext2.txt
│	│	└── plaintext3.txt
│	├── eng_baseline.json (default baseline for English)
│       └── theGreatGatsby_Gutenberg.txt
└── README.md (this file)
```
### Files
- **main.py:** The main script to run the Caesar Cipher programme.
- **baseline_generator.py:** Contains functions to generate and plot letter frequencies based on a text sample.
- **cipher_solver.py:** Contains functions to encrypt, decrypt, and solve Caesar ciphers.
- **utils.py:** Utility functions for cleaning text, frequency analysis, and file handling.
## Requirements
- Python 3.x
- Required Python packages:    
    - `matplotlib`
    
Install the required packages using
```shell
pip install matplotlib
```
## Usage
### Running the Main Program
1. Open your terminal.
2. Navigate to the project directory.
3. Run the main script:
```shell
    python main.py
```
4. Follow the instructions in the terminal to choose an action:
    - **Decrypt (d)**
    - **Encrypt (e)**
    - **Create new baseline (b)**
    - **Exit (x)**

### Sample Files

Sample files are provided in the `data` folder to help you try out the encryption, decryption, and baseline creation features:
- `plaintext1.txt`: A sample file for encryption.
- `cipher1.txt`: A sample file for decryption.
- `data\theGreatGatsby_Gutenberg.txt`: A sample file for baseline creation.
Use these samples to quickly test and understand how the program works.

### Encrypting Text
1. Choose the `Encrypt (e)` option.
2. Provide the file path for the text to encrypt (e.g., `data\samples\plaintext1.txt`).
3. Provide the encryption key (1-26).
5. The encrypted text will be saved to `cipheroutput.txt`.

### Decrypting Text with a Known Key
1. Choose the `Decrypt (d)` option.
2. Choose `Use key (k)` option.
3. Provide the file path for the cipher (e.g., `data\samples\cipher1.txt).
4. Provide the decryption key (1-26).
5. The decrypted text will be saved to `plainoutput.txt`.
    
### Solving Cipher Key
1. Choose the `Decrypt (d)` option.
2. Choose `Solve key (s)` option.
3. Provide the file path for the cipher. (e.g., `data/sample_cipher.txt`).
4. Provide the file path for the baseline (optional).
	- If you choose `no` then the provided baseline for English, `eng_baseline.json`, will be used.
5. The programme will determine the key and decrypt the text.
6. The decrypted text will be saved to `plainoutput.txt`.

### Creating a Baseline
To decrypt a Caesar cipher the programme matches letter frequencies from a baseline with the letter frequencies in the sample. Each language will have a different baseline. A default baseline for the English language is provided. This feature can be used to create baselines for other languages. 

1. Choose the `Create new baseline (b)` option.    
2. Provide the file path for the text sample (e.g., `data\theGreatGatsby_Gutenberg.txt`).
3. Provide the language of the text.
4. The baseline will be saved as a JSON file.

### Plotting a Baseline
After creating a new baseline, you can optionally plot the letter frequency data:

1. When creating a baseline you will be prompted wether you wish to plot the baseline.
2. To plot the baseline, write `y`as the option.
3. To skip plotting the baseline, write `n`.

## What I learned

This project taught me a lot about decryption and frequency analysis. I also got to try `matplotlib` and `os` libraries for the first time and learned many new coding tricks I had not used before (e.g., some new functions like `ord()` and how to make my code more readable through type hinting). I also ran into issues with encoding when attempting to decrypt and encrypt files as well as reading the Great Gatsby sample. These issues were quickly fixed by explicitly stating which type of decoding/encoding to use (e.g., utf-8-sig for handling UTF-8 BOM encoding).

In the future, this project could be improved by using a more sophisticated decryption method. The current method used will only reliably work on a sample that is a little longer; shorter samples will not decrypt correctly.

The English language baseline was created using a few chapters from [the Great Gatsby by F. Scott Fitzgerald](https://www.gutenberg.org/ebooks/64317), which is available copyright free through the Gutenberg project.
