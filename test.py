import itertools

ids = [1,4,3,3,4,2,3,4,5,6,1]
it = itertools.groupby(ids)
for k, g in it:
    print(k)