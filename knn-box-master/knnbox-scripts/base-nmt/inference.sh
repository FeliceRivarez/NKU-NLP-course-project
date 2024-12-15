:<<!
[script description]: use neural machine translation model to translate 
[dataset]: multi domain DE-EN dataset
[base model]: WMT19 DE-EN
!
# this line speed up faiss. base nmt dosent need faiss, 
# we set this environment variable here just for fair comparison.
export OMP_WAIT_POLICY=PASSIVE

PROJECT_PATH=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )/../..
# DATA_PATH=$PROJECT_PATH/old/it
# BASE_MODEL=$PROJECT_PATH/pretrain-models/wmt19.de-en/wmt19.de-en.ffn8192.pt

DATA_PATH=/root/dataset/data-bin/
# BASE_MODEL=$PROJECT_PATH/newTrain/checkpoint_last.pt

BASE_MODEL=/root/autodl-tmp/selective_distillation-main/backup/checkpoint_best.pt


CUDA_VISIBLE_DEVICES=0 python $PROJECT_PATH/fairseq_cli/generate.py $DATA_PATH \
--task translation \
--path $BASE_MODEL \
--dataset-impl mmap \
--beam 4 --lenpen 0.6 --max-len-a 1.2 --max-len-b 10 --source-lang en --target-lang de \
--gen-subset test \
--model-overrides "{'eval_bleu': False, 'required_seq_len_multiple':1, 'load_alignments': False}" \
--max-tokens 2048 \
--scoring sacrebleu \
--tokenizer moses --remove-bpe \
