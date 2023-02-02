"""Extract keywords from titles and abstracts using textrank"""
import pandas as pd
import spacy
import pytextrank

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("textrank")

data = pd.read_csv("../../../data/papers/CL_papers.csv")
labels = ["title", "abstract"]


for label in labels:
    df_keywords = pd.DataFrame(columns=[label, "keywords"])

    keywords = []

    docs = data[label].tolist()
    docs = [doc for doc in docs if doc != ""]
    df_keywords[label] = docs

    for text in docs:
        doc = nlp(text)

        keywords_doc = []
        for phrase in doc._.phrases:
            keywords_doc.append(phrase.text)
        keywords.append(keywords_doc)

    df_keywords["keywords"] = keywords
    df_keywords.to_csv(f"../../../data/papers/keywords_{label}s.csv", index=False)
