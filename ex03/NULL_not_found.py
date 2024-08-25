import math


def NULL_not_found(object: any) -> int:
    """
    Finds and prints the corresponding null value
    type for the given object.

    Parameters:
    object (any): The object for which to
    find its null value type.

    Returns:
    int: 0 if the null value type was found and
    printed successfully, 1 if not found.
    """
    type_names = {
        None: "Nothing",
        math.nan: "Cheese",
        48: "Zero",
        '': "Empty",
        False: "Fake"
    }

    type_name = type_names.get(object, "Type not Found")

    if type(object) is float and math.isnan(object):
        print(f"Cheese: {object} {type(object)}")
    elif object == 0 and type(object) is int:
        print(f"Zero: {object} {type(object)}")
    elif type_name != "Type not Found":
        print(f"{type_name}: {object} {type(object)}")
    else:
        print("Type not found")
        return 1
    return 0
