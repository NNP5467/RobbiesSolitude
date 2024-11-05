from typing import Tuple


def type_checking(obj: object, type: object, error_message: str) -> None:
    """
    Returns an error if the types do not match

    :param obj: object
    :param type: the type being checked
    :param error_message: error message
    """
    if not isinstance(obj, type):
        raise TypeError(error_message)
    

def types_checking(obj: object, types: Tuple[object, ...], error_message: str) -> None:
    """
    Returns an error if the types do not match

    :param obj: object
    :param types: types to be checked
    :param error_message: error message
    """
    if not isinstance(obj, types):
        raise TypeError(error_message)
