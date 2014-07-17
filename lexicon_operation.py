import re

def generate_lexicon_from_textfile(filename):
    with open(filename) as f:
        lexicon = set()
        for line in f:
            words = re.split('[ ]+', line.strip())
            for word in words:
                lexicon.add(word)

    return lexicon

def generate_cutoff_lexicon(lexicon, stopwords_filename):
    stopwords = set()
    with open(stopwords_filename) as f:
        for line in f:
            stopwords.add(line.strip())

    lexicon = lexicon.difference(stopwords)
    return lexicon

def write_lexicon_to_file(filename, lexicon):
    """
    set(): lexicon
    """
    # remove empty string character
    try:
        lexicon.remove('')
    except:
        pass

    count = 0

    special_lex = ['<epsilon>']
    irregular_lex = ['<unk>', '<s>', '</s>']
    lexicon = lexicon.union(set(irregular_lex))
    lexicon = list(lexicon) # just in case lexicon is a set

    with open(filename, 'w') as output:
        for lex in special_lex + lexicon:
            output.write('%s\t%d\n' % (lex, count))
            count += 1
