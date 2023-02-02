"""Cluster keywords based on embeddings"""
import pandas as pd
from sentence_transformers import SentenceTransformer, util
import ast

data = pd.read_csv("../../../data/papers/keywords_titles.csv")
data["keywords"] = data["keywords"].apply(lambda x: ast.literal_eval(x))
keywords = data["keywords"][:100].tolist()
keywords = [keyword for doc in keywords for keyword in doc]

model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)
corpus_embeddings = model.encode(
    keywords, batch_size=64, show_progress_bar=True, convert_to_tensor=True
)

min_community_size = 10
min_community_size = min(min_community_size, len(corpus_embeddings))
clusters = util.community_detection(
    corpus_embeddings, min_community_size=min_community_size, threshold=0.75
)

for i, cluster in enumerate(clusters):
    print("\nCluster {}, #{} Elements ".format(i + 1, len(cluster)))
    for sentence_id in cluster[0:max]:
        print("\t", keywords[sentence_id])
    print("\t", "...")
