#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    set_1_2 = set_1.difference(set_2)
    set_2_1 = set_2.difference(set_1)
    return set_1_2.union(set_2_1)
