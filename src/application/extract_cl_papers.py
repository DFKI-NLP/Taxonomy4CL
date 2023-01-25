"""Extract only CL papers from arXive data"""

import pandas as pd

df = pd.read_json("../../data/arxiv-metadata-oai-snapshot.json", lines=True)
categories = df.categories.unique().tolist()
labels = [category for category in categories if "cs.CL" in category]
data = df.loc[df['categories'].isin(labels)]
data.to_csv("../../data/CL_papers.csv", index=False)