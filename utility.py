#!/usr/bin/env python
# -*- coding: utf-8 -*-

#身份证校验
#Y_P = mod( ∑(Ai×Wi),11 )
def is_id_card(haoma):
    if len(str(haoma)) != 18:
        return False
    chmap = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9, 'x': 10, 'X': 10
    }
    try:
        chl = [chmap[ch] for ch in list(str(haoma))]
    except:
        return False
    summ = 0
    for ii, n in enumerate(chl):
        i = 18 - ii
        weight = 2 ** (i - 1) % 11
        summ = (summ + n * weight) % 11
    if summ != 1:
        return False

    return True

#营业执照校验
#公式找不到了，都是黑科技：（
def is_license(haoma):
    if len(str(haoma)) != 15:
        return False
    chmap = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
    }
    try:
        chl = [chmap[ch] for ch in list(str(haoma))]
    except:
        return False
    s = []
    p = [10]
    m = 10
    for ii, n in enumerate(chl):
        s.append(p[ii] % 11 + n)
        if 0 == s[ii] % 10:
            p.append(10 * 2)
        else:
            p.append(s[ii] % m * 2)

    if 1 != s[14] % 10:
        return False

    return True

#组织机构代码校验
def is_org_code(haoma):
    if len(str(haoma)) != 10:
        return False
    if str(haoma)[-2:-1] != '-':
        return False
    chmap = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,
        'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19,
        'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24,
        'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29,
        'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34,
        'Z': 35
    }
    weight = [3, 7, 9, 10, 5, 8, 4, 2]
    M_P = str(haoma)[:-2]
    Y_P = str(haoma)[-1]
    try:
        chl = [chmap[ch] for ch in list(M_P)]
    except:
        return False
    summ = 0
    for ii, n in enumerate(chl):
        summ += n * weight[ii]

    try:
        Y_P = chmap[Y_P]
    except:
        return False

    if Y_P != 11 - summ % 11:
        return False

    return True
