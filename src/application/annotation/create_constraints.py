"""Pipeline for creating the constraints txt file for inception"""
import json
from generate_template import levels_template


file = open("../visualisation/collapsibletree/taxonomy.json")
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
                    temp_str += levels_template(item, i, subitem, high_level_numb="1", low_level_numb="2")
                    if "children" in subitem:
                        for i, child in enumerate(subitem["children"]):
                            temp += levels_template(subitem, i, child, high_level_numb="2", low_level_numb="3")   
                        temp += ";\n"      
                temp_str+=";\n"
                f.write(temp_str) 

                if len(temp)!=0:
                    f.write(temp) 
                
            else:
                f.write(f'Level1="{item["name"]}" -> Level2="None";\n')

        f.write("}")

if __name__ == "__main__":
    main()