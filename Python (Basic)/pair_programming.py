'''
1. Set Union
first_set.union(second_set), first_set | second_set

2. Set Intersection
first_set.intersection(second_set), first_set & second_set

3. Set Difference
>>> first_set = {1, 2, 3, 4, 5, 6}
>>> second_set = {4, 5, 6, 7, 8, 9}
>>> first_set.difference(second_set), first_set - second_set
{1, 2, 3}

4. Set Symmetric Difference
:The symmetric difference between two sets is the set of all the elements that are either in the first set or the second set but not in both.
>>> first_set = {1, 2, 3, 4, 5, 6}
>>> second_set = {4, 5, 6, 7, 8, 9}
>>> first_set.symmetric_difference(second_set), first_set ^ second_set
{1, 2, 3, 7, 8, 9}

5.Other Set Operations in Python
the a.issubset(b) method or <= operator returns true if the a is a subset of b
the a.issuperset(b) method or >= operator returns true if the a is a superset of b
the a.isdisjoint(b) method return true if there are no common elements between sets a and b
Frozen Sets in Python : immutable (you can use them as dictionary keys)
a = frozenset((1, 2, 3, 4)) 
'''
a_list = ['b','c','c','e',1]
b_list = ['a','b','c','c','d',1]
c_list = ['c','e',1]

def find_common(list_a, list_b, list_c):
    return_list = []
    for item in set(list_a):
        if item in list_b and item not in return_list:
            if item in list_c and item not in return_list:    
                return_list.append(item)
    return return_list


def find_common_set(list_a, list_b, list_c):
    common_set_list = list(set(list_a) & set(list_b) & set(list_c)) 
    return common_set_list


def find_common_set2(list_a, list_b, list_c):
    set_a = set(list_a)
    set_b = set(list_b)
    set_c = set(list_c)
    common_set_list = = list(set_a.intersection(set_b).intersection(set_c))
    return common_set_list

print(find_common_set(a_list, b_list, c_list))
