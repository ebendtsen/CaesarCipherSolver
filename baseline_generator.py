import utils as utl
import json
import matplotlib.pyplot as plt

def get_baseline() -> None:
    """Prompts the user to provide a file path and language for text analysis.
    Calculates letter frequency and saves it to a JSON file. 
    Optionally plots the baseline data. """
    print('Enter filepath for text to be analysed: ')
    path = utl.get_path()
    language = input('What language is the text: ').strip().lower()

    # Calculate the frequency of each letter in sample
    baseline = utl.analyze_frequency(path)

    # Save the result to a JSON file
    try:
        with open(f'{language}_baseline.json', 'w') as json_file:
            json.dump(baseline, json_file, indent=4)  # Save with pretty formatting
    except IOError: 
        print("An error occurred while writing the JSON file.")

    # Optionally plot the baseline
    action = input("Do you wish to plot the baseline (y/n)?").strip().lower()
    if action == "y":
        plot_baseline(None, baseline)

    
def plot_baseline(jsonfile = None, frequencydict: dict = None) -> None:
    """ Plots the letter frequency baseline data. 
    Either a JSON file or a frequency dictionary must be provided. """
    # Ensure that either jsonfile or frequencydict is provided, but not both
    if jsonfile and frequencydict:
        raise ValueError("Provide either jsonfile or frequencydict, not both.")
    if not jsonfile and not frequencydict:
        raise ValueError("Provide either jsonfile or frequencydict.")
    
    try:
        # Load baseline from jsonfile if it's provided
        if jsonfile:
            baseline = utl.load_baseline(jsonfile)
            print("Loaded baseline from jsonfile.")
        elif frequencydict:
            baseline = frequencydict  # Use frequencydict directly
            print("Using provided frequencydict.")
        
        # Extract keys and values
        letters = list(baseline.keys())
        percentages = list(baseline.values())
        
        # Plot the data
        plt.figure(figsize=(10, 6))
        plt.bar(letters, percentages, color='skyblue')

        # Add labels and title
        plt.xlabel('Letters of the Alphabet')
        plt.ylabel('Percentage of Occurrences (%)')
        plt.title('Percentage of Occurrences of Each Letter in Text')
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        # Show the plot
        plt.tight_layout()
        plt.savefig('baseline.png')
        plt.show()
    
    except Exception as e:
        print(f"An unexpected error occurred when plotting the baseline data: {e}")