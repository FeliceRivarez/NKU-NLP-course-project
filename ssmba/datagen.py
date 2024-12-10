from datasets import load_dataset
from tqdm import tqdm
import random  # 导入random库

# 加载wmt14德语-英语数据集
ds = load_dataset("wmt/wmt14", "de-en")

# 获取训练集的德语和英语句子
de_sentences = [item['de'] for item in ds['train']['translation']]
en_sentences = [item['en'] for item in ds['train']['translation']]

# 抽取 30,000 行随机样本
sample_size = 30000
sampled_indices = random.sample(range(len(de_sentences)), sample_size)  # 随机选择 30,000 个索引

# 根据随机选择的索引获取句子
sampled_de_sentences = [de_sentences[i] for i in sampled_indices]
sampled_en_sentences = [en_sentences[i] for i in sampled_indices]

print(f"从训练集中随机抽取了 {len(sampled_de_sentences)} 行")

# 创建句子对格式并保存到文件
output_file = 'train_sentence_pairs_en_de_sampled.txt'

# 使用tqdm显示进度条
with open(output_file, 'w', encoding='utf-8') as f:
    for en, de in tqdm(zip(sampled_en_sentences, sampled_de_sentences), total=sample_size, desc="Processing sentences"):
        # 每对句子之间用制表符分隔
        f.write(f"{en}\t{de}\n")

print(f"训练集句子对数据已随机抽样并保存到 {output_file}")
