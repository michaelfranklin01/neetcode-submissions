from typing import Dict, List

def remove_keys(my_dict: Dict[str, int], keys: List[str]) -> Dict[str, int]:

    # This case pop is more concise
    # for key in keys:
    #     my_dict.pop(key, 0)
    # return my_dict

    # can use the del keyword but need to check membership first:
    for key in keys:
        if key in my_dict:
            del my_dict[key]
    return my_dict





# do not modify below this line
print(remove_keys({"a": 1, "b": 2, "c": 3}, ["a", "c"]))
print(remove_keys({"a": 1, "b": 2, "c": 3}, ["d"]))
