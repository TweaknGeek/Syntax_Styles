from pygments.style import Style
from pygments.token import Token, Comment, Keyword, Name, String, Generic, Number, Operator, Punctuation

class DarkStyle(Style):
    styles = {
        Token:              '',
        Comment:            'italic #c61313',
        Keyword:            'bold #840f75',
        Name:               'bold #071899',
        String:             'bold #11700f',
        Generic:            'bold #997a26',
        Number:             'bold #247572',
        Operator:           'bold #247572',
        Punctuation:        'bold #840f75',
    }