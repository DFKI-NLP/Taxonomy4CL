import pandas as pd
from sentence_transformers import SentenceTransformer, util
import ast

data = pd.read_csv("../../data/keywords_titles.csv")
data["keywords"] = data["keywords"].apply(lambda x: ast.literal_eval(x))
corpus = data["keywords"][:100].tolist()
corpus = [doc for l in test for doc in l]

model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
corpus_embeddings = model.encode(corpus, batch_size=64, show_progress_bar=True, convert_to_tensor=True)
clusters = util.community_detection(corpus_embeddings, min_community_size=25, threshold=0.75)

for i, cluster in enumerate(clusters):
    print("\nCluster {}, #{} Elements ".format(i+1, len(cluster)))
    for sentence_id in cluster[0:max]:
        print("\t", corpus[sentence_id])
    print("\t", "...")