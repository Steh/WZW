import random
import string
from wzw.models import *

def create_token():
    token = ''
    for x in range(0, 4):
        token += ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
        if x <= 2:
            token += '-'
    return token

# wenn gruppe existiert wird die schleife erneut ausgefuehrt
# wenn nicht wird ein fehler geworfen und die Variable auf False gesetzt
def token_existing(token):
    '''token der getestet werden soll'''
    try:
        Group.objects.get(token=token)
        token_existing = True
    except Group.DoesNotExist:
        token_existing = False
    return token_existing