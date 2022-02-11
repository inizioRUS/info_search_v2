from math import log2

check_list = {'minecraft': [4, 3, 3, 2, 1, 1, 3, 3, 1],
              'Saratov': [2, 1, 2, 2, 4, 1, 2, 2, 2, 4],
              'ussr': [3, 2, 2, 4, 2, 4, 2, 2, 2, 1],
              'Electromagnetic radiation': [1, 1, 3, 4, 1, 1, 3, 3, 2, 1],
              'BTS': [1, 1, 5, 5, 4, 4, 1, 1, 1, 1],
              'Linkin park': [5, 3, 5, 4, 3, 3, 3, 3, 3, 3],
              'Ronald Reagan': [4, 2, 2, 2, 2, 2, 4, 4, 4, 2]}


def nDSG(spisok, k):
    idsg = 0
    dsg = 0
    for i in range(1, k + 1):
        dsg += spisok[i - 1] / log2(i + 1)
        idsg += sorted(spisok)[-i] / log2(i + 1)
    return dsg / idsg


for k, v in check_list.items():
    print(k, nDSG(v, 9))
