from math import log2
from math import floor


def print90(h, i, max_i):
    if i < max_i:
        indent = floor(log2(i+1))
        print90(h, (i*2)+2, max_i)
        print('   ' * indent, h[i])
        print90(h, (i*2)+1, max_i)


def insertMinHeap(h, i):
    """insertMinHeap"""
    print('insert', h[i], 'at index', i, end='      ')
    print(h)
    insertEle = h[i]
    fi = (i-1)//2
    while i > 0 and insertEle < h[fi]:
        h[i] = h[fi]
        i = fi
        fi = (i-1)//2
    h[i] = insertEle


h = [30, 85, 97, 100, 200]
for i in range(1, len(h)):
    insertMinHeap(h, i)
    print(h)
    print90(h, 0, i)
    print('------------------\n')






