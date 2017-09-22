import sys

# quick implementation, improve later?

stations = {
        "kone": set(["id","nv","ut"]),
        "ktwo": set(["wa","id","mt"]),
        "kthree": set(["or","nv","ca"]),
        "kfour": set(["nv","ut"]),
        "kfive": set(["ca","az"])
        }


# note the values should be unique
def create_value_covered_dict(values):

    value_covered_dict = {}
    for value in values:
        value_covered_dict[value] = False

    return value_covered_dict

def coverage(curr_set, value_covered_dict):
    return len([value for value in list(curr_set) if not value_covered_dict[value]])


def find_set_with_largest_coverage(set_dict,value_covered_dict):

    items = set_dict.items()
    items.sort(key=lambda (key,value): coverage(value,value_covered_dict))
    items  = list(filter(lambda (key,value): coverage(value,value_covered_dict) > 0, items))
    if items:
        return items[-1]
    return None

# for a given dictionary of sets, set cover
# will return the sub optimal keys that cover
# the entire values
def set_cover(set_dict):

    distinct_values = list(set(reduce(lambda x,y: list(x)+list(y),set_dict.values())))
    value_covered_dict = create_value_covered_dict(distinct_values)
    sets = []
    _set  = find_set_with_largest_coverage(set_dict,value_covered_dict)
    while _set:
        sets.append(_set[0])
        values = list(_set[1])
        for value in values:
            value_covered_dict[value] = True
        _set = find_set_with_largest_coverage(set_dict,value_covered_dict)
    return sets

def main():
    print set_cover(stations)

if __name__ == "__main__":
    main()
