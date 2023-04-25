"""Pipeline for collecting abstracts, titles from acl English papers, saving them into seperate txt files with the paper acl id as a filename"""
import pandas as pd
import spacy
import spacy_fastlang


nlp = spacy.load("en_core_web_lg")

def is_english(text: str) -> bool:
    """
    Checks if a text is in English using SpaCy language detection.
    Params:
        text: A srting with the text to be checked
    Return:
        bool:True if the input text is in English, False otherwise
    """
    nlp.add_pipe("language_detector")
    doc = nlp(text)
    return doc._.language == "en"


def main():
    df = pd.read_parquet("acl_publications.parquet")

    df_filtered = df[
        (df["abstract"] != "") & (df["title"] != "") & (df["acl_id"] != "")
    ]
    df_filtered= df_filtered[df_filtered["year"].astype(int)>=2016]
    df_filtered["is_english_title"] = [is_english(text) for text in df_filtered["title"]]
    df_filtered["is_english_abstract"] = [is_english(text) for text in df_filtered["abstract"]]

    english_papers = df_filtered[
        (df_filtered["is_english_title"] == True) & (df_filtered["is_english_abstract"] == True)
        ]
    

    english_papers = english_papers.reset_index(drop=True)
    sample_set = english_papers.sample(n=50)

    for index, row in sample_set.iterrows():
        with open(f'papers_to_annotate/{row["acl_id"]}.txt', "w") as f:
            f.write("TITLE " + f'{row["title"]}' + " TITLE" + "\n")
            f.write("ABSTRACT " + f'{row["abstract"]}' + " ABSTRACT")


if __name__ == "__main__":
    main()
