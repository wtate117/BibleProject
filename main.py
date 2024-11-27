
from collections import Counter
import string
import pandas as pd
import numpy as np


def count_dem_words():
    # Open and read the file
    # Using Colossians
    book = 'Colossians' + '.rtf'  # pick a certain book of the Bible
    Bible = 'ESV Bible 2001.txt'
    file_path = f'/Users/wesleytate/PycharmProjects/BibleWordProject/Bibletxt/{Bible}'  #
    with open(file_path, 'r') as file:
        text = file.read()
    # Normalize the text: remove punctuation and convert to lowercase
    translator = str.maketrans('', '', string.punctuation)
    clean_text = text.translate(translator).lower()

    # Split the text into words
    words = clean_text.split()

    # Count the words
    word_counts = Counter(words)

    # Create dataframe
    df = pd.DataFrame(word_counts.items(), columns=['Word', 'Count'])
    # Sort the dataframe
    df = df.sort_values(by='Count', ascending=False).reset_index(drop=True)

    return df

def print_results(df):
    print(df)


def summary_stats(df):
    max_index = df['Count'].idxmax()  # Get the index of the max value
    max_word = df.loc[max_index, 'Word']  # Get the word at that index
    max_count = df.loc[max_index, 'Count']  # Get the count at that index
    print(f"The word with the maximum count is '{max_word}' with a count of {max_count}.")

# Export to Excel
# df.to_csv('word_counts.csv', index=False)  # Set index=False to avoid exporting the index
# print("DataFrame exported to 'word_counts.csv'.")


# fruit of the spirit
def fruit_of_the_spirit(df):
    fruit = ['love', 'joy', 'peace', 'patience', 'kindness', 'goodness', 'faithfulness', 'gentleness', 'selfcontrol']
    fruit_seeds = np.zeros((len(fruit), 2), dtype=object)

    # Fruit loop
    for f, berry in enumerate(fruit):
        fruit_seeds[f, 0] = berry
        fruit_seeds[f, 1] = df.query(f"Word == '{berry}'")['Count'].iloc[0] if not df.query(f"Word == '{berry}'").empty else 0

    trendy_fruits = fruit_seeds[np.argsort(fruit_seeds[:, 1])[::-1]]
    return trendy_fruits


def main():
    # Your main program logic here
    word_count = count_dem_words()
    f_scores = fruit_of_the_spirit(word_count)

    print(f_scores)

if __name__ == "__main__":
    main()
