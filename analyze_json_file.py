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


def analyze_dict(dct: object):
    """
    Analyzes the dict
    :param dct: dictionary, which we want to analyze
    :return: True
    """
    temp = [dct]
    while temp:
        sub_elem = temp[-1]
        if isinstance(sub_elem, list):
            print("There are available indexes in range of {}"
                  .format(len(sub_elem)))
        elif isinstance(sub_elem, dict):
            print("There are available keys of dict:\n{}"
                  .format('\n'.join([el for el in sub_elem])))
        else:
            print(sub_elem)
        key = input("Enter the command or the key/index value,"
                    " which u want to look for: ")
        if key == 'PRINT':
            print(temp[-1])
        elif key == 'ESCAPE':
            print("Hope u enjoyed using this program...")
            return True
        elif key == 'BACK':
            temp.pop()
            continue
        elif key.isdigit():
            temp.append(sub_elem[int(key)])
        else:
            temp.append(sub_elem[key])
    print("Hope u enjoyed this program")


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
        elif var == '2':
            commands_text = "LIST of commands:\n" +\
                            "1) to print the current object," \
                            " please type 'PRINT'\n" +\
                            "2) to get back, please type 'BACK'\n" + \
                            "3) to escape from program, type 'ESCAPE'\n"
            print(commands_text)
            analyze_dict(dct_from_json)
        else:
            print("There is no more variants of realization, sorry")
    except (KeyError, ValueError, IndexError):
        print("Enter the true value of key/index!")


if __name__ == "__main__":
    main('form.json')