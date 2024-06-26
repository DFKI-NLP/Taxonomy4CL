"""Pipeline for preparing a csv with annotations and metadata"""
import xml.etree.ElementTree as ET
import os
import re
import pandas as pd
import numpy as np


# Note that first all curation files should be unzipped
# Command for mac:
# find . -name "*.zip" | while read filename; do unzip -o -d "`dirname "$filename"`" "$filename"; done;


def get_xmi_file_paths(main_path: str):
    """Finds all xmi files in a given directory and its subdirectories
    Args:
        main_path (str): The path to the main directory.
    Returns:
        List: list of xmi files with their full path.
    """
    return [
        os.path.join(root, file)
        for root, dirs, files in os.walk(main_path)
        for file in files
        if file.endswith(".xmi")
    ]

def main():
    
    MAIN_PATH = ""

    xmi_files = get_xmi_file_paths(MAIN_PATH)
    xmi_files

    # get labels per level per doc
    # create dict of type [{'acl id': [{'Level1': 'label'},
    #                                  {'Level2': label},]},
    #                      {'acl_id': [{'Level1': 'label'},
    #                                  {'Level3': 'label'}]}]


    curation = []

    for file in xmi_files:
        acl_id = re.search(r"\/([^/]+)\.txt", file).group(1)

        lables = []
        tree = ET.parse(file)
        root = tree.getroot()

        for child in root:
            if "FoRhierarchy" in child.tag:
                for key, value in child.attrib.items():
                    if "Level" in key:
                        lables.append({key: value})

        curation.append({acl_id: list(lables)})

    data = []

    for item in curation:
        for id, value in item.items():
            level1 = []
            level2 = []
            level3 = []
            for element in value:
                for key, value in element.items():
                    if key == "Level1":
                        level1.append(value)
                    elif key == "Level2":
                        level2.append(value)
                    else:
                        level3.append(value)

            data.append(
                {
                    "acl_id": id,
                    "Level1": list(set(level1)),
                    "Level2": list(set(level2)),
                    "Level3": list(set(level3)),
                }
            )

    df = pd.DataFrame(data)
    df = df.applymap(lambda x: np.nan if isinstance(x, list) and len(x) == 0 else x)

    df.to_csv("annotated_data.csv", index=False)

    path_to_acl_data = ""

    raw_acl_corpus = pd.read_csv(
        path_to_acl_data,
        usecols=[
            "acl_id",
            "abstract",
            "url",
            "publisher",
            "year",
            "month",
            "booktitle",
            "author",
            "title",
            "doi",
            "venue",
        ],
    )
    final_data = pd.merge(df, raw_acl_corpus, on="acl_id", how="left")
    final_data.to_csv("FoRC4CL.csv", index=False)

if __name__ == "__main__":
    main()