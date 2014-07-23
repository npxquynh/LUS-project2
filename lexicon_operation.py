import re
import default_concept as def_con

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

def generate_refined_cutoff_lexicon(lexicon, stopwords_filename):
    lexicon = generate_cutoff_lexicon(lexicon, stopwords_filename)

    for x in "after and around at before between by for from in of on to".split(" "):
        lexicon.add(x)

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

    all_possible_concepts = def_con.all_possible_concepts()

    special_lex = ['<epsilon>']
    irregular_lex = ['<unk>', '<s>', '</s>', 'null']
    lexicon = lexicon.union(set(irregular_lex))
    lexicon = lexicon.union(all_possible_concepts)
    lexicon = list(lexicon) # just in case lexicon is a set

    with open(filename, 'w') as output:
        for lex in special_lex + lexicon:
            output.write('%s\t%d\n' % (lex, count))
            count += 1
