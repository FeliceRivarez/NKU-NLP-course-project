from datasets import load_dataset
from tqdm import tqdm  # 导入tqdm库

# 加载wmt14德语-英语数据集
ds = load_dataset("wmt/wmt14", "de-en")

# 获取训练集的德语和英语句子
de_sentences = [item['de'] for item in ds['train']['translation']]
en_sentences = [item['en'] for item in ds['train']['translation']]
print(len(de_sentences), len(en_sentences))

# 创建句子对格式并保存到文件
output_file_en = 'val.en'
output_file_de = 'val.de'


# 使用tqdm显示进度条
f_en=open(output_file_en, 'w')
f_de=open(output_file_de, 'w')

# for de, en in tqdm(zip(de_sentences, en_sentences), total=len(de_sentences), desc="Processing sentences"):
#     # 每对句子之间用制表符分隔
#     if de.find('\n')!=-1:
#         print("!!!")
#     en=en.replace('\n', "")
#     de=de.replace('\n', "")
#     f_en.write(f"{en}\n")
#     f_de.write(f"{de}\n")

for i in range(203000,206000):
    # 每对句子之间用制表符分隔
    # if de.find('\n')!=-1:
    #     print("!!!")
    # en=en.replace('\n', "")
    # de=de.replace('\n', "")
    f_en.write(f"{en_sentences[i]}\n")
    f_de.write(f"{de_sentences[i]}\n")
    if i%10000==0:
        print(i)

overall=open("overall.txt", 'w')
# for de, en in tqdm(zip(de_sentences, en_sentences), total=len(de_sentences), desc="Processing sentences"):
#     en=en.replace('\n', "")
#     de=de.replace('\n', "")
#     overall.write(f"{en}\t{de}\n")

for i in range(len(en_sentences)):
    # 每对句子之间用制表符分隔
    # if de.find('\n')!=-1:
    #     print("!!!")
    # en=en.replace('\n', "")
    # de=de.replace('\n', "")
    overall.write(f"{en_sentences[i]}\t{de_sentences[i]}\n")


# print(f"训练集句子对数据已保存到 {output_file}")

f_en.close()
f_de.close()
overall.close()

f_en=open(output_file_en, encoding='utf-8')
f_de=open(output_file_de, encoding='utf-8')

num=0
for i in f_en:
    num+=1

for i in f_de:
    num-=1
print(num)

error=open('errors.txt','w')
num=0
overall=open("overall.txt")
for i in overall:
    num+=1
    data=i.split('\t')
    if len(data)!=2:
        print(num)
        print(data)
        error.write(f"{num}\t{data}\n")
print(num)

