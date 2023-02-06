"""Run bertopic on acl titles/abstracts"""
from bertopic import BERTopic
import pandas as pd
from scipy.cluster import hierarchy as sch

nr_topics = [50, 100, 150, 200]
labels = ["title", "abstract"]

for label in labels:
    df = pd.read_csv(f"../../../data/papers/keywords_{label}s.csv")
    docs = df[label].tolist()
    for nr in nr_topics:
        topic_model = BERTopic(verbose=True)
        topics, probs = topic_model.fit_transform(docs)
        topic_model.reduce_topics(docs, nr_topics=nr)
        topic_model.get_topic_info().to_csv(
            f"../../../data/results/csv/{label}s_{nr}_topics.csv", index=False
        )

        linkage_function = lambda x: sch.linkage(x, "single", optimal_ordering=True)
        hierarchical_topics = topic_model.hierarchical_topics(
            docs, linkage_function=linkage_function
        )

        intertopic_map = topic_model.visualize_topics()
        intertopic_map.write_html(
            f"../../../data/results/html/{label}s_intertopic_map_{nr}_topics.html"
        )
        intertopic_map.write_image(
            f"../../../data/results/pdf/{label}s_intertopic_map_{nr}_topics.html"
        )

        hierarchy_fig = topic_model.visualize_hierarchy(
            hierarchical_topics=hierarchical_topics
        )
        hierarchy_fig.write_html(
            f"../../../data/results/html/hierarchy_{label}s_{nr}_topics.html"
        )

        hierarchy_fig.write_image(
            f"../../../data/results/pdf/hierarchy_{label}s_{nr}_topics.html"
        )
