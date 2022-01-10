# Author: SCT (AMDG) 1/10/22

def double_stuff(lst):
    for i, v in enumerate(lst):
        lst[i] = 2 * v
    return lst


print(double_stuff([2, 3, 4]) == [4, 6, 8])
print(double_stuff([2, 2.5, 3.5]) == [4, 5, 7])
print(double_stuff([2, 2.5, "two"]) == [4, 5, "twotwo"])
