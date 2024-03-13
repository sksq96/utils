from openai import OpenAI
client = OpenAI()

def embed(texts):
    texts = list(texts)
    model = "text-embedding-3-small"
    res = client.embeddings.create(input = texts, model=model)
    return np.array([r.embedding for r in res.data])
