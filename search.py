from tqdm import tqdm
from sentence_transformers import SentenceTransformer, util
from autofaiss import build_index

import sys

spacefile = sys.argv[1]
queryfile = sys.argv[2]


# read the embedding space text file
space = set()
with open(spacefile, 'r') as f:
    for line in tqdm(f):
        space.add(line.strip())
space = list(space)
print('space size:', len(space))


# read the query text file
query = set()
with open(queryfile, 'r') as f:
    for line in tqdm(f):
        query.add(line.strip())
query = list(query)
print('query size:', len(query))



model = SentenceTransformer('all-MiniLM-L6-v2', device='cuda')

embeddings = model.encode(space, batch_size=64, show_progress_bar=True)
print('embedding size:', len(embeddings))

queries = model.encode(query, batch_size=64, show_progress_bar=True)
print('query size:', len(queries))


index, index_infos = build_index(embeddings, save_on_disk=True)
scores, indicies = index.search(queries, 1)

with open(sys.argv[3], 'w') as f:
    for i, (score, idx) in enumerate(zip(scores, indicies)):
        print(query[i], space[idx[0]], score[0], sep='\t', file=f)


