# -*- coding: utf-8 -*-

import random
import string

'''
Funktion um einen Token zu erstellen
:returns Token
'''


# Funktion, die einen eindeutigen 4x4 stelligen Token erzeugt
# der einer Gruppe eindeutig zugeordnet werden kann
def create_token():
    unique = True
    while unique:
        token = ''
        for x in range(0, 4):
            token += ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
            if x <= 2:
                token += '-'
        unique = token_existing(token)

    return token


'''
Wenn Gruppe mit Token bereits vorhanden, neuen Token generieren

:returns boolean ob Gruppe existiert
'''


# Funktion zur ÃœberprÃ¼fung auf einen gÃ¼ltigen Token
def token_existing(token):
    """token der getestet werden soll"""
    # TODO test ob Unique
    return False
