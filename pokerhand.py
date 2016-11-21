def c1(h):
    '''
    Primary Check of h (hand)

    >>> c1([[5, 'H'], [5, 'C'], [6, 'S'], [7, 'S'], [13, 'D']])
    'One Pair'
    
    >>> c1([[5, 'H'], [5, 'C'], [6, 'S'], [13, 'S'], [13, 'D']])
    'Two Pairs'

    >>> c1([[5, 'H'], [6, 'C'], [6, 'S'], [13, 'S'], [13, 'D']])
    'Two Pairs'

    >>> c1([[5, 'H'], [13, 'C'], [6, 'S'], [13, 'S'], [13, 'D']])
    'Three of a Kind'

    >>> c1([[5, 'H'], [5, 'C'], [13, 'S'], [13, 'S'], [13, 'D']])
    'Full House'

    >>> c1([[5, 'H'], [10, 'C'], [6, 'S'], [3, 'S'], [11, 'D']])
    'No Pair'

    >>> c1([[10, 'H'], [10, 'C'], [10, 'S'], [3, 'S'], [10, 'D']])
    'Four of a Kind'
    
    '''
    
    d={}
    for i in [j[0] for j in h]:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    x4 = [i for i in d if d[i]==4]
    x3 = [i for i in d if d[i]==3]
    x2 = [i for i in d if d[i]==2]

    if len(x4) == 1:
        return "Four of a Kind"
    if len(x3) == 1:
        if len(x2) == 1:
            return "Full House"
        elif len(x2) == 0:
            return "Three of a Kind"
    else:
        if len(x2) == 2:
            return "Two Pairs"
        elif len(x2) == 1:
            return "One Pair"
        else:
            return "No Pair"


def clear_data(a):
    '''
    Transform data to suitable format

    >>> clear_data('5H 5C 6S 7S KD')
    [[5, 'H'], [5, 'C'], [6, 'S'], [7, 'S'], [13, 'D']]

    >>> clear_data('2D 3H 7D JD 3D')
    [[2, 'D'], [3, 'H'], [7, 'D'], [11, 'D'], [3, 'D']]
    '''

    d={}
    for i in range(2,10):
        d[str(i)] = i
    d['T'] = 10
    d['J'] = 11
    d['Q'] = 12
    d['K'] = 13
    d['A'] = 14
    h = [[d[i[0]],i[1]] for i in a.split()]
    return h


def is_straight(h):
    '''
    >>> is_straight([[5, 'H'], [5, 'C'], [6, 'S'], [7, 'S'], [13, 'D']])
    False

    >>> is_straight([[5, 'H'], [7, 'C'], [6, 'S'], [8, 'S'], [4, 'D']])
    True

    >>> is_straight([[5, 'H'], [6, 'H'], [7, 'H'], [8, 'H'], [9, 'H']])
    True

    '''
    a = [j[0] for j in h]
    return len(set(a)) ==5 and max(a)-min(a)==4


def high_card(h):
    '''
    >>> high_card([[5, 'H'], [5, 'C'], [6, 'S'], [7, 'S'], [13, 'D']])
    13

    >>> high_card([[5, 'H'], [7, 'C'], [6, 'S'], [8, 'S'], [4, 'D']])
    8

    >>> high_card([[3, 'S'], [10, 'H'], [2, 'H'], [8, 'H'], [9, 'H']])
    10

    '''
    a = [j[0] for j in h]
    return max(a)


def is_flush(h):
    '''
    >>> is_flush([[5, 'H'], [5, 'C'], [6, 'S'], [7, 'S'], [13, 'D']])
    False

    >>> is_flush([[5, 'H'], [7, 'C'], [6, 'S'], [8, 'S'], [4, 'D']])
    False

    >>> is_flush([[3, 'S'], [10, 'S'], [2, 'S'], [8, 'S'], [9, 'S']])
    True
    
    '''
    a = [j[1] for j in h]
    return len(set(a)) == 1



def is_straight_flush(h):
    '''
    >>> is_straight_flush([[5, 'H'], [7, 'H'], [6, 'S'], [8, 'S'], [4, 'D']])
    False

    >>> is_straight_flush([[3, 'S'], [4, 'S'], [6, 'S'], [5, 'S'], [7, 'S']])
    True
    '''
    return is_flush(h) and is_straight(h)

def is_royal_flush(h):
    '''
    >>> is_royal_flush([[5, 'H'], [7, 'H'], [6, 'S'], [8, 'S'], [4, 'D']])
    False

    >>> is_royal_flush([[3, 'S'], [4, 'S'], [6, 'S'], [5, 'S'], [7, 'S']])
    False
    
    >>> is_royal_flush([[10, 'S'], [11, 'S'], [12, 'S'], [13, 'S'], [14, 'S']])
    True
    '''
    return is_straight_flush(h) and max([i[0] for i in h])==14
    

if __name__ == '__main__':
    import doctest, pokerhand
    doctest.testmod(pokerhand)
