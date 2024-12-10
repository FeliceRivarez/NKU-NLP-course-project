### 配置代理和虚拟环境
source /etc/network_turbo
conda activate ssmba

### 格式
增强前增强后格式都为 sentence1 \t sentence2 \n
sentence1 can be trasnlated to sentence2

### 增强示例
img 文件夹

### 原测试脚本
// in dic ssmba
``` python
python ssmba.py \
    --shard 0 \
    --num-shards 1 \
    --model bert-base-uncased \
    --tokenizer bert-base-uncased \
    --in-file test/test_en_de.txt \
    --output-prefix test/augmented_test_en_de.txt \
    --noise-prob 0.15 \
    --random-token-prob 0.1 \
    --leave-unmasked-prob 0.1 \
    --batch 8 \
    --num-samples 4 \
    --max-tries 10 \
    --min-len 4 \
    --max-len 512 \
    --topk 10
```
### 新测试脚本（将数据处理直接插入的SSMBA.py）
``` python
python ssmba.py \
    --shard 0 \
    --num-shards 1 \
    --model bert-base-uncased \
    --tokenizer bert-base-uncased \
    --in-file WMT14/train_sentence_pairs_en_de.txt \
    --output-prefix WMT14/augmented_train_sentence_pairs_en_de.txt \
    --noise-prob 0.15 \
    --random-token-prob 0.1 \
    --leave-unmasked-prob 0.1 \
    --batch 64 \
    --num-samples 4 \
    --max-tries 10 \
    --min-len 4 \
    --max-len 512 \
    --topk 10
```