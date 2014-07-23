# cd /media/quynh/DATA/Courses/Language\ Understanding\ System/project2

cd ../

# make necessary directory
mkdir -p preprocess_train
mkdir -p preprocess_test
mkdir -p result
mkdir -p tmp_file

PREFIX="./tmp_file/";
LEXICON="${PREFIX}lexicon.txt";
CONCEPT_LEXICON=./files_from_outside/concept_lexicon.txt;

G_FSM="${PREFIX}g.fsm";
W2C_FSM="${PREFIX}w2c.fsm";
G_FST="${PREFIX}g.fst";
W2C_FST="${PREFIX}w2c.fst";

TRAIN_FILE="./preprocess_train/mixed.txt";
TRAIN_FAR="${PREFIX}train.far";
TRAIN_FAR_FINAL="${PREFIX}train_final.far";
TRAIN_COUNT="${PREFIX}train.count";
TRAIN_LM="${PREFIX}train.lm";
TRAIN_ELM="${PREFIX}train.elm";

TEST_FILE="./preprocess_test/sentences.txt";

# Step 1
farcompilestrings -u '<unk>' -i $LEXICON $TRAIN_FILE > $TRAIN_FAR

# Step 2
fsmcompile -i $LEXICON -o $LEXICON -t $G_FSM > $G_FST
# farfilter "fsmcompose - $G_FST"< $TRAIN_FAR > "${PREFIX}train_2.far";
# farfilter "fsmcompose - $G_FST | fsmbestpath | fsmrmepsilon"< $TRAIN_FAR > "${PREFIX}train_2.far";

# Step 3
fsmcompile -i $LEXICON -o $LEXICON -t $W2C_FSM > $W2C_FST;
# farfilter "fsmcompose - $W2C_FST"< "${PREFIX}train_2.far" > $TRAIN_FAR_FINAL;
# farfilter "fsmcompose - $W2C_FST | fsmbestpath | fsmrmepsilon"< "${PREFIX}train_2.far" > $TRAIN_FAR_FINAL;

# Step 4
grmcount -i $LEXICON -n 2 -s '<s>' -f '</s>' $TRAIN_FAR > $TRAIN_COUNT
grmmake -n 2 $TRAIN_COUNT > $TRAIN_LM
grmconvert -i $LEXICON -f '<epsilon>' $TRAIN_LM > $TRAIN_ELM

# Step 5 - run the refined SCLM with the test set
farcompilestrings -u '<unk>' -i $LEXICON $TEST_FILE > ./result/test1.far
# farfilter "fsmcompose - $G_FST" < ./result/test1.far > ./result/test2.far
# farfilter "fsmcompose - $W2C_FST" < ./result/test2.far > ./result/test3.far

farfilter "fsmcompose - $G_FST $W2C_FST $TRAIN_ELM | fsmbestpath | fsmrmepsilon" < ./result/test1.far > ./result/test4.far
# farfilter "fsmcompose - $G_FST $W2C_FST | fsmbestpath | fsmrmepsilon" < ./result/test1.far > ./result/test2.far
# farfilter "fsmcompose - $TRAIN_ELM | fsmbestpath | fsmrmepsilon" < ./result/test2.far > ./result/test4.far
farprintstrings -o $LEXICON ./result/test4.far > ./result/test4.txt

# Step 6 - map all 'non-concept' terminals to 'null'
cat ./result/test4.txt | farcompilestrings -u 'null' -i $CONCEPT_LEXICON > ./result/result.far
farprintstrings -o $CONCEPT_LEXICON ./result/result.far > ./result/result.txt

# Step 7 - show result of running the SCLM with the test set
python concept_analysis.py

################
# Code to test
################
# farprintstrings -o $LEXICON $TRAIN_FAR > "${PREFIX}train.txt";
# farprintstrings -o $LEXICON "${PREFIX}train_2.far" > "${PREFIX}train_2.txt";
# farprintstrings -o $LEXICON $TRAIN_FAR_FINAL > "${PREFIX}train_final.txt";

# farprintstrings -o $LEXICON ./result/test2.far > ./result/test2.txt
# farprintstrings -o $LEXICON ./result/test3.far > ./result/test3.txt