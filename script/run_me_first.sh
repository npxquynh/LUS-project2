# go to main folder
cd ../

python main.py lexicon

PREFIX="./tmp_file/";
LEXICON="${PREFIX}cutoff_lexicon.txt";
CONCEPT_LEXICON=./files_from_outside/concept_lexicon.txt;

cat ./MT2_Data/ATIS.train.txt |
farcompilestrings -u 'null' -i $LEXICON |
farprintstrings -o $LEXICON > ./MT2_Data/cutoff_ATIS.train.txt;

python main.py rowize_dataset
python main.py fst

cd ./script/

# You can change the below line to run the cutoff_script.sh
bash cutoff_script.sh