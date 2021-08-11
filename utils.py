from stop_words import sw

def isValidWord(word):
    return word != '' and (word not in sw)

def filterStopWords(listOfWords):
    return list(filter(lambda word: isValidWord(word),listOfWords))