from pygments.style import Style
from pygments.token import Token, Comment, Keyword, Symbols, Name, String, Generic, Number, Operator, Punctuation

class GambitStyle(Style):
    styles = {
        Token:              '',
        Comment:            'italic #0AD0CC',
        Keyword:            'bold #928E01',
        Name:               'bold #19E519',
        String:             'bold #F96600',
        Generic:            'bold #997a26',
        Number:             'bold #FA28EC',
        Operator:           'bold #2883FA',
        Punctuation:        'bold #28FA36',
        Symbols:            'bold #FA9F28',
    }