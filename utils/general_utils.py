""""Provides general helper functions"""
import inspect
from utils.exceptions import GeneralUtilsException
from itertools import chain


def variable_name(var):
    """prints out the variable name as a string. Note that this does not work within functions :/"""
    try:
        callers_local_vars = list(inspect.currentframe().f_back.f_locals.items())
        return [var_name for var_name, var_val in callers_local_vars if var_val is var][0]
    except Exception as e:
        raise GeneralUtilsException('The variable_name function failed with the following error - {0}'.format(e))


def intersect(*d):
    """finds the intersection between any number of provided lists"""
    try:
        sets = iter(map(set, d))
        result = next(sets)
        for s in sets:
            result = result.intersection(s)
        return list(result)
    except Exception as e:
        raise GeneralUtilsException('The intersect function failed with the following error - {0}'.format(e))


def list_diff(l1, l2):
    """finds the difference/ between two lists"""
    try:
        list_diff = list(set(l1) - set(l2))
        return list_diff
    except Exception as e:
        raise GeneralUtilsException('The list_diff function failed with the following error - {0}'.format(e))


def add_lists(*d):
    """finds the difference/ between two lists"""
    try:
        return list(chain(*d))
    except Exception as e:
        raise GeneralUtilsException('The add_list function failed with the following error - {0}'.format(e))


def intersect_specific(l1, l2, keep_list):
    return [x for x in intersect(l1, l2) if x in keep_list]











