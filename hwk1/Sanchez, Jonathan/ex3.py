def file_to_wordlist(fname):
    wordlist = []

    f = open(fname, 'r')


    for line in f:
        line = line.rstrip('\n')
        line = line.replace('-', ' ') # replace hyphens with whitespace
        cleaned_line = []
        line_strs = line.split(" ")
        for word in line_strs:
            word = word.translate(None, '.,?!":;()*[]')
            word = word.lower()
            if word != "":  # check for empty string here
                cleaned_line.append(word)
        wordlist.extend(cleaned_line)
    f.close()
    return wordlist


def wordlist_to_wordfreq(wordlist):
    wordfreq = {}

    for word in wordlist:
        if word in wordfreq:
            wordfreq[word] += 1
        else:
            wordfreq[word] = 1

    return wordfreq

import heapq


def wordfreq_to_wordpriority(wordfreq):
    wordpriority = []

    # for realzies first we need to sort by the 2nd invariant: alphabetically

    wordfreq_keys = sorted(wordfreq)

    # first we need to convert the dictionary into a list of tuples

    for key in wordfreq_keys:
        heapq.heappush(wordpriority, (wordfreq[key], key))


    return [heapq.heappop(wordpriority) for i in range (len(wordpriority))]


