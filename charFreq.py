# 5 letter word Trie Builder
# Ben 2022

import json
import pickle

print("Starting up...")

# sets up char frequency dictionary
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z']
chars = {}
for n in alphabet:
    chars[n] = 0
    chars[n+n] = 0
    chars[n+n+n] = 0

def findNumWith(s):
    count = 0
    with open('ospd5.txt') as inf:
        for line in inf:
            temp = line
            b = True
            for sc in s:
                ind = temp.find(sc)
                if ind >= 0:
                    temp2 = temp[0:ind]
                    if ind < len(temp)-1:
                        temp2 += temp[temp.find(sc)+1]
                    temp = temp2
                else:
                    b = False
                    break
            if b: count += 1
    return count

def findWordsWith(s):
    words = []
    with open('ospd5.txt') as inf:
        for line in inf:
            temp = line
            b = True
            for sc in s:
                ind = temp.find(sc)
                if ind >= 0:
                    temp2 = temp[0:ind]
                    if ind < len(temp)-1:
                        temp2 += temp[temp.find(sc)+1]
                    temp = temp2
                else:
                    b = False
                    break
            if b: words.append(line)
    return words


# generates char frequency dictionary
with open('ospd5.txt') as inf:
    for line in inf:
        # builds dict of char freq in word
        wcf = {}
        for i in range (0,5):
            if line[i] in wcf:
                wcf[line[i]] += 1
            else:
                wcf[line[i]] = 1
        # adds to dictionary; multiple instances of char are considered different
        # so a first e is counted separately from a second e
        for w in wcf:
            if wcf[w] == 3:
                chars[w+w+w] += 1
            if wcf[w] >= 2:
                chars[w+w] += 1
            if wcf[w] >= 1:
                chars[w] += 1
        # # calculate word index
        # index = 0
        # for w in wcf:

# keys are sorted based on frequency
d = sorted(chars, key=chars.get, reverse=True)

# sorted dictionary generated
sortedChars = {}
for c in d:
    if chars[c] == 0:
        break
    sortedChars[c] = chars[c]

# # print sorted dictionary
# print(sortedChars)

print("Building Trie...")

# build word trie
trie = {}
for a in alphabet:
    trie[a] = [sortedChars[a], {}]
    for b in alphabet[ord(a)-97:]:
        freq = findNumWith(a+b)
        if freq > 0:
            print("considering"+a+b)
            trie[a][1][b] = [freq, {}]
            for c in alphabet[ord(b)-97:]:
                freqq = findNumWith(a+b+c)
                if freqq > 0: 
                    trie[a][1][b][1][c] = [freqq, {}]
                    for d in alphabet[ord(c)-97:]:
                        freqqq = findNumWith(a+b+c+d)
                        if freqqq > 0:
                            trie[a][1][b][1][c][1][d] = [freqqq, {}]
                            for e in alphabet[ord(d)-97:]:
                                freqqqq = findNumWith(a+b+c+d+e)
                                if freqqqq > 0:
                                    trie[a][1][b][1][c][1][d][1][e] = [freqqqq, findWordsWith(a+b+c+d+e)]

print("Trie built.")

with open("wordleTrie.pkl",'wb') as triepickle:
    pickle.dump(trie, triepickle)

with open("wordleTrie.json", 'w') as triejson:
    json.dump(trie, triejson, indent=4)

