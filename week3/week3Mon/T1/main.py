if __name__ == '__main__':
    word = input()
    wordCapital = word.capitalize()
    wordLow = word.lower()
    #print(word)
    #print(wordCapital)
    sentence = input()
    sentenceLow = sentence.lower()
    st = 0
    ed = len(sentence)
    #while sentence.count(word, st, ed) != 0 or sentence.count(wordCapital, st, ed) != 0:
    while sentenceLow.count(wordLow, st, ed) != 0:
        #loc = sentence.find(wordCapital, st, ed) if sentence.find(wordCapital, st, ed) != -1 else sentence.find(word, st, ed)
        loc = sentenceLow.find(wordLow, st, ed)
        if loc == st:
            #print("loc = 0")
            sentenceLow = sentenceLow[:st + len(word):] + " " + sentenceLow[st + len(word)::]
            sentence = sentence[:st + len(word)] + " " + sentence[st + len(word)::]
            st = loc + len(word) + 1
        else:
            sentenceLow = sentenceLow[:loc:] + " " + sentenceLow[loc:loc + len(word):] + " " + sentenceLow[loc + len(word)::]
            sentence = sentence[:loc:] + " " + sentence[loc:loc + len(word):] + " " + sentence[loc + len(word)::]
            st = loc + len(word) + 2
        #print("sentence : " + sentence)
        ed = len(sentence)
        #print("New : " + sentence[st::])
        #print(sentence)
    while sentence[len(sentence) - 1::] == " ":
        sentence = sentence[:len(sentence) - 1:]
    print(sentence)