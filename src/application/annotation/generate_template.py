def levels_template(item:dict, i:int, subitem:dict, high_level_numb:str, low_level_numb:str) -> str:
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
    
    if i==0:           
        return f'Level{high_level_numb}="{item["name"]}" -> Level{low_level_numb}="{subitem["name"]}"'
    else:
        return f' | Level{low_level_numb}="{subitem["name"]}"'
    