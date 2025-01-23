import os
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

from sentence_transformers import SentenceTransformer

# 加载预训练模型
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# 要编码的句子
sentences = ['Python is an interpreted high-level general-purpose programming language.',
'Python is dynamically-typed and garbage-collected.',
'The quick brown fox jumps over the lazy dog.']

# 获取句子的嵌入向量
embeddings = model.encode(sentences)

# 打印嵌入向量
for sentence, embedding in zip(sentences, embeddings):
    print("Sentence:", sentence)
    print("Embedding:", embedding)
    print("")