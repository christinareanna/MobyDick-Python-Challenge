from collections import Counter
import string


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


with open("mobydick.txt", encoding="utf8") as f:
    passage_text = f.read()

with open("stop-words.txt") as f:
    stopwords = [line.strip() for line in f]


top_words = get_top_words(passage_text, stopwords)

for word, count in top_words:
    print(f"{word}: {count}")
