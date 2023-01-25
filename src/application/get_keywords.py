import pandas as pd
import spacy
import pytextrank


data = pd.read_csv("../../data/CL_papers.csv")

keywords_titles = pd.DataFrame(columns = ["title", "keywords", "ranks", "counts"])
titles = data["title"].tolist()
titles = [title for title in titles if title != ""]
keywords_titles["title"] = titles

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("textrank")

keywords = []
ranks = []
counts = []

for title in titles:
    doc = nlp(title)

    title_keywords = []
    title_ranks = []
    title_counts = []
    
    for phrase in doc._.phrases:
        title_keywords.append(phrase.text)
        title_ranks.append(phrase.rank)
        title_counts.append(phrase.count)
    keywords.append(title_keywords)
    ranks.append(title_ranks)
    counts.append(title_counts)

keywords_titles["keywords"] = keywords
keywords_titles["ranks"] = ranks
keywords_titles["counts"] = counts

keywords_titles.to_csv("../../data/keywords_titles.csv", index=False)