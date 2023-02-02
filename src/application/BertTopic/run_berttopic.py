"""Run berttopic on acl papers titles"""
from bertopic import BERTopic
from sklearn.datasets import fetch_20newsgroups
import pandas as pd
from scipy.cluster import hierarchy as sch

nr_topics = [50, 100, 150, 200]

for nr in nr_topics:
    df = pd.read_csv("../../../data/papers/keywords_titles.csv")
    titles = df["title"].tolist()

    topic_model = BERTopic(verbose=True, nr_topics="auto")
    topics, probs = topic_model.fit_transform(titles)
    topic_model.reduce_topics(titles, nr_topics=nr)
    topic_model.get_topic_info().to_csv(
        f"../../../data/results/{nr}topics.csv", index=False
    )

    linkage_function = lambda x: sch.linkage(x, "single", optimal_ordering=True)
    hierarchical_topics = topic_model.hierarchical_topics(
        titles, linkage_function=linkage_function
    )

    fig = topic_model.visualize_hierarchy(hierarchical_topics=hierarchical_topics)
    fig.write_image(f"../../../data/results/{nr}_topics.pdf")
