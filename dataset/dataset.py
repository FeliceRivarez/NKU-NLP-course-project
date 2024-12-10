from datasets import load_dataset
from tqdm import tqdm  # 导入tqdm库

# 加载wmt14德语-英语数据集
ds = load_dataset("wmt/wmt14", "de-en")

# 获取训练集的德语和英语句子
de_sentences = [item['de'] for item in ds['train']['translation']]
en_sentences = [item['en'] for item in ds['train']['translation']]
print(len(de_sentences), len(en_sentences))

# 创建句子对格式并保存到文件
output_file = 'train_sentence_pairs.txt'

# 使用tqdm显示进度条
with open(output_file, 'w', encoding='utf-8') as f:
    for de, en in tqdm(zip(de_sentences, en_sentences), total=len(de_sentences), desc="Processing sentences"):
        # 每对句子之间用制表符分隔
        f.write(f"{de}\t{en}\n")

print(f"训练集句子对数据已保存到 {output_file}")