def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = xrange(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def levenshtein2(a1, a2):
    if len(a1) < len(a2):
        return levenshtein(a2, a1)

    # len(a1) >= len(a2)
    if len(a2) == 0:
        return len(a1)

    previous_row = xrange(len(a2) + 1)
    for i, c1 in enumerate(a1):
        current_row = [i + 1]
        for j, c2 in enumerate(a2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def number_of_sentences_recognized(filename):
    number_of_lines = 0
    number_of_sentences = 0
    with open(filename) as f:
        for line in f:
            number_of_lines += 1
            if len(line.strip()) != 0:
                number_of_sentences += 1

    print "Recognized %d sentences over %d (%f%%)" % (
        int(number_of_sentences),
        int(number_of_lines),
        (number_of_sentences * 100.0 / number_of_lines)
    )

def analyse_edit_distance(recognized_concept_file, annotated_concept_file):
    recognized_concepts = list()
    annotated_concepts = list()

    with open(recognized_concept_file) as f:
        recognized_concepts = f.readlines()

    with open(annotated_concept_file) as f:
        annotated_concepts = f.readlines()

    # if len(recognized_concepts) != len(annotated_concepts):
    #     print "something wrong in the code!!!"
    #     return 0

    edit_distance = list()
    for i in range(len(recognized_concepts)):
        a1 = recognized_concepts[i].strip(' \n').split(' ')
        a2 = annotated_concepts[i].strip().split(' ')

        if a1[0] != '':
            distance = levenshtein2(a1, a2)
            edit_distance.append(distance)
        else:
            edit_distance.append(-1)

    return edit_distance

def write_edit_distance(output_file, edit_distance):
    with open(output_file, 'w') as output:
        output.writelines('%d\n' % d for d in edit_distance)

if __name__ == '__main__':
    OUTPUT_FILE = './result/result.txt'
    ORIGINAL_CONTEXT_FILE = './preprocess_test/concepts.txt'

    number_of_sentences_recognized(OUTPUT_FILE)
    edit_distance = analyse_edit_distance(OUTPUT_FILE, ORIGINAL_CONTEXT_FILE)
    write_edit_distance('./result/edit_distance.txt', edit_distance)
