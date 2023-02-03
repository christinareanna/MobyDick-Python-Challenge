# Initialize new set
stopwords = set()
with open("stop-words.txt") as f:
# Read file
    lines = f.readlines()

    for line in lines: 
        # Use strip to get rid of extra space at beginning and end of string
        line = line.strip()
        # If word doesn't start with # and isn't an empty string, add to stopwords set
        if not line.startswith("#") and line != "":
            stopwords.add(line)
    # print(stopwords)

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