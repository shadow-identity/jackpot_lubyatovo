# -*- coding: utf-8 -*-
""" Just for fun
looking for those who are most successful in the lottery at http://www.lubyatovo-promo.ru/
list - text file from http://www.lubyatovo-promo.ru/winners.html with copypasted values (see example)
output -
"""


def jackpot():
    f = open('list', 'r')
    lines = f.readlines()
    phones = [line[10:20] for line in lines]

    jackpot = {}
    for i, string in enumerate(phones):
        if string in jackpot.keys():  # already counted - fufufu
            continue
        for phone in phones[i+1:]:  # search phone for more
            if phone == string:
                if phone in jackpot.keys():
                    jackpot[phone] += 1  # another one entry in record
                else:
                    jackpot[phone] = 2  # find duplicate first time, create record
    return jackpot


if __name__ == '__main__':
    print jackpot()

