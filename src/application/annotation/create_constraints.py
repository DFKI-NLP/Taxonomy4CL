"""Pipeline for creating the constraints file for INCEpTION"""
import json


def levels_template(
    item: dict, i: int, subitem: dict, high_level_numb: str, low_level_numb: str
) -> str:
    """Creates a template string depending on the number of elements in a subitem

    if 1 element:
    '''
    Level_N="NAME" -> Level_n="NAME";
    '''

    if >1 element:
    '''
    Level_N="NAME" -> Level_n="NAME" | Level_n="NAME" | ... | Level_n="NAME;
    '''
    """

    if i == 0:
        return f'Level{high_level_numb}="{item["name"]}" -> Level{low_level_numb}="{subitem["name"]}"'
    else:
        return f' | Level{low_level_numb}="{subitem["name"]}"'


file = open("../data/taxonomy/taxonomy_v1.0.0.json")
data = json.load(file)
header = "import webanno.custom.NLP_Taxonomy as NLP_Taxonomy;\nNLP_Taxonomy {\n"


def main():
    with open("hierarchy_constraints.txt", "a") as f:
        f.write(header)
        for item in data["children"]:
            if "children" in item:
                temp_str = ""
                temp = ""

                for i, subitem in enumerate(item["children"]):
                    temp_str += levels_template(
                        item, i, subitem, high_level_numb="1", low_level_numb="2"
                    )
                    if "children" in subitem:
                        for i, child in enumerate(subitem["children"]):
                            temp += levels_template(
                                subitem,
                                i,
                                child,
                                high_level_numb="2",
                                low_level_numb="3",
                            )
                        temp += ";\n"
                temp_str += ";\n"
                f.write(temp_str)

                if len(temp) != 0:
                    f.write(temp)

            else:
                f.write(f'Level1="{item["name"]}" -> Level2="None";\n')

        f.write("}")


if __name__ == "__main__":
    main()
