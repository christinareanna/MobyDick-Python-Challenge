# Initialize new set to make searching faster
stopwords = set()

# get all stop words
# want to count how many times words show up in moby dick book
# exclude stop words
# key value format
# top 100


def parseWords():
    with open("stop-words.txt") as f:
        # Read file
        words = f.readlines()

    for word in words:
        # Use strip to get rid of extra space at beginning and end of string
        word = word.strip()
        # If word doesn't start with # and isn't an empty string, add to stopwords set
        if not word.startswith("#") and word != "":
            stopwords.add(word)
    print(stopwords)


parseWords()

# Test to see if words are in the set


def checkIfInSet(line):
    words = line.split()
    # Check if word is in stopwords set
    for word in words:
        if word in stopwords:
            print("This word is in the set. Can't insert!")
        else:
            print("It's not in the set")
    checkIfInSet(line)
    print(line)
