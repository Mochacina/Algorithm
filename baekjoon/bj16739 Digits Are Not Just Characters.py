import re

def split_items(filename):
    return re.findall(r'[A-Za-z]+|\d+', filename)

def compare_items(item1, item2):
    if item1.isdigit() and item2.isdigit():
        return int(item1) - int(item2)
    elif item1.isdigit():
        return -1
    elif item2.isdigit():
        return 1
    else:
        return (item1 > item2) - (item1 < item2)

def compare_filenames(name1, name2):
    items1 = split_items(name1)
    items2 = split_items(name2)
    
    for i in range(min(len(items1), len(items2))):
        cmp = compare_items(items1[i], items2[i])
        if cmp != 0:
            return cmp
    
    return len(items1) - len(items2)

n = int(input())
s0 = input()
for _ in range(n):
    print(['-','+'][compare_filenames(input(),s0) >= 0])
