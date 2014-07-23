# go to main folder
cd ../

python main.py lexicon

PREFIX="./tmp_file/";

CUTOFF_LEXICON="${PREFIX}cutoff_lexicon.txt";
cat ./MT2_Data/ATIS.train.txt |
farcompilestrings -u 'null' -i $CUTOFF_LEXICON |
farprintstrings -o $CUTOFF_LEXICON > ./MT2_Data/cutoff_ATIS.train.txt;

REFINED_CUTOFF_LEXICON="${PREFIX}refined_cutoff_lexicon.txt";
cat ./MT2_Data/ATIS.train.txt |
farcompilestrings -u 'null' -i $REFINED_CUTOFF_LEXICON |
farprintstrings -o $REFINED_CUTOFF_LEXICON > ./MT2_Data/refined_cutoff_ATIS.train.txt;

python main.py rowize_dataset
python main.py fst

cd ./script/

# You can change the below line to run the cutoff_script.sh
bash script.sh
# bash cutoff_script.sh
# bash refined_cutoff_script.sh