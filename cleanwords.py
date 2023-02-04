# get all stop words
# want to count how many times words show up in moby dick book
# exclude stop words
# key value format
# top 100

from collections import Counter
import string

pathToText = "/Users/christinaknapp/Documents/mobydick-project/mobydick.txt"
pathToStopWords = "/Users/christinaknapp/Documents/mobydick-project/stop-words.txt"


def getTextRead(pathToFile):
    with open(pathToFile) as f:
        words = f.read()
        return words

def getTextReadLines(pathToFile):
    with open(pathToFile) as f:
        words = f.readlines()
        return words


def getStopWordsSet(stopWordsText):

    stopwords = set()

    for word in stopWordsText:
        # Use strip to get rid of extra space at beginning and end of string
        word = word.strip()
        # If word doesn't start with # and isn't an empty string, add to stopwords set
        if not word.startswith("#") and word != "":
            stopwords.add(word)
    return stopwords

def text_process(text):
    text = text.lower()
    text = text.translate(str.maketrans(
        "", "", string.punctuation))  # removes punctuation. maketrans takes 3 parameters. leave first 2 empty, put punctuation in 3rd parameter
    text = text.split()
    return text

def get_top_words(text, stopwords):
    words = text_process(text)
    words = [word for word in words
            if word not in stopwords]  # remove stopwords from words
    word_counter = Counter(words)
    return word_counter.most_common(100)


def main():
    stopWordsText = getTextReadLines(pathToStopWords)
    passageText = getTextRead(pathToText)
    stopwordset = getStopWordsSet(stopWordsText)
    wordCountList = get_top_words(passageText, stopwordset)
    print(wordCountList)


if __name__ == "__main__":
    main()
