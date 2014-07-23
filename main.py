import sys

from preprocess_data import *
import lexicon_operation as lex
import transducer_operation as td

TRAINING_FILE   = './MT2_Data/ATIS.train.txt'
CUTOFF_TRAINING_FILE   = './MT2_Data/cutoff_ATIS.train.txt'
REFINED_CUTOFF_TRAINING_FILE   = './MT2_Data/refined_cutoff_ATIS.train.txt'
TESTING_FILE    = './MT2_Data/ATIS.test.txt'

LEX_FILE                = './tmp_file/lexicon.txt'
CUTOFF_LEX_FILE         = './tmp_file/cutoff_lexicon.txt'
REFINED_CUTOFF_LEX_FILE = './tmp_file/refined_cutoff_lexicon.txt'

G_FILE          = './tmp_file/g.fsm'
W2C_FILE        = './tmp_file/w2c.fsm'

G_CUTOFF_FILE          = './tmp_file/cutoff_g.fsm'
W2C_CUTOFF_FILE        = './tmp_file/cutoff_w2c.fsm'

G_REFINED_CUTOFF_FILE          = './tmp_file/refined_cutoff_g.fsm'
W2C_REFINED_CUTOFF_FILE        = './tmp_file/refined_cutoff_w2c.fsm'

OUTPUT_FILE = './result/result.txt'
ORIGINAL_CONTEXT_FILE = './preprocess_test/2.txt'

def prepare_set_of_lexicon():
    # Step 1: generate lexicon
    lexicon = lex.generate_lexicon_from_textfile(TRAINING_FILE)
    lex.write_lexicon_to_file(LEX_FILE, lexicon)

    cutoff_lexicon = lex.generate_cutoff_lexicon(lexicon, './files_from_outside/english.stop.txt')
    lex.write_lexicon_to_file(CUTOFF_LEX_FILE, cutoff_lexicon)

    refined_cutoff_lexicon = lex.generate_refined_cutoff_lexicon(lexicon, './files_from_outside/english.stop.txt')
    lex.write_lexicon_to_file(REFINED_CUTOFF_LEX_FILE, refined_cutoff_lexicon)

def preprocess_dataset():
    # Step 0: preprocess training data & testing data
    new_output_files = ['sentences.txt', 'word_categories.txt', 'concepts.txt', 'mixed.txt']
    Preprocess_Data(TRAINING_FILE, './preprocess_train/', new_output_files)
    Preprocess_Data(TESTING_FILE, './preprocess_test/', new_output_files)

    Preprocess_Data(CUTOFF_TRAINING_FILE, './preprocess_train/cutoff_', new_output_files)
    Preprocess_Data(REFINED_CUTOFF_TRAINING_FILE, './preprocess_train/refined_cutoff_', new_output_files)

def prepare_transducer():
    # Step 2: From words --> word categories
    temp = td.step_2(TRAINING_FILE)
    td.write_transducer(G_FILE, temp)

    temp = td.step_2(CUTOFF_TRAINING_FILE)
    td.write_transducer(G_CUTOFF_FILE, temp)

    temp = td.step_2(REFINED_CUTOFF_TRAINING_FILE)
    td.write_transducer(G_REFINED_CUTOFF_FILE, temp)

    # Step 3: From words/word categories --> concepts
    temp = td.step_3(TRAINING_FILE)
    td.write_transducer(W2C_FILE, temp)

    temp = td.step_3(CUTOFF_TRAINING_FILE)
    td.write_transducer(W2C_CUTOFF_FILE, temp)

    temp = td.step_3(REFINED_CUTOFF_TRAINING_FILE)
    td.write_transducer(W2C_REFINED_CUTOFF_FILE, temp)

def main(function_type):
    if (function_type == 'lexicon'):
        prepare_set_of_lexicon()
    elif (function_type == 'rowize_dataset'):
        preprocess_dataset()
    elif (function_type == 'fst'):
        prepare_transducer()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        preprocess_dataset()
        prepare_transducer()