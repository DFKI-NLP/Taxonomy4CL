"""Pipeline for collecting abstracts, titles from acl English papers, saving them into seperate txt files with the paper acl id as a filename"""
import pandas as pd
import spacy
import spacy_fastlang
from tqdm import tqdm
import regex as re
from typing import List


nlp = spacy.load("en_core_web_lg")


def detect_en_lang(dataset: List[str], nlp, batch_size: int = 10) -> bool:
    """
    Checks which docs in the dataset are English using SpaCy language detection.
    Params:
        dataset (List[str]): A set of text docs.
        nlp: spaCy pipeline.
        batch_size (int: Optional): Number of docs to be processed at a time. By default equals to 10.
    Return:
        bool: True if English, False otherwise
    """

    if "language_detector" not in nlp.pipe_names:
        nlp.add_pipe("language_detector")

    languages = []

    for i in tqdm(range(0, len(dataset), batch_size)):
        batch = dataset[i : i + batch_size]
        docs = list(nlp.pipe(batch))

        for doc in docs:
            languages.append(doc._.language == "en")

    return languages


def check_aclid_format(acl_id: str) -> bool:
    """
    Gets whether acl id is in old (CYY-VPPP or CYY-VVPP) or new format ({year}.{venue}-{volume}.{#})
    Params:
        acl_id (str): String with acl_id
    Return:
        bool: True is the fist 2 char are letters, thus old acl format
    """
    if acl_id[:1].isalpha():
        return True
    return False


def get_venue(acl_id: str) -> str:
    """
    Gets the venue from new acl_id format of type {year}.{venue}-{volume}.{#}
    Params:
        acl_id (str): String with acl_id
    Return:
        str: acl venue
    """
    search_pattern = "\.(.*)\-"
    venue = re.search(search_pattern, acl_id).group(1)
    return venue


def main():
    df = pd.read_parquet("acl_publications.parquet")

    # filter out documents with empty abstracts, titles and acl ids
    df_filtered = df[
        (df["abstract"] != "") & (df["title"] != "") & (df["acl_id"] != "")
    ]

    # filter out papers published before 2016
    df_filtered = df_filtered[df_filtered["year"].astype(int) >= 2016]

    # filter out non English papers
    lang_abstracts = detect_en_lang(
        df_filtered["abstract"].tolist(), nlp, batch_size=50
    )
    df_filtered["abstract_lang"] = lang_abstracts

    lang_titles = detect_en_lang(df_filtered["title"].tolist(), nlp, batch_size=50)
    df_filtered["title_lang"] = lang_titles

    english_papers = df_filtered[
        (df_filtered["title_lang"] == True) & (df_filtered["abstract_lang"] == True)
    ]

    english_papers = english_papers.reset_index(drop=True)

    # get venues and build a dataset with randomply selected docs with (almost) equal nub of papers per paper
    english_papers["venue"] = english_papers.apply(
        lambda row: get_venue(row["acl_id"])
        if check_aclid_format(row["acl_id"]) == False
        else row["acl_id"][:3],
        axis=1,
    )

    # we want to have 1500 docs in the dataset
    # define the min docs per venue

    min_numb = 1500 / len(english_papers["venue"].unique())
    dataset = english_papers.groupby("venue").apply(
        lambda x: x.sample(min(round(min_numb), len(x))).reset_index(drop=True)
    )

    # remove any brackets from the text

    dataset = dataset["title"].apply(lambda x: re.sub(r"[\([{})\]]", "", x))
    dataset = dataset["abstract"].apply(lambda x: re.sub(r"[\([{})\]]", "", x))

    # add special token to the text and save it with the acl id as a filename
    for index, row in dataset.iterrows():
        with open(f'papers_to_annotate/{row["acl_id"]}.txt', "w") as f:
            f.write("TITLE " + f'{row["title"]}' + " TITLE" + "\n")
            f.write("ABSTRACT " + f'{row["abstract"]}' + " ABSTRACT")


if __name__ == "__main__":
    main()
