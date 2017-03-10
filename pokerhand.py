#lacks of info: how to rank between colors
#e.g. 5H 5S 6H 6S 7H v.s. 5D 5C 6D 6C 7S

def check_pairs(h):
    '''
    Primary Check of h (hand)

    >>> check_pairs([[5, 2], [5, 1], [6, 3], [7, 3], [13, 0]])
    'One Pair'
    
    >>> check_pairs([[5, 2], [5, 1], [6, 3], [13, 3], [13, 0]])
    ['Two Pairs', 13, 5]

    >>> check_pairs([[5, 2], [6, 1], [6, 3], [13, 3], [13, 0]])
    ['Two Pairs', 13, 6]

    >>> check_pairs([[5, 2], [13, 1], [6, 3], [13, 3], [13, 0]])
    ['Three of a Kind', 13]

    >>> check_pairs([[5, 2], [5, 1], [13, 3], [13, 3], [13, 0]])
    ['Full House', 13]

    >>> check_pairs([[5, 2], [10, 1], [6, 3], [3, 3], [11, 0]])
    'No Pair'

    >>> check_pairs([[10, 2], [10, 1], [10, 3], [3, 3], [10, 0]])
    ['Four of a Kind', 10]
    
    '''
    
    d={}
    for i in h:
        if i[0] in d:
            d[i[0]] += 1
        else:
            d[i[0]] = 1

    x4 = [i for i in h if d[i[0]]==4]
    x3 = [i for i in h if d[i[0]]==3]
    x2 = [i for i in h if d[i[0]]==2]

    if len(x4) == 4:
        return ["Four of a Kind",x4[0][0]] #number
    if len(x3) == 3:
        if len(x2) == 2:
            return ["Full House", x3[0][0]] #number
        elif len(x2) == 0:
            return ["Three of a Kind",x3[0][0]] #number
    else:
        if len(x2) == 4:
            return ["Two Pairs", max([i[0] for i in x2]),min([i[0] for i in x2])]
        elif len(x2) == 2:
            return "One Pair"
        else:
            return "No Pair"


def clear_data(a):
    '''
    Transform data to suitable format

    >>> clear_data('5H 5C 6S 7S KD')
    [[5, 2], [5, 1], [6, 3], [7, 3], [13, 0]]

    >>> clear_data('2D 3H 7D JD 3D')
    [[2, 0], [3, 2], [7, 0], [11, 0], [3, 0]]
    '''

    dn={}
    dc={'S':3, 'H':2, 'C':1, 'D':0}
    for i in range(2,10):
        dn[str(i)] = i
    dn['T'] = 10
    dn['J'] = 11
    dn['Q'] = 12
    dn['K'] = 13
    dn['A'] = 14
    h = [[dn[i[0]],dc[i[1]]] for i in a.split()]
    return h


def is_straight(h):
    '''
    >>> is_straight([[5, 2], [5, 1], [6, 3], [7, 3], [13, 0]])
    False

    >>> is_straight([[5, 2], [7, 1], [6, 3], [8, 3], [4, 0]])
    True

    >>> is_straight([[5, 2], [6, 2], [7, 2], [8, 2], [9, 2]])
    True

    '''
    a = [j[0] for j in h]
    return len(set(a)) ==5 and max(a)-min(a)==4


def high_card(h):
    '''
    >>> high_card([[5, 2], [5, 1], [6, 3], [7, 3], [13, 0]])
    13

    >>> high_card([[5, 2], [7, 1], [6, 3], [8, 3], [4, 0]])
    8

    >>> high_card([[3, 3], [10, 2], [2, 2], [8, 2], [9, 2]])
    10

    '''
    a = [j[0] for j in h]
    return max(a)


def is_flush(h):
    '''
    >>> is_flush([[5, 2], [5, 1], [6, 3], [7, 3], [13, 0]])
    False

    >>> is_flush([[5, 2], [7, 1], [6, 3], [8, 3], [4, 0]])
    False

    >>> is_flush([[3, 3], [10, 3], [2, 3], [8, 3], [9, 3]])
    True
    
    '''
    a = [j[1] for j in h]
    return len(set(a)) == 1



def is_straight_flush(h):
    '''
    >>> is_straight_flush([[5, 2], [7, 2], [6, 3], [8, 3], [4, 0]])
    False

    >>> is_straight_flush([[3, 3], [4, 3], [6, 3], [5, 3], [7, 3]])
    True
    '''
    return is_flush(h) and is_straight(h)

def is_royal_flush(h):
    '''
    >>> is_royal_flush([[5, 2], [7, 2], [6, 3], [8, 3], [4, 0]])
    False

    >>> is_royal_flush([[3, 3], [4, 3], [6, 3], [5, 3], [7, 3]])
    False
    
    >>> is_royal_flush([[10, 3], [11, 3], [12, 3], [13, 3], [14, 3]])
    True
    '''
    return is_straight_flush(h) and max([i[0] for i in h])==14
    

if __name__ == '__main__':
    import doctest, pokerhand
    doctest.testmod(pokerhand)
