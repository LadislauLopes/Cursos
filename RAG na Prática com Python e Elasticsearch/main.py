from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

sentences = ["carro rápido", "automóvel veloz",'fast car','very agile car','速い車']

embeddings = model.encode(sentences)

similaridade = util.cos_sim(embeddings[0], embeddings[4])

print(similaridade)

