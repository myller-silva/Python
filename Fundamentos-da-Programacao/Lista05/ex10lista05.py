from  random import randint
from  collections import  defaultdict
n1 = [randint(0, 11), randint(0, 11), randint(0, 11), randint(0, 11), randint(0, 11), randint(0, 11), randint(0, 11), randint(0, 11), randint(0, 11), randint(0, 11)]
n2 = defaultdict(list);
for n3, v in enumerate(n1):
    n2[v].append(n3)
for v in n2:
    if len(n2[v]) > 1:
        print(v, n2[v])
