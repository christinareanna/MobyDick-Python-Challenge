# TO DO
# get all stop words
# want to count how many times words show up in moby dick book and exclude stop words
# key value format
# top 100 words

from collections import Counter
import string

pathToText = "./mobydick.txt"
pathToStopWords = "./stop-words.txt"

# easily can use one or the other for different purposes
# use read to read entire file 
def getTextRead(pathToFile):
    with open(pathToFile) as f:
        words = f.read()
        return words

# Use readlines to read line by line
def getTextReadLines(pathToFile):
    with open(pathToFile) as f:
        words = f.readlines()
        return words


# Put stop words into set while ignoring comments and empty strings
def getStopWordsSet(stopWordsText):
    # use set to remove duplicates
    stopwords = set()

    for word in stopWordsText:
        # Use strip to get rid of extra space at beginning and end of string
        word = word.strip()
        # If word doesn't start with # and isn't an empty string, add to stopwords set
        if not word.startswith("#") and word != "":
            stopwords.add(word)
    return stopwords

# Read all of mobydick text, put to lower case, remove punctuation using string.punctuation, split into individual words
def text_process(text):
    text = text.lower()
    text = text.translate(str.maketrans(
        "", "", string.punctuation))  # removes punctuation. maketrans takes 3 parameters. leave first 2 empty, put punctuation in 3rd parameter
    text = text.split()
    return text

# Function to get top 100 words and remove stop words 
def get_top_words(text, stopwords):
    words = text_process(text)
    words = [word.lower() for word in words
            if word not in stopwords]  # remove stopwords from words
    word_counter = Counter(words)
    return word_counter.most_common(100)

# Function to organize format of top 100 words starting with index 1 to 100
def print_top_words(wordCountList):
    for i, (word, count) in enumerate(wordCountList, 1):
        print(f"{i}. {word}: {count}")


def main():
    stopWordsText = getTextReadLines(pathToStopWords)
    passageText = getTextRead(pathToText)
    stopwordset = getStopWordsSet(stopWordsText)
    # Print statement to test stopwordset shows accurately
    # print(stopwordset)
    wordCountList = get_top_words(passageText, stopwordset)
    # Print statement to test wordCountList shows accurately
    # print(wordCountList)
    # Calling print_top_words using wordCountList as argument to show formatted list from 1-100 with word and count
    print_top_words(wordCountList)


if __name__ == "__main__":
    main()
