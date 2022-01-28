import sys

from wordleWords import La, Ta

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z']

def calcFreqs(separateDuplicates):
    chars = {}
    for n in alphabet:
        chars[n] = 0
        chars[n+n] = 0
        chars[n+n+n] = 0
    for line in La:
        if separateDuplicates: 
            wcf = {}
        for i in range (0,5):
            if not separateDuplicates:
                chars[line[i]] += 1
            else:
                if line[i] in wcf:
                    wcf[line[i]] += 1
                else:
                    wcf[line[i]] = 1
                # adds to dictionary; multiple instances of char are considered different
                # so a first e is counted separately from a second e
        if separateDuplicates:
            for w in wcf:
                if wcf[w] == 3:
                    chars[w+w+w] += 1
                if wcf[w] >= 2:
                    chars[w+w] += 1
                if wcf[w] >= 1:
                    chars[w] += 1
    # keys are sorted based on frequency
    d = sorted(chars, key=chars.get, reverse=True)

    # sorted dictionary generated
    sortedChars = {}
    for c in d:
        if chars[c] == 0:
            continue
        sortedChars[c] = chars[c]

    return sortedChars

if len(sys.argv) < 2:
    print(calcFreqs(True))
    print(calcFreqs(False))
else:
    for word in sys.argv[1:]:
        freqs = calcFreqs(False)
        wordScore = 0
        for char in word:
            wordScore += freqs[char]
        print(word+": "+str(wordScore))



