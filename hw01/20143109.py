import sys

args1 = sys.argv[1]
args2 = sys.argv[2]
file1 = args1
file2 = args2

with open(args1, "r", encoding='UTF8') as f:
    data1 = f.read()
with open(args2, "r", encoding='UTF8') as f:
    data2 = f.read()

wordSplit1 = data1.split()
wordCountFlag = len(wordSplit1)
syllableSplit1 = []

wordSplit2 = data2.split()
syllableSplit2 = []

for i in wordSplit1:
    if (('.') in list(i)) or ((',') in list(i)) or (('"') in list(i)) or (("'") in list(i)):
        for j in list(i):
            if (j == '.') or (j == ',') or (j == '"') or (j == "'"):
                continue
            else:
                syllableSplit1 += j
    else:
        syllableSplit1 += list(i)

for i in wordSplit2:
    if (('.') in list(i)) or ((',') in list(i)) or (('"') in list(i)) or (("'") in list(i)):
        for j in list(i):
            if (j == '.') or (j == ',') or (j == '"') or (j == "'"):
                continue
            else:
                syllableSplit2 += j
    else:
        syllableSplit2 += list(i)
    


syllableCountFlag = len(syllableSplit1)

wordDictSum = {}
syllableDictSum = {}

for i, word in enumerate(wordSplit1):
    if wordSplit1[i] in wordDictSum:
        wordDictSum[word] += 1
    elif not(wordSplit1[i] in wordDictSum):
        wordDictSum[word] = 1
    else:
        print('error')
for i, syllable in enumerate(syllableSplit1):
    if syllableSplit1[i] in syllableDictSum:
        syllableDictSum[syllable] += 1
    elif not(syllableSplit1[i] in syllableDictSum):
        syllableDictSum[syllable] = 1
    else:
        print('error')

for i, word in enumerate(wordSplit2):
    if wordSplit2[i] in wordDictSum:
        wordDictSum[word] += 1
    elif not(wordSplit2[i] in wordDictSum):
        wordDictSum[word] = 1
    else:
        print('error')
for i, syllable in enumerate(syllableSplit2):
    if syllableSplit2[i] in syllableDictSum:
        syllableDictSum[syllable] += 1
    elif not(syllableSplit2[i] in syllableDictSum):
        syllableDictSum[syllable] = 1
    else:
        print('error')

sameWords = 0
samesyllables = 0

for i, word in enumerate(wordSplit1):
    if wordDictSum[word] > 1:
        sameWords += 1
for i, syllable in enumerate(syllableSplit1):
    if syllableDictSum[syllable] > 1:
        samesyllables += 1

wordPers = (sameWords/wordCountFlag) * 100
syllablePers = (samesyllables/syllableCountFlag) * 100

print(f'sentence 1 : {data1}')
print(f'sentence 2 : {data2}')

print(f'words similarity = {wordPers}%')
print(f'syllabic similarity = {syllablePers}%')
