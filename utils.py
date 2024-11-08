from typing import Tuple


def types_checking(obj: Tuple[object, ...],
                   types: Tuple[object | Tuple[object, ...], ...]) -> None:
    if len(obj) != len(types):
        ValueError("Unequal number of objects in the parameters")

    for i in range(len(obj)):
        if not isinstance(obj[i], types[i]):
            TypeError(f"The type of variable {obj.__name__} does not match the proper type!")
