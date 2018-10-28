def file_to_wordlist(fname):
    wordlist = []

    f = open(fname, 'r')


    for line in f:
        line = line.rstrip('\n')
        line = line.replace('-', ' ') # replace hyphens with whitespace
        cleaned_line = []
        line_strs = line.split(" ")
        for word in line_strs:
            word = word.translate(None, '.,?!":;()*')
            word = word.lower()
            if word != "":  # check for empty string here
                cleaned_line.append(word)
        wordlist.extend(cleaned_line)
    f.close()
    return wordlist