LONG = '2'
SHORT = '1'
SEPARATOR = '*'


MORSE_DICT = { 'A': (SHORT, LONG,),
               'B': (LONG, SHORT, SHORT, SHORT,),
               'C': (LONG, SHORT, LONG, SHORT,),
               'D': (LONG, SHORT, SHORT,),
               'E': (SHORT,),
               'F': (SHORT, SHORT, LONG, SHORT,),
               'G': (LONG, LONG, SHORT,),
               'H': (SHORT, SHORT, SHORT, SHORT,),
               'I': (SHORT, SHORT,),
               'J': (SHORT, LONG, LONG, LONG,),
               'K': (LONG, SHORT, LONG,),
               'L': (SHORT, LONG, SHORT, SHORT,),
               'M': (LONG, LONG,),
               'N': (LONG, SHORT,),
               'O': (LONG, LONG, LONG,),
               'P': (SHORT, LONG, LONG, SHORT, ),
               'Q': (LONG, LONG, SHORT, LONG, ),
               'R': (SHORT, LONG, SHORT),
               'S': (SHORT, SHORT, SHORT, ),
               'T': (LONG, ),
               'U': (SHORT, SHORT, LONG, ),
               'V': (SHORT, SHORT, SHORT, LONG, ),
               'W': (SHORT, LONG, LONG),
               'X': (LONG, SHORT, SHORT, LONG, ),
               'Y': (LONG, SHORT, LONG, LONG, ),
               'Z': (LONG, LONG, SHORT, SHORT),
               '1': (SHORT, LONG, LONG, LONG, LONG, ),
               '2': (SHORT, SHORT, LONG, LONG, LONG, ),
               '3': (SHORT, SHORT, SHORT, LONG, LONG),
               '4': (SHORT, SHORT, SHORT, SHORT, LONG, ),
               '5': (SHORT, SHORT, SHORT, SHORT, SHORT, ),
               '6': (LONG, SHORT, SHORT, SHORT, SHORT),
               '7': (LONG, LONG, SHORT, SHORT, SHORT, ),
               '8': (LONG, LONG, LONG, SHORT, SHORT, ),
               '9': (LONG, LONG, LONG, LONG, SHORT),
               '0': (LONG, LONG, LONG, LONG, LONG, ),
               ', ': (LONG, LONG, SHORT, SHORT, LONG, LONG, ),
               '. ': (SHORT, LONG, SHORT, LONG, SHORT, LONG),
               '?': (SHORT, SHORT, LONG, LONG, SHORT, SHORT, ),
               '/': (LONG, SHORT, SHORT, LONG, SHORT, ),
               '-':(LONG, SHORT, SHORT, SHORT, SHORT, LONG),
               '(': (LONG, SHORT, LONG, LONG, SHORT, ),
               ')': (LONG, SHORT, LONG, LONG, SHORT, LONG,)
               }

REVERSED_MORSE = {v: k for (k, v) in MORSE_DICT.items()}


def encode(value_str):
    encoded = ''
    for letter in value_str.upper():
        encoded += ''.join(MORSE_DICT.setdefault(letter, SEPARATOR)) + ' '
    return encoded


def decode(value_str, long=LONG, short=SHORT):
    if long != LONG:
        value_str = value_str.replace(long, LONG)
    if short != SHORT:
        value_str = value_str.replace(short, SHORT)
    decoded = ''
    for letter in value_str.split(' '):
        decoded += REVERSED_MORSE.get(tuple(letter), ' ')
    return decoded
