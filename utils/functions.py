import random


def get_ticket():
    s = '0123456789abcdefghijklmnopqrstuvwxyz'
    ticket = ''
    for i in range(25):
        ticket += random.choice(s)

    return ticket
