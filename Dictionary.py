import json 
from difflib import get_close_matches

#Load dictionary data
def load_dictionary():
    with open('dictionary.json', 'r') as file:
        data = json.load(file)
        
    return data

#Function to get word definition
def get_definition(word, data):
    word = word.lower() # Convert word to lowercase
    if word in data:
        return data[word]
    else:
        #Check for similar words
        similar_words = get_close_matches(word, data.keys(), n=3, cutoff=0.8)
        if similar_words:
            suggestion= similar_words[0]
            choice = input(f"Did you mean '{suggestion}' instead? (yes/no): ").lower()
            if choice == 'yes':
                return data[suggestion]
            else:
                return "Word not found. Please try again."
        else:
            return "Word not found. Please try again."
        
        
#Main function
def main():
    data = load_dictionary()
    while True:
        word = input("Enter a word to get its definition (or type 'exit' to quit): ")
        if word.lower() == 'exit':
            break
        
        else:
            definition = get_definition(word, data)
            print(definition)
            
if __name__ == "__main__":
    main()