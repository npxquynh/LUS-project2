import re
import default_concept as def_con

def step_2(training_file):
    transducer = dict()
    with open(training_file) as f:
        for line in f:
            words = re.split('[ ]+', line.strip())
            if len(words) >= 3:
                if words[0] not in transducer:
                    transducer[words[0]] = set()
                transducer[words[0]].add(words[1])

    # treating special case
    tmp_set = set()
    tmp_set.add('null');
    transducer['null'] = tmp_set

    # treating unknown words
    tmp_set = set()
    tmp_set.add('<unk>')
    transducer['<unk>'] = tmp_set

    return transducer

# def step_2_cutoff(training_file, cutoff_lexicon):
#     transducer = dict()
#     with open(training_file) as f:
#         for line in f:
#             words = re.split('[ ]+', line.strip())
#             if len(words) >= 3 and words[0] in cutoff_lexicon:
#                 if words[0] not in transducer:
#                     transducer[words[0]] = set()

#                 if words[1] in cutoff_lexicon:
#                     transducer[words[0]].add(words[1])
#                 else:
#                     transducer[words[0]].add('null')
#     return transducer

def step_3(training_file):
    transducer = dict()
    with open(training_file) as f:
        for line in f:
            words = re.split('[ ]+', line.strip())
            if len(words) >= 3:
                word = words[1]
                concept = ""

                if words[2] == 'null':
                    # keep the non-terminal the same
                    concept = word
                else:
                    concept = words[2]

                if word not in transducer:
                    transducer[word] = set()
                transducer[word].add(concept)

    # treating special case
    null_set = set()
    null_set.add('null');
    transducer['null'] = null_set

    # all unknown words should be mapped to all possible concepts
    all_concepts = def_con.all_possible_concepts()
    all_concepts.add('null')
    transducer['<unk>'] = all_concepts

    return transducer

def write_transducer(filename, transducer):
    with open(filename, 'w') as output:
        for word in transducer:
            for conceptual_word in transducer[word]:
                output.write('%d\t%d\t%s\t%s\n' % (0, 0, word, conceptual_word))
        # special case
        output.write('%d\t%d\t%s\t%s\n' % (0, 0, '<unk>', '<unk>'))

        # accepting state
        output.write('0\n');

