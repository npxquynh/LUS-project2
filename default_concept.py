def all_possible_concepts():
    CONCEPT_FILENAME = './files_from_outside/concepts.txt'
    concepts = set()
    with open(CONCEPT_FILENAME) as f:
        for line in f:
            concepts.add(line.strip())

    return concepts