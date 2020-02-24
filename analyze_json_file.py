import pprint
import json


def get_key_values(data: dict, target: str) -> list:
    """
    Returns all values in dict depending on the key
    :param data: dict, in which values will be looked for
    :param target: value of the key
    :return: list of all found values
    """
    temp = []

    def dfs_get_values(parent: object, target):
        if isinstance(parent, dict):
            for key in parent:
                if key == target:
                    temp.append(parent[key])
                else:
                    dfs_get_values(parent[key], target)
        if isinstance(parent, list):
            for item in parent:
                dfs_get_values(item, target)
    dfs_get_values(data, target)
    return temp


def get_dict_from_json(json_file_path: str) -> dict:
    """
    Transforms json file to dict
    :param json_file_path: path to json file
    :return: transformed dictionary
    """
    with open(json_file_path, mode='r') as f:
        data = json.load(f)
    return data


def analyze_dict(sub_elem: object):
    """
    Analyzes the dict
    :param sub_elem: subdict or a sublist in which we are searching for a value
    :return: bool
    """
    if isinstance(sub_elem, list):
        print("There are available indexes in range of {}"
              .format(len(sub_elem)))
    elif isinstance(sub_elem, dict):
        print("There are available keys of dict: {}"
              .format(', '.join([el for el in sub_elem])))
    else:
        print(sub_elem)
        return True
    key = input("Enter the key/index to search: ")
    if key == 'ESCAPE':
        print(sub_elem)
        return True
    if key.isdigit():
        analyze_dict(sub_elem[int(key)])
    else:
        analyze_dict(sub_elem[key])


def main(path: str):
    """
    Runs a program which is used for analysing json files
    :return: None
    """
    dct_from_json = get_dict_from_json('form.json')
    opening_text = "Enter the variant of realization:\n"\
                   + "If u know the key and want to search" \
                     " for all values by this key, enter '1'\n" +\
                   "If u want to search for values step by step, enter '2'\n: "
    var = input(opening_text)
    try:
        if var == '1':
            key = input("Enter the key value: ")
            print(get_key_values(dct_from_json, key))
        if var == '2':
            print("In order to print the current object, please type 'ESCAPE'")
            analyze_dict(dct_from_json)
        else:
            print("There is no more variants of realization, sorry")
    except (KeyError, ValueError, IndexError):
        print("Enter the true value of key/index!")


if __name__ == "__main__":
    main('form.json')