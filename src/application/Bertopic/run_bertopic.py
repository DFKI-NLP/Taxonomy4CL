"""Run bertopic on titles/abstracts from arXiv papers tages as cs.CL"""
from bertopic import BERTopic
import pandas as pd
from scipy.cluster import hierarchy as sch
from umap import UMAP

labels = ["title", "abstract"]

for label in labels:
    df = pd.read_csv(f"../../../data/papers/{label}s.csv")
    docs = df[label].tolist()
    umap_model = UMAP(random_state=42)
    topic_model = BERTopic(umap_model=umap_model)
    topics, probs = topic_model.fit_transform(docs)
   
    topic_model.get_topic_info().to_csv(
            f"../../../data/results/csv/{label}s_topics.csv", index=False
        )
    topic_model.get_document_info(docs).to_csv(f"../../../data/results/csv/doc_info_{label}s.csv", index=False)

    linkage_function = lambda x: sch.linkage(x, "single", optimal_ordering=True)
    hierarchical_topics = topic_model.hierarchical_topics(
            docs, linkage_function=linkage_function
        )

    intertopic_map = topic_model.visualize_topics()
    intertopic_map.write_html(
            f"../../../data/results/html/{label}s_intertopic_map.html"
        )
    intertopic_map.write_image(
            f"../../../data/results/pdf/{label}s_intertopic_map.html"
        )

    hierarchy_fig = topic_model.visualize_hierarchy(
            hierarchical_topics=hierarchical_topics
        )
    hierarchy_fig.write_html(
            f"../../../data/results/html/hierarchy_{label}s.html"
        )

    hierarchy_fig.write_image(
            f"../../../data/results/pdf/hierarchy_{label}s.html"
        )
